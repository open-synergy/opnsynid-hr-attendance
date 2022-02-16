# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from openerp import _, api, models
from openerp.exceptions import Warning as UserError
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from pytz import timezone, utc


class HrTimesheetSheet(models.Model):
    _name = "hr_timesheet_sheet.sheet"
    _inherit = "hr_timesheet_sheet.sheet"

    @api.multi
    # pylint: disable=W8106
    def unlink(self):
        for sheet in self:
            sheet._check_attendance_unlink()
            sheet._check_state_unlink()
            sheet._unlink_timesheet_detail()
        return models.Model.unlink(self)

    @api.multi
    def _check_attendance_unlink(self):
        self.ensure_one()
        error_msg = _("You cannot delete a timesheet which have attendance entries")
        if (
            self.company_id.check_timesheet_attendance_unlink
            and self.total_attendance != 0.0
        ):
            raise UserError(error_msg)
        return True

    @api.multi
    def _check_state_unlink(self):
        self.ensure_one()
        strWarning = _("You can only delete data on New or Open state")
        if self.state not in ["draft", "open"]:
            if not self.env.context.get("force_unlink", False):
                raise UserError(strWarning)

    @api.multi
    def _unlink_timesheet_detail(self):
        self.ensure_one()
        if self.company_id.delete_timesheet_sheet_unlink:
            self.timesheet_ids.unlink()

    @api.multi
    def action_recompute_attendance(self):
        for record in self:
            record._recompute_attendance()

    @api.multi
    def _recompute_attendance(self):
        self.ensure_one()
        obj_attendance = self.env["hr.attendance"]
        date_from, date_to = self._convert_sheet_date_tz()
        criteria = [
            ("employee_id.id", "=", self.employee_id.id),
            ("name", ">=", date_from),
            ("name", "<=", date_to),
        ]
        obj_attendance.search(criteria)._compute_sheet()

    @api.multi
    def _convert_sheet_date_tz(self):
        self.ensure_one()

        employee_tz = timezone("utc")

        date_from = self.date_from + " 00:00:00"
        date_to = self.date_to + " 23:59:00"

        if self.employee_id.user_id:
            user = self.employee_id.user_id
            if user.partner_id.tz:
                employee_tz = timezone(user.partner_id.tz)

        date_from_employee_tz = datetime.strptime(
            date_from, DEFAULT_SERVER_DATETIME_FORMAT
        )
        date_to_employee_tz = datetime.strptime(date_to, DEFAULT_SERVER_DATETIME_FORMAT)

        date_from_employee_tz = employee_tz.localize(date_from_employee_tz)
        date_to_employee_tz = employee_tz.localize(date_to_employee_tz)

        date_from_employee_tz = date_from_employee_tz.astimezone(utc)
        date_to_employee_tz = date_to_employee_tz.astimezone(utc)

        date_from_employee_tz = date_from_employee_tz.strftime(
            DEFAULT_SERVER_DATETIME_FORMAT
        )
        date_to_employee_tz = date_to_employee_tz.strftime(
            DEFAULT_SERVER_DATETIME_FORMAT
        )

        return date_from_employee_tz, date_to_employee_tz
