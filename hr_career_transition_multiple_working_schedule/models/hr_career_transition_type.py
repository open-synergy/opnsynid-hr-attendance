# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class HrCareerTransitionType(models.Model):
    _inherit = "hr.career_transition_type"

    change_multiple_working_schedule = fields.Boolean(
        string="Change Multiple Working Schedule?",
    )
