from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


# class WebsiteSaleInherit(WebsiteSale):
#     @http.route([
#         '/shop',
#         '/shop/page/<int:page>',
#         '/shop/category/<model("product.public.category"):category>',
#         '/shop/category/<model("product.public.category"):category>/page/<int:page>',
#     ], type='http', auth="public", website=True)
#     def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
#         res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0,
#                                                    ppg=False, **post)
#
#
#         return res

# def _get_additional_shop_values(self, values):
#     res = super()._get_additional_shop_values(values)
#     values["to_one"] = 21
#     return values


class Cars(http.Controller):
    @http.route('/car_Rental/cars', website=True, auth='public')
    def cars(self, page=0, **kw):
        cars = request.env['car.management'].sudo().search([('type', '=', 'hatchback')], limit=3)
        customer = request.env['customer.customer'].sudo().search([])
        return request.render("car_Rental.cars", {
            'cars': cars,
            'customer': customer
        })


class Contacts(http.Controller):
    @http.route(['/contact', '/contact/<int:page>'], website=True, auth='public')
    def contacts(self, page=0, **kw):
        contact = request.env['res.partner'].search([])
        total = len(contact)
        par_page = 10
        pager = request.website.pager(
            url="/contact",
            url_args=None,
            total=total,
            page=page,
            scope=2,
            step=par_page)
        contact = request.env['res.partner'].sudo().search([], limit=par_page, offset=pager['offset'])
        return request.render("car_Rental.contacts_res_partner", {
            'contact': contact,
            'pager': pager
        })

    @http.route('/contact/details/<int:id>', website=True, auth='public')
    def contacts_details(self, id=None, **kw):
        details = request.env['res.partner'].sudo().browse([id])
        return request.render("car_Rental.contacts_res_partner_details", {
            'contact_id': details,
        })
    # @http.route('/contact/details/<int:page>', website=True, auth='public')
    # def contacts_details(self, page=0, **kw):
    #     contact = request.env['res.partner'].search([])
    #     total = len(contact)
    #     par_page = 10
    #     pager = request.website.pager(
    #         url="/my/leads",
    #         url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
    #         total=total,
    #         page=page,
    #         step=par_page
    #     )
    #     return request.render("car_Rental.contacts_res_partner_details", {
    #         'contact_id': details
    #     })
