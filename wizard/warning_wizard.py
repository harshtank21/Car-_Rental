from odoo import api, fields, models


class SaleOrderWizad(models.TransientModel):
    _name = 'warning.wizard'

    warning = fields.Char(
        string="Warning"
    )

    def force_fully_assign(self):
        context = self.env.context
        customer_id = context.get('customer')
        cars_id = context.get('code_match')
        old_order_context = context.get('old_order')
        store = context.get('store')
        customer = self.env["customer.customer"].browse(int(customer_id))
        customer.update({
            'cars_name_ids': [(fields.Command.set(cars_id))]
        })
        for rec in store:
            for order in old_order_context:
                order_old = self.env["customer.customer"].browse(int(order))
                order_old.update({
                    'cars_name_ids': [(fields.Command.unlink(rec))]
                })

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        defaults['warning'] = "This car has been given to someone else"
        return defaults
