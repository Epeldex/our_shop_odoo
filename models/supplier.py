from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    image = fields.Binary(string='Image URL', help='URL to the custom image for the supplier')

    @api.constrains('name', 'country')
    def _check_string_values(self):
        if self.name and (len(self.name) > 255 or not self.name.strip()):
            raise ValidationError('The name cannot be empty or exceed 255 characters.')
        if self.country and (len(self.country) > 255 or not self.country.strip()):
            raise ValidationError('The country cannot be empty or exceed 255 characters.')

    @api.onchange('zip')
    def _onchange_numeric_values(self):
        if self.zip is not None and (not isinstance(self.zip, int) or len(str(self.zip)) > 10):
            self.zip = 0
            return {'warning': {'title': 'Invalid ZIP Code', 'message': 'ZIP Code must be a valid numeric value and less than 10 digits.'}}

    def copy(self, default=None):
        if default is None:
            default = {}

        # Agrega tu lógica personalizada antes de la copia
        default.update({
            'name': '',
            'phone': '',
            'zip': ''
        })

        return super(Supplier, self).copy(default)