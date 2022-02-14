# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class HrContract(models.Model):
    _inherit = "hr.contract"

    @api.multi
    def _get_multiple_working_schedule_dict(self):
        self.ensure_one()
        result = []
        for document in self.working_schedule_ids:
            working_schedule_policy_id = document.working_schedule_policy_id.id
            working_schedule_id = document.working_schedule_id.id
            result.append(
                (
                    0,
                    0,
                    {
                        "working_schedule_policy_id": working_schedule_policy_id,
                        "working_schedule_id": working_schedule_id,
                    },
                )
            )
        return result
