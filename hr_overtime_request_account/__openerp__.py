# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "HR Attendance Overtime Request - Integration with Accounting",
    "version": "8.0.1.0.0",
    "category": "Human Resources",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr_attendance_overtime_request",
        "account",
    ],
    "data": [
        "views/hr_overtime_request_views.xml",
    ],
}
