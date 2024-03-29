# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=W0622

from datetime import datetime

from dateutil import relativedelta
from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.safe_eval import safe_eval as eval
from pytz import timezone


class HrWorkingSchedulePolicy(models.Model):
    _name = "hr.working_schedule_policy"
    _inherit = "hr.working_schedule_policy"

    @api.model
    def _default_condition_python_code(self):
        return "result = True"

    timesheet_period_computation_method = fields.Selection(
        string="Timesheet Period Computation Method",
        selection=[
            ("code", "Python Code"),
        ],
        default="code",
        required=True,
    )
    python_code = fields.Text(
        string="Python Code for Date To Computation",
    )
    cron_id = fields.Many2one(
        string="Cron",
        comodel_name="ir.cron",
    )
    condition_python_code = fields.Text(
        string="Python Code for Timesheet Creation Condition",
        default=lambda self: self._default_condition_python_code(),
    )

    @api.model
    def _cron_generate_timesheet(self, working_schedule_policy_id):
        working_schedule_policy = self.browse([working_schedule_policy_id])[0]
        working_schedule_policy._generate_timesheet()

    @api.multi
    def action_generate_timesheet(self):
        for document in self:
            document._generate_timesheet()

    @api.multi
    def _generate_timesheet(self):
        self.ensure_one()
        obj_hr_timesheet_sheet = self.env["hr_timesheet_sheet.sheet"]
        employees = self._get_employee()
        for employee in employees:
            tz = employee.user_id.tz
            date_start = datetime.now(timezone(tz))
            if self._compute_timesheet_creation_condition(employee, date_start):
                obj_hr_timesheet_sheet.create(
                    self._prepare_timesheet_create(employee, date_start)
                )

    @api.multi
    def _prepare_timesheet_create(self, employee, date_start):
        self.ensure_one()
        return {
            "date_from": date_start,
            "date_to": self._compute_date_end(employee, date_start),
            "employee_id": employee.id,
        }

    @api.multi
    def _get_employee(self):
        self.ensure_one()
        criteria = [
            ("working_schedule_policy_ids", "in", self.id),
        ]
        obj_employee = self.env["hr.employee"]
        return obj_employee.search(criteria)

    @api.multi
    def _get_localdict(self, employee, date_from):
        self.ensure_one()
        return {
            "env": self.env,
            "document": self,
            "relativedelta": relativedelta,
            "datetime": datetime,
            "employee": employee,
            "date_from": date_from,
        }

    @api.multi
    def _compute_date_end(self, employee, date_from):
        self.ensure_one()
        result = 0.0
        localdict = self._get_localdict(employee, date_from)
        try:
            eval(self.python_code, localdict, mode="exec", nocopy=True)
            result = localdict["result"]
        except:  # noqa: E722
            raise UserError(_("Error in date to computation"))
        return result

    @api.multi
    def _compute_timesheet_creation_condition(self, employee, date_from):
        self.ensure_one()
        result = 0.0
        localdict = self._get_localdict(employee, date_from)
        try:
            eval(self.condition_python_code, localdict, mode="exec", nocopy=True)
            result = localdict["result"]
        except:  # noqa: E722
            raise UserError(_("Error in timesheet creation condition"))
        return result

    @api.multi
    def action_create_cron(self):
        for document in self:
            document._create_cron()

    @api.multi
    def action_delete_cron(self):
        for document in self:
            document._delete_cron()

    @api.multi
    def _delete_cron(self):
        self.ensure_one()
        if self.cron_id:
            self.cron_id.unlink()

    @api.multi
    def _create_cron(self):
        self.ensure_one()
        if self.cron_id:
            strWarning = _("Cron already exist")
            raise UserError(strWarning)

        obj_cron = self.env["ir.cron"]
        name = "Working Schedule Policy: %s" % self.name
        args = "[%s]" % (str(self.id))
        cron = obj_cron.create(
            {
                "name": name,
                "user_id": self.env.user.id,
                "active": False,
                "model": "hr.working_schedule_policy",
                "function": "_cron_generate_timesheet",
                "args": args,
            }
        )
        self.cron_id = cron
