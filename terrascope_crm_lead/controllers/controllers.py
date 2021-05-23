 # -*- coding: utf-8 -*-

from odoo import http

class WebsiteCrmLead(http.Controller):
    @http.route('/contactus', type='http', auth="public", website=True)
    def index(self, **kw):
        destination_id = http.request.env['product.attribute.value'].sudo().search([('attribute_id.name', '=', 'Location')])
        dest = []
        for ids in destination_id:
            dest.append(ids.id)
        product_id = http.request.env['product.template'].sudo().search([('attribute_line_ids.value_ids', 'in', dest)])
        return http.request.render("terrascope_crm_lead.terrascope_crm_contactus_form", {'product_id':product_id , 'destination_id':destination_id})