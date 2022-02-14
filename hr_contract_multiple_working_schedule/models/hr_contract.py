# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrContract(models.Model):
    _name = "hr.contract"
    _inherit = "hr.contract"

    working_schedule_ids = fields.One2many(
        string="Working Schedules",
        comodel_name="hr.contract_multiple_working_schedule",
        inverse_name="contract_id",
    )
