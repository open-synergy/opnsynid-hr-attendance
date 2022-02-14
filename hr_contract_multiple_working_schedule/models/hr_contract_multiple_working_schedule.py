# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrContractMultipleWorkingSchedule(models.Model):
    _name = "hr.contract_multiple_working_schedule"
    _description = "Contract Multiple Working Schedule"

    contract_id = fields.Many2one(
        string="# Employee Contract",
        comodel_name="hr.contract",
        required=True,
    )
    working_schedule_policy_id = fields.Many2one(
        string="Working Schedule Policy",
        comodel_name="hr.working_schedule_policy",
        required=True,
    )
    working_schedule_id = fields.Many2one(
        string="Working Schedule",
        comodel_name="resource.calendar",
        required=True,
    )
