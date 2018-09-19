# A Test Task
# Started at 10 am Tuestday September 18 2018
{'name': 'delivery_schedule',
 'version': '0',
 'author': "Sadaf",
 'category': 'Delivery',
 'complexity': 'normal',
 'depends': ['order','delivery'],
 'data': [
     'views/schedule.xml',
     'views/stock.xml',
     'views/res_config.xml',
     'security/ir.model.access.csv',
     'wizard/manifest_wizard_view.xml',
 ],
 'installable': True,
 'auto_install': False,
 'license': 'AGPL-3',
 }
