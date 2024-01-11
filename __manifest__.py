{
    'name': 'Our shop',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 9001,
    'description': """
This module allows to manage onboardings and their progress
================================================================================
    """,
    'depends': ['base'],
    'installable': True,
    'data': ['security/our_shop_security.xml',
             'security/ir.model.access.csv',
             'views/views.xml',
             'views/supplier.xml',
             'views/supplier_view.xml'],
    'license': 'LGPL-3',
}
