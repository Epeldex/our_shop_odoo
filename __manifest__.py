# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Our Shop',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 9001,
    'description': """
This module allows to manage onboardings and their progress
================================================================================
    """,
    'depends': ['base'],
    'installable': True,
    'data': [
        'security/our_shop_security.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'LGPL-3',
}
