from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrderWizad(models.TransientModel):
    _name = 'customer.wizard'
    customer = fields.Many2one('customer.customer', string="customer", required=True)
    address = fields.Char(string="Address", required=True)
    licence = fields.Char(string="Licence", required=True)
    force_fully = fields.Boolean(string="force_fully")

    @api.onchange('customer')
    def onchange_customer(self):
        self.address = self.customer.address
        self.licence = self.customer.licence

    def assigning_cars(self):
        context = self.env.context.get('active_ids')
        customer = self.env["customer.customer"].search([])
        store = []
        old_order = []
        for rec in customer:
            car_id = list(res.id for res in rec.cars_name_ids)
            cars = list(car for car in context if car in car_id)
            if not cars:
                store.extend(cars)
            else:
                old_order.append(rec.id)
                store.extend(cars)

        if store == []:
            self.customer.update({
                'cars_name_ids': [(fields.Command.set(context))]
            })
        else:
            return {
                'name': 'Warning',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                "view_type": "form",
                'res_model': 'warning.wizard',
                'target': 'new',
                'view_id': self.env.ref
                ('car_Rental.warning_wizard_form_view').id,
                'context': {'active_id': self.id,
                            'code_match': context,
                            'customer': self.customer.id,
                            'old_order': old_order,
                            'store' : store},
            }
