# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Timesheet Attendance Schedule Integration With "
    "Contract Multiple Working Schedule",
    "version": "8.0.1.0.2",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_contract_multiple_working_schedule_mass_generate",
        "hr_timesheet_attendance_schedule",
    ],
    "data": [],
    "images": [
        "static/description/banner.png",
    ],
}
