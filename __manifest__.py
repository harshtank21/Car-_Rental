{
    "name": "Car Rental",
    'version': '16.0.1.0.0',
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
    'depends': ['base', 'mail', 'sale', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir_sequence_data.xml',
        'data/mail_template_data.xml',
        'report/sale_order_report.xml',
        'report/car_rental_order_report_template.xml',
        'report/car_rental_order_report_second_template.xml',
        'report/car_rental_order_report.xml',
        'views/menu_views.xml',
        'views/offline_transaction_views.xml',
        'views/online_transaction_views.xml',
        'views/all_order_views.xml',
        'views/avd_orders_views.xml',
        'views/running_order_views.xml',
        'views/driver_salary_views.xml',
        'views/customers_customers_views.xml',
        'views/cars_management_views.xml',
        'views/customer_invoices_views.xml',
        'views/cleaning_maintenance_views.xml',
        'views/cleaning_ticket_create_views.xml',
        'views/car_bills_views.xml',
        'views/finance_views.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
