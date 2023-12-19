from odoo import models, fields

class Tag(models.Model):
    _name = 'your_module.tag'
    _description = 'Tag Model'

    tag_id = fields.Integer(string='Tag ID')
    type = fields.Char(string='Type')
    label = fields.Char(string='Label')
    active = fields.Boolean(string='Active')
    create_timestamp = fields.Datetime(string='Create Timestamp')