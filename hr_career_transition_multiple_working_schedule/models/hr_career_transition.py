# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import api, fields, models


class HrCareerTransition(models.Model):
    _inherit = "hr.career_transition"

    new_multiple_working_schedule_ids = fields.One2many(
        string="New Multiple Working Schedule",
        comodel_name="hr.career_transition_new_multiple_working_schedule",
        inverse_name="career_transition_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    previous_multiple_working_schedule_ids = fields.One2many(
        string="Previous Multiple Working Schedule",
        comodel_name="hr.career_transition_previous_multiple_working_schedule",
        inverse_name="career_transition_id",
    )
    change_multiple_working_schedule = fields.Boolean(
        string="Change Multiple Working Schedule?",
        related="type_id.change_multiple_working_schedule",
    )

    @api.multi
    def _get_value_before_onchange_previous_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._get_value_before_onchange_previous_contract()
        result.update(
            {
                "new_multiple_working_schedule_ids": [],
                "previous_multiple_working_schedule_ids": [],
            }
        )
        return result

    @api.multi
    def _get_value_after_onchange_previous_contract(self, previous_contract):
        _super = super(HrCareerTransition, self)
        result = _super._get_value_after_onchange_previous_contract(previous_contract)
        result.update(
            {
                "new_multiple_working_schedule_ids": previous_contract._get_multiple_working_schedule_dict(),  # noqa: B950
                "previous_multiple_working_schedule_ids": previous_contract._get_multiple_working_schedule_dict(),  # noqa: B950
            }
        )
        return result

    @api.multi
    def _prepare_new_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_new_contract()
        working_schedule_ids = []
        for schedule in self.new_multiple_working_schedule_ids:
            working_schedule_policy_id = schedule.working_schedule_policy_id.id
            working_schedule_id = schedule.working_schedule_id.id
            working_schedule_ids.append(
                (
                    0,
                    0,
                    {
                        "working_schedule_policy_id": working_schedule_policy_id,
                        "working_schedule_id": working_schedule_id,
                    },
                )
            )
        result.update(
            {
                "working_schedule_ids": working_schedule_ids,
            }
        )
        return result

    @api.multi
    def _prepare_contract_revert(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_contract_revert()
        self.previous_contract_id.working_schedule_ids.unlink()
        working_schedule_ids = []
        for schedule in self.previous_multiple_working_schedule_ids:
            working_schedule_policy_id = schedule.working_schedule_policy_id.id
            working_schedule_id = schedule.working_schedule_id.id
            working_schedule_ids.append(
                (
                    0,
                    0,
                    {
                        "working_schedule_policy_id": working_schedule_policy_id,
                        "working_schedule_id": working_schedule_id,
                    },
                )
            )
        result.update(
            {
                "working_schedule_ids": working_schedule_ids,
            }
        )
        return result

    @api.multi
    def _prepare_contract_update(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_contract_update()
        self.previous_contract_id.working_schedule_ids.unlink()
        working_schedule_ids = []
        for schedule in self.new_multiple_working_schedule_ids:
            working_schedule_policy_id = schedule.working_schedule_policy_id.id
            working_schedule_id = schedule.working_schedule_id.id
            working_schedule_ids.append(
                (
                    0,
                    0,
                    {
                        "working_schedule_policy_id": working_schedule_policy_id,
                        "working_schedule_id": working_schedule_id,
                    },
                )
            )
        result.update(
            {
                "working_schedule_ids": working_schedule_ids,
            }
        )
        return result


class HrCareerTransitionNewMultipleWorkingSchedule(models.Model):
    _name = "hr.career_transition_new_multiple_working_schedule"
    _description = "Career Transition New Multiple Working Schedule"

    career_transition_id = fields.Many2one(
        string="Career Transition",
        comodel_name="hr.career_transition",
    )
    working_schedule_policy_id = fields.Many2one(
        string="Working Schedule Policy",
        comodel_name="hr.working_schedule_policy",
    )
    working_schedule_id = fields.Many2one(
        string="Working Schedule",
        comodel_name="resource.calendar",
    )


class HrCareerTransitionPreviousMultipleWorkingSchedule(models.Model):
    _name = "hr.career_transition_previous_multiple_working_schedule"
    _description = "Career Transition Previous Multiple Working Schedule"

    career_transition_id = fields.Many2one(
        string="Career Transition",
        comodel_name="hr.career_transition",
    )
    working_schedule_policy_id = fields.Many2one(
        string="Working Schedule Policy",
        comodel_name="hr.working_schedule_policy",
    )
    working_schedule_id = fields.Many2one(
        string="Working Schedule",
        comodel_name="resource.calendar",
    )
