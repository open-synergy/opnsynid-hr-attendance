# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Career Transition - Multiple Working Schedule Integration",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_career_transition",
        "hr_contract_multiple_working_schedule",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_career_transition_type_views.xml",
        "views/hr_career_transition_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
