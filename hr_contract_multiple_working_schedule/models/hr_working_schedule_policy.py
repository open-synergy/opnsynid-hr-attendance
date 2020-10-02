# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrWorkingSchedulePolicy(models.Model):
    _name = "hr.working_schedule_policy"
    _description = "Working Schedule Policy"

    name = fields.Char(
        string="Working Schedule Policy",
        required=True
    )
    code = fields.Char(
        string="Code",
    )
    description = fields.Text(
        string="Description"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
