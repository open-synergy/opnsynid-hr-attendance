# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api
from datetime import datetime
import pytz


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    @api.multi
    def _check_existing_schedule(self, dt_start, dt_end):
        _super = super(HrTimesheetSheet, self)
        res = _super._check_existing_schedule(dt_start, dt_end)

        employee = self.employee_id
        company = self.company_id
        country_id = False
        state_id = False

        if employee.user_id and employee.user_id.tz:
            tz = pytz.timezone(employee.user_id.tz)
        else:
            tz = pytz.timezone(company.partner_id.tz)

        convert_dt = datetime.strptime(dt_start, "%Y-%m-%d %H:%M:%S")
        convert_utc = pytz.utc.localize(convert_dt).astimezone(tz)
        conv_date = convert_utc.strftime("%Y-%m-%d")

        obj_base_public_holiday = \
            self.env["base.public.holiday"]

        if employee.address_home_id and employee.address_home_id.country_id:
            country_id = employee.address_home_id.country_id.id
        if employee.address_home_id and employee.address_home_id.state_id:
            state_id = employee.address_home_id.state_id.id

        if obj_base_public_holiday.is_public_holiday(
            conv_date,
            country_id=country_id,
            state_id=state_id
        ):
            return False
        else:
            return res
