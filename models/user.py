from odoo import api, fields, models

class user(models.Model):
    _name = 'our-shop.user'
    _description = 'User class'

    user_id = fields.Integer(string = 'user_id')