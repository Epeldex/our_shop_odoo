from odoo import api, fields, models


class Admin(models.Model):
    
    _name = 'shop.admin'
    _description = 'Admin class'
    _inherit = 'shop.user'

    last_access = fields.Date(string='Last access date')