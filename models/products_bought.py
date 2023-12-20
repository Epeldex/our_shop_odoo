from odoo import models, fields


class ProductsBought(models.Model):
    _name = 'shop.products_bought'
    _description = 'Information about products that were bought'

    product_id = fields.Many2one('shop.product', string='Referenced product ID')
    customer_id = fields.Many2one('shop.customer', string='Referenced customer ID')
    amount = fields.Integer(string='Amount')
    bought_timestamp = fields.Date(string='Bought Timestamp')
