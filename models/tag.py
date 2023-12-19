from odoo import models, fields

class Tag(models.Model):
    _name = 'your_module.tag'
    _description = 'Tag Model'

    tag_id = fields.Integer(string='Tag ID')
    type = fields.Char(string='Type')
    label = fields.Char(string='Label')
    active = fields.Boolean(string='Active')
    create_timestamp = fields.Datetime(string='Create Timestamp')


    tag_products = fields.One2many(comodel_name="our_shop.product", inverse_name="product_id", string="Products")

