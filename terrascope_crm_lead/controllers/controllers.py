 # -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm

class WebsiteCrmLead(http.Controller):
    @http.route('/contactus', type='http', auth="public", website=True)
    def index(self, **kw):
        product_id = http.request.env['product.template'].sudo().search([])
        return http.request.render("terrascope_crm_lead.terrascope_crm_contactus_form", {'product_id':product_id})