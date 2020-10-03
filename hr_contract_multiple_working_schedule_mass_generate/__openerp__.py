# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Mass Generate Timesheet From "
            "Contract Multiple Working Schedule",
    "version": "8.0.1.1.1",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_contract_multiple_working_schedule",
        "hr_timesheet_sheet",
    ],
    "data": [
        "views/hr_working_schedule_policy_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
