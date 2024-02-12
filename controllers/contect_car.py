from odoo import http
from odoo.http import request


class CarsWeb(http.Controller):
    @http.route('/cars/contect', website=True, auth='public')
    def cars(self, **kw):
        cars = request.env['car.management'].sudo().search([])
        values = {
            'cars': cars,
        }
        return request.render("car_Rental.cars_contect_page", values)