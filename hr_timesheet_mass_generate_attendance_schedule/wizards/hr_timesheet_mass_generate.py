# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api


class HrTimesheetMassGenerate(models.TransientModel):
    _inherit = "hr.timesheet_mass_generate"

    working_schedule_id = fields.Many2one(
        string="Working Schedule",
        comodel_name="resource.calendar",
    )

    @api.multi
    def _prepare_data_timesheet(self, employee):
        _super = super(HrTimesheetMassGenerate, self)
        res = _super._prepare_data_timesheet(employee)

        res["working_schedule_id"] = self.working_schedule_id.id

        return res
