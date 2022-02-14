# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class HrWorkingSchedulePolicy(models.Model):
    _name = "hr.working_schedule_policy"
    _inherit = "hr.working_schedule_policy"

    @api.multi
    def _prepare_timesheet_create(self, employee, date_start):
        _super = super(HrWorkingSchedulePolicy, self)
        result = _super._prepare_timesheet_create(employee, date_start)
        obj_schedule = self.env["hr.contract_multiple_working_schedule"]
        criteria = [
            ("contract_id", "=", employee.current_contract_id.id),
            ("working_schedule_policy_id", "=", self.id),
        ]
        schedules = obj_schedule.search(criteria)
        result.update(
            {
                "working_schedule_id": schedules[0].working_schedule_id.id,
            }
        )
        return result
