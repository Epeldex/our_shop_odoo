from odoo import models, fields


class Supplier(models.Model):
    _name = 'shop.supplier'
    _description = 'Supplier Information'

    supplier_id = fields.Integer(string='Supplier ID')
    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    country = fields.Char(string='Country')
    zip = fields.Integer(string='ZIP Code')
    create_timestamp = fields.Datetime(string='Create Timestamp')
    supplier_products = fields.One2many(comodel_name='shop.product', inverse_name='product_id', string='Products')


