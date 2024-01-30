from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    image = fields.Binary(string='Image URL', help='URL to the custom image for the product')

    supplier_id = fields.Many2one(comodel_name='shop.supplier', string='Supplier')
    tag_id = fields.Many2one(comodel_name='shop.tag', string='Tag')

    product_productsBought = fields.One2many(comodel_name='shop.products_bought', inverse_name='product_id',
                                             string='ProductsBought')

    # Existing Function Corrections

    @api.constrains('brand', 'model', 'other_info', 'description')
    def _check_string_values(self):
        if self.brand and (len(self.brand) > 255 or not self.brand.strip()):
            raise ValidationError('The brand cannot be empty or exceed 255 characters.')
        if self.model and (len(self.model) > 255 or not self.model.strip()):
            raise ValidationError('The model cannot be empty or exceed 255 characters.')
        if self.other_info and (len(self.other_info) > 255 or not self.other_info.strip()):
            raise ValidationError('The other information cannot be empty or exceed 255 characters.')
        if self.description and len(self.description) > 255:
            raise ValidationError('The description cannot exceed 255 characters.')

    @api.onchange('weight', 'price')
    def _onchange_numeric_values(self):
        if self.weight is not None and self.weight < 0:
            self.weight = 0
            return {'warning': {'title': 'Invalid Weight', 'message': 'The weight cannot be negative.'}}
        if self.price is not None and self.price < 0:
            self.price = 0
            return {'warning': {'title': 'Invalid Price', 'message': 'The price cannot be negative.'}}

    # Override Copy Method
    def copy(self, default=None):
        default = dict(default or {})
        # Modify a specific field, e.g., product_number
        modified_product_number = self.product_number + "_copy"  # This is an example
        default['product_number'] = modified_product_number
        return super(Product, self).copy(default)
