# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models


class HrDemotionTransition(models.Model):
    _name = "hr.demotion_transition"
    _inherit = [
        "hr.demotion_transition",
        "hr.career_transition"
    ]
