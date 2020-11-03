# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models


class HrPromotionTransition(models.Model):
    _name = "hr.promotion_transition"
    _inherit = [
        "hr.promotion_transition",
        "hr.career_transition"
    ]
