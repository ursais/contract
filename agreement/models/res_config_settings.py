# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_agreement_maintenance = fields.Boolean(
        string='Manage maintenance agreements and contracts.')
    module_agreement_mrp = fields.Boolean(
        string='Link your manufacturing orders to an agreement.')
    module_agreement_project = fields.Boolean(
        string='Link your projects and tasks to an agreement.')
    module_agreement_repair = fields.Boolean(
        string='Link your repair orders to an agreement.')
    module_agreement_rma = fields.Boolean(
        string='Link your RMAs to an agreement.')
    module_agreement_stock = fields.Boolean(
        string='Link your pickings to an agreement.')
    module_fieldservice_agreement = fields.Boolean(
        string='Link your Field Service orders to an agreement.')
    module_fieldservice_equipment_agreement = fields.Boolean(
        string='Link your Field Service equipments to an agreement.')
    module_helpdesk_agreement = fields.Boolean(
        string='Link your Helpdesk tickets to an agreement.')
