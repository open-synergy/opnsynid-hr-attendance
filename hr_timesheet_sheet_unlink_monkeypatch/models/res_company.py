# -*- coding: utf-8 -*-
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResCompany(models.Model):
    _name = "res.company"
    _inherit = "res.company"

    check_timesheet_attendance_unlink = fields.Boolean(
        string="Check Attendance When Unlink",
        default=True,
    )
    delete_timesheet_sheet_unlink = fields.Boolean(
        string="Delete Timesheet Detail When Unlink",
        default=True,
    )
