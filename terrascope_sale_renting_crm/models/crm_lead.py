# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def _get_action_rental_context(self):

        order_lines = []
        for line in self:
            order_lines.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.product_id.get_product_multiline_description_sale()
            }))

        return {
            "search_default_opportunity_id": self.id,
            "default_opportunity_id": self.id,
            "search_default_partner_id": self.partner_id.id,
            "default_partner_id": self.partner_id.id,
            "default_team_id": self.team_id.id,
            "default_campaign_id": self.campaign_id.id,
            "default_medium_id": self.medium_id.id,
            "default_origin": self.name,
            "default_source_id": self.source_id.id,
            "default_company_id": self.company_id.id or self.env.company.id,
            "default_is_rental_order": True,
            "default_order_line": order_lines,
        }
