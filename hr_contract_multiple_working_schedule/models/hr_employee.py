# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class HrEmployee(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"

    @api.depends(
        "current_contract_id",
        "current_contract_id.working_schedule_ids",
    )
    def _compute_working_schedule_policy(self):
        for document in self:
            result = []
            if document.current_contract_id:
                contract = document.current_contract_id
                for policy in contract.working_schedule_ids:
                    result.append(policy.working_schedule_policy_id.id)

            document.working_schedule_policy_ids = result

    working_schedule_policy_ids = fields.Many2many(
        string="Working Schedule Policies",
        comodel_name="hr.working_schedule_policy",
        relation="rel_employee_2_working_schedule_policy",
        column1="employee_id",
        column2="working_schedule_policy_id",
        compute="_compute_working_schedule_policy",
        store=True,
    )
