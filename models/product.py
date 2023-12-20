from odoo import models, fields, api


class Product(models.Model):
    _name = 'shop.product'
    _description = 'Product Class'

    product_id = fields.Integer(string='Product ID', readonly=True)
    product_number = fields.Char(string='Product Number')
    brand = fields.Char(string='Brand')
    model = fields.Char(string='Model')
    other_info = fields.Char(string='Other Information')
    weight = fields.Float(string='Weight')
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    create_timestamp = fields.Datetime(string='Create Timestamp', default=fields.Datetime.now, readonly=True)

    supplier_id = fields.Many2one(comodel_name='shop.supplier', string='Supplier')
    tag_id = fields.Many2one(comodel_name='shop.tag', string='Tag')

    product_productsBought = fields.One2many(comodel_name='shop.products_bought', inverse_name='product_id',
                                             string='ProductsBought')
