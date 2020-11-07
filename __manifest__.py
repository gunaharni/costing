{
    'name': 'Costing',
    'version': '13.0.1.0',
    'category': 'Tools',
    'author': 'Odoo Mates',
    'website': 'odoomates.com',
    'license': 'AGPL-3',
    'summary': 'Costing app',
    'description': """Module to manage costing""",
    'depends': ['base', 'mail','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/types.xml',
        'views/cost.xml',
        'views/menu.xml',
        'views/stages.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False

}