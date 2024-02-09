from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


#
# class Covid(http.Controller):
#     @http.route('/shop', website=True, auth='public')
#     def covid(self, **kw):
#         is_covid = request.env['ir.config_parameter'].get_param('car_Rental.is_covid')
#
#         print("======================\n\n\n\n\n\n\n\n\n\n\n",is_covid)
#         # return request.render("car_rental.contacts_res_partner_warning", {
#         #     'covid': is_covid
#         # })
class WebsiteSaleInherit(WebsiteSale):
    def _get_additional_shop_values(self, values):
        super()._get_additional_shop_values(values)
        is_covid = request.env['ir.config_parameter'].get_param('car_Rental.is_covid')
        if is_covid == str(True):
            return {"code": bool(is_covid)}
        else:
            return {'code': bool(is_covid)}

    def _prepare_product_values(self, product, category, search, **kwargs):
        res = super(WebsiteSaleInherit, self)._prepare_product_values(product, category, search, **kwargs)
        is_covid = request.env['ir.config_parameter'].get_param('car_Rental.is_covid')
        if is_covid == "True":
            res['code'] = False
        else:
            res['code'] = True
        return res

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0,
                                                   ppg=False, **post)
        return res
