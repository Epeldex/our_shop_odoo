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
             'views/product.xml',
             'views/tag.xml',
             'views/supplier_view.xml',
             'views/product_view.xml',
             'views/tag_view.xml'
             ],
    'icon' : '/shop/static/description/icon.png',
    'license': 'LGPL-3',
}
