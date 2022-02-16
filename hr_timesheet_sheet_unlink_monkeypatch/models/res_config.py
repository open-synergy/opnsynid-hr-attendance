# -*- coding: utf-8 -*-
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResConfig(models.TransientModel):
    _inherit = "hr.attendance_config_setting"

    check_timesheet_attendance_unlink = fields.Boolean(
        string="Check Attendance When Unlink",
        related="company_id.check_timesheet_attendance_unlink",
    )
    delete_timesheet_sheet_unlink = fields.Boolean(
        string="Delete Timesheet Detail When Unlink",
        related="company_id.delete_timesheet_sheet_unlink",
    )
