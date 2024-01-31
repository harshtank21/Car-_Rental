from odoo import http
from odoo.http import request


class Cars(http.Controller):
    @http.route('/car_Rental/cars', website=True, auth='public')
    def cars(self, **kw):
        print(request)
        cars = request.env['car.management'].sudo().search([])
        return request.render("car_Rental.cars", {
            'cars': cars
        })


class Contacts(http.Controller):
    @http.route('/contact', website=True, auth='public')
    def contacts(self, **kw):
        contact = request.env['res.partner'].sudo().search([])
        print(contact)
        return request.render("car_Rental.contacts_res_partner", {
            'contact': contact
        })
