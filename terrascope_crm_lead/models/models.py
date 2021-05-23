# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lead(models.Model):
    _inherit = 'crm.lead'

    no_of_passengers = fields.Integer(string='Number of Passengers')
    destination = fields.Char(string='Destination')
    pickup_time_date = fields.Datetime(string='Pickup Date & Time')
    food_drink_needed = fields.Boolean(string='Food & Drinks Needed?')
    product_id = fields.Many2one(comodel_name='product.template', string='Product')