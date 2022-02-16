# -*- coding: utf-8 -*-
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Timesheet Unlink Monkey Patch",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_sheet",
        "hr_attendance_configuration_page",
    ],
    "data": [
        "data/ir_actions_server_data.xml",
        "views/hr_attendance_config_setting_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
