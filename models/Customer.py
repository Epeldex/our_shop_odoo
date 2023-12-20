from odoo import models, fields


class Customer(models.Model):

    _name = 'shop.customer'
    _description = 'Customer entity'

    # Fields definition
    customer_id = fields.Integer(string='Customer ID', readonly=True)
    full_name = fields.Char(string='Full Name')
    email = fields.Char(string='Email')
    street = fields.Char(string='Street Address')
    postal_code = fields.Integer(string='Postal Code')
    city = fields.Char(string='City')
    phone = fields.Char(string='Phone Number')
    balance = fields.Float(string='Balance')
    customer_products = fields.One2many(comodel_name='shop.products_bought', inverse_name='customer_id',
                                             string='ProductsBought')

