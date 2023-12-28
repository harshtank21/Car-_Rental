{
    "name" : "Car Rental",
    'version' : '16.0.1.0.0',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
School Management 
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends' : ['base'],
    'data': [
        'views/menu_views.xml',
        'security/ir.model.access.csv',
        'views/offline_transaction_views.xml',
        'views/online_transaction_views.xml',
        'views/All_order_views.xml',
        'views/avd_orders_views.xml',
        'views/running_order_views.xml',
        'views/drver_salary_views.xml',
        'views/customers_customers_views.xml',
        'views/cars_management_views.xml',
        'views/customer_incoices_views.xml',
        'views/cleaning_maintenance_views.xml',
        'views/cleaning_ticket_create_views.xml',
        'views/car_bills_views.xml',
        'data/ir_sequence_data.xml'





    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
