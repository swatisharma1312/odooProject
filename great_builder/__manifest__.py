{
    'name': "Builder Management",

    'category': 'Sales/Sales',

    'sequence': 5,

    'summary': "builder management",

    'description': """Builder Management""",

    'author': "Swati Sharma",

    'version': '1.0',

    'depends': ['base', 'mail', 'sale', 'purchase', 'account', 'product'],

    'data': [
        'security/product.xml',
        'security/ir.model.access.csv',
        'views/product_update.xml',
    ],

    'application': True,
}