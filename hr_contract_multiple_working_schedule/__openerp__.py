# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Contract Multiple Working Schedule",
    "version": "8.0.2.0.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_employee_data_from_contract",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_working_schedule_policy_views.xml",
        "views/hr_contract_views.xml",
        "views/hr_employee_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
