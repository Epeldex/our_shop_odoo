from odoo import api, fields, models

class user(models.Model):
    _name = 'our-shop.user'
    _description = 'User class'

    user_id = fields.Integer(string='User ID', readonly=True)
    username = fields.Text(string='Username')
    password = fields.Text(string='Password')
    active = fields.Boolean(string="Active")
    