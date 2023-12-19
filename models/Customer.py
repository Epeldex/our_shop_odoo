from odoo import models, fields

class Customer(models.Model):

    _inherit = 'user.user'
    _name = 'entities.customer'
    _description = 'Customer entity'

    # Fields definition
    full_name = fields.Char(string='Full Name')
    email = fields.Char(string='Email')
    street = fields.Char(string='Street Address')
    postal_code = fields.Integer(string='Postal Code')
    city = fields.Char(string='City')
    phone = fields.Char(string='Phone Number')
    balance = fields.Float(string='Balance')

    customer_products = fields.One2many(comodel_name="our_shop.product", inverse_name="product_id", string="Products")