{
    'name': 'Real Estate Extended',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Extends Real Estate Advertisement and Services',
    'description': "",
    'website': 'http://www.odoo.com/real_estate_extend',
    'depends': [
        'real_estate'
    ],
    'data':[
       'security/ir.model.access.csv',
       'views/sez_property_views.xml',
       'views/special_offer_views.xml'

    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'


}
