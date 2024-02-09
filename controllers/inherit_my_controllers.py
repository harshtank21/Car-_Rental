from odoo import http
from .main import Cars
from odoo.http import request


class CarsInherit(Cars):
    def _get_additional_car_values(self, values):
        customer = request.env['customer.customer'].sudo().search([],limit=14)
        return {
            "customer": 'RAJU BHAI'

        }

    @http.route('/cars', website=True, auth='public')
    def cars(self, **kw):
        res = super(CarsInherit, self).cars(**kw)
        print(res, "kkkkkkkkkkkkkkkkkkkkkk")
        return res
