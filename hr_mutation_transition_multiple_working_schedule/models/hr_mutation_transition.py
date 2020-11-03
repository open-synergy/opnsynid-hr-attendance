# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models


class HrMutationTransition(models.Model):
    _name = "hr.mutation_transition"
    _inherit = [
        "hr.mutation_transition",
        "hr.career_transition"
    ]
