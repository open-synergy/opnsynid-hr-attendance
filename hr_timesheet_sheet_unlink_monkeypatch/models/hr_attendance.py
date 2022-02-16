# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrAttendance(models.Model):
    _name = "hr.attendance"
    _inherit = "hr.attendance"

    @api.multi
    def _check(self):
        return True

    @api.depends(
        "employee_id",
        "name",
    )
    def _compute_sheet(self):
        obj_sheet = self.env["hr_timesheet_sheet.sheet"]
        for document in self:
            date_tz = self._get_attendance_employee_tz(
                document.employee_id.id, document.name
            )
            criteria = [
                ("date_to", ">=", date_tz),
                ("date_from", "<=", date_tz),
                ("employee_id.id", "=", document.employee_id.id),
            ]
            sheets = obj_sheet.search(criteria)
            if len(sheets) > 0:
                document.sheet_id = sheets[0]

    sheet_id = fields.Many2one(
        compute="_compute_sheet",
        store=True,
    )
