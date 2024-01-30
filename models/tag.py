from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class Tag(models.Model):
    _name = 'shop.tag'
    _description = 'Tag Model'

    tag_id = fields.Integer(string='Tag ID')
    type = fields.Char(string='Type')
    label = fields.Char(string='Label')
    active = fields.Boolean(string='Active')
    create_timestamp = fields.Datetime(string='Create Timestamp')
    tag_products = fields.One2many(comodel_name='shop.product', inverse_name='product_id', string='Products')
    image = fields.Binary(string='Image URL', help='URL to the custom image for the tag')
    
     # Override Copy Method
    def copy(self, default=None):
        default = dict(default or {})
        # Modify a specific field, e.g., product_number
        modified_tag_type = self.type + "_copy"  # This is an example
        default['type'] = modified_tag_type
        return super(Tag, self).copy(default)
    
    
    # Validations for every field    
    @api.constrains('label')
    def check_label_is_filled(self):
        for record in self:
            if not record.label:
                raise ValidationError("Label cannot be empty")
            
    @api.constrains('type')
    def check_type_is_filled(self):
        for record in self:
            if not record.type:
                raise ValidationError("Type cannot be empty")

                
    @api.constrains('create_timestamp')
    def check_valid_date(self):
        for record in self:
            if record.create_timestamp:
                today = fields.Date.today()
                # Convert the string to a date object
                record_date = fields.Date.from_string(record.create_timestamp)
                if record_date >= today:
                    raise models.ValidationError("The 'Create Timestamp' must be a date before the present.")

    @api.onchange('type')
    def verify_type_length(self):
        if self.type:
            length = len(self.type)
            if (255 < length):
                return {
                    'warning': {
                        'title': "Incorrect 'Type' value",
                        'message': "Type field can't be longer than 255 characters.",
                    },
                }
                
    @api.onchange('label')
    def verify_label_length(self):
        if self.label:
            length = len(self.label)
            if (255 < length):
                return {
                    'warning': {
                        'title': "Incorrect 'Label' value",
                        'message': "Label field can't be longer than 255 characters.",
                    },
                }
            
       
    