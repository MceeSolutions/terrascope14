 # -*- coding: utf-8 -*-

import json
from odoo import http

class WebsiteCrmLead(http.Controller):
    @http.route('/contactus', type='http', auth="public", website=True)
    def index(self, **kw):
        default_values = {}
        destination_id = http.request.env['product.attribute.value'].sudo().search([('attribute_id.name', '=', 'Location')])
        dest = []
        for ids in destination_id:
            dest.append(ids.id)
        product_id = http.request.env['product.template'].sudo().search([('attribute_line_ids.value_ids', 'in', dest)])
        for cost in product_id:
            default_values['estimated_cost'] = cost.list_price
        return http.request.render("terrascope_crm_lead.terrascope_crm_contactus_form", {'default_values': default_values, 'product_id':product_id , 'destination_id':destination_id})

    @http.route('/fetch/estimatedprice', type='json', auth="public", website=True)
    def get_price(self, **kw):
        # print('kwagrs >>>>>>>>>', kw)
        product_id = kw.get('product_id')
        destination_id = kw.get('dest_id')
        product = http.request.env['product.product'].sudo().search([('product_tmpl_id', '=', product_id), ('product_template_attribute_value_ids.name', '=', destination_id)])
        # print('product >>>>>>>>>', product)
        if product:
            currency_symbol = product.currency_id.symbol
            price = product.lst_price
            currency = "{:,.2f}".format(price)
            return currency_symbol + currency
        else:
            msg = '<p style="color:Red;"> Boat currently not available for selected destination <p/>'
            return msg
        #pass

class ConceptBoat(http.Controller):
    @http.route('/concept-boat', type='http', auth="public", website=True)
    def index(self, **kw):
        default_values = {}
        destination_id = http.request.env['product.attribute.value'].sudo().search([('attribute_id.name', '=', 'Location')])
        dest = []
        for ids in destination_id:
            dest.append(ids.id)
        product_id = http.request.env['product.template'].sudo().search([('attribute_line_ids.value_ids', 'in', dest), ('name', '=', 'Concept Boat 27 (Atalanta)')])
        #product_varaint_id = http.request.env['product.product'].sudo().search([('id', 'in', destination_id.id), ('product_tmpl_id', '=', product_id.id)])

        for cost in product_id:
            # estimated_cost = cost.list_price
            default_values['estimated_cost'] = cost.list_price
            # default_values['estimated_cost'] = cost.lst_price
        return http.request.render("terrascope_crm_lead.terrascope_concept_boats", {'default_values': default_values, 'product_id':product_id , 'destination_id':destination_id})

class NauticaRib(http.Controller):
    @http.route('/nautica-rib', type='http', auth="public", website=True)
    def index(self, **kw):
        default_values = {}
        destination_id = http.request.env['product.attribute.value'].sudo().search([('attribute_id.name', '=', 'Location')])
        dest = []
        for ids in destination_id:
            dest.append(ids.id)
        product_id = http.request.env['product.template'].sudo().search([('attribute_line_ids.value_ids', 'in', dest), ('name', '=', 'Nautica Rib')])
        
        for cost in product_id:
            default_values['estimated_cost'] = cost.list_price
        return http.request.render("terrascope_crm_lead.terrascope_nautica_ribs", {'default_values': default_values, 'product_id':product_id , 'destination_id':destination_id})

class Searay_Sunsport_290_SS(http.Controller):
    @http.route('/searay-sunsport-290-SS', type='http', auth="public", website=True)
    def index(self, **kw):
        default_values = {}
        destination_id = http.request.env['product.attribute.value'].sudo().search([('attribute_id.name', '=', 'Location')])
        dest = []
        for ids in destination_id:
            dest.append(ids.id)
        product_id = http.request.env['product.template'].sudo().search([('attribute_line_ids.value_ids', 'in', dest), ('name', '=', 'Searay Sunsport 290 SS')])
        
        for cost in product_id:
            default_values['estimated_cost'] = cost.list_price
        return http.request.render("terrascope_crm_lead.searay_sunsport_290_SSs", {'default_values': default_values, 'product_id':product_id , 'destination_id':destination_id})

class AquaTerraBoat(http.Controller):
    @http.route('/aqua-terra-boat', type='http', auth="public", website=True)
    def index(self, **kw):
        default_values = {}
        destination_id = http.request.env['product.attribute.value'].sudo().search([('attribute_id.name', '=', 'Location')])
        dest = []
        for ids in destination_id:
            dest.append(ids.id)
        product_id = http.request.env['product.template'].sudo().search([('attribute_line_ids.value_ids', 'in', dest), ('name', '=', 'Aqua-Terra Boat')])
        
        for cost in product_id:
            default_values['estimated_cost'] = cost.list_price
        return http.request.render("terrascope_crm_lead.aqua-terra_boats", {'default_values': default_values, 'product_id':product_id , 'destination_id':destination_id})

class Searay175SportBoat(http.Controller):
    @http.route('/searay-175-sport-boat', type='http', auth="public", website=True)
    def index(self, **kw):
        default_values = {}
        destination_id = http.request.env['product.attribute.value'].sudo().search([('attribute_id.name', '=', 'Location')])
        dest = []
        for ids in destination_id:
            dest.append(ids.id)
        product_id = http.request.env['product.template'].sudo().search([('attribute_line_ids.value_ids', 'in', dest), ('name', '=', 'Searay 175 Sport Boat')])
        
        for cost in product_id:
            default_values['estimated_cost'] = cost.list_price
        return http.request.render("terrascope_crm_lead.searay_175_port_boats", {'default_values': default_values, 'product_id':product_id , 'destination_id':destination_id})

class ChrisCraftBoat(http.Controller):
    @http.route('/chris-craft-boat', type='http', auth="public", website=True)
    def index(self, **kw):
        default_values = {}
        destination_id = http.request.env['product.attribute.value'].sudo().search([('attribute_id.name', '=', 'Location')])
        dest = []
        for ids in destination_id:
            dest.append(ids.id)
        product_id = http.request.env['product.template'].sudo().search([('attribute_line_ids.value_ids', 'in', dest), ('name', '=', 'Chris Craft Boat')])
        
        for cost in product_id:
            default_values['estimated_cost'] = cost.list_price
        return http.request.render("terrascope_crm_lead.chris_craft_boats", {'default_values': default_values, 'product_id':product_id , 'destination_id':destination_id})