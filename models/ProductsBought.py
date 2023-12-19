from odoo import models, fields

class ProductsBought(models.Model):

    _name = 'entities.products_bought'
    _description = 'Information about products that were bought'

    customer_id = fields.Many2one(comodel_name="our_shop.Customer", string="Customer")
    product_id = fields.Many2one(comodel_name="our_shop.product", string="Product")

    # The amount of products bought
    amount = fields.Integer(string='Amount')

    # The timestamp indicating when the products were bought
    bought_timestamp = fields.Datetime(string='Bought Timestamp')




