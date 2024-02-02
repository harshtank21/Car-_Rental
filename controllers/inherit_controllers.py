from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class Cars(WebsiteSale):
    @http.route('/car_Rental/cars', website=True, auth='public')
    def cars(self, **kw):
        cars = request.env['car.management'].sudo().search([])
        return request.render("car_Rental.cars", {
            'cars': cars
        })