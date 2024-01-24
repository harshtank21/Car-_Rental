from odoo import api, fields, models


class SaleOrderWizad(models.TransientModel):
    _name = 'customer.wizard'
    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    star_date = fields.Date(string="Star Date")
    end_date = fields.Date(string="End Date")
    email = fields.Char(string="Email")
    company_img = fields.Binary("img")
    phone = fields.Char(string="phone")
    licence = fields.Char(string="Licence", required=True)
    licence_attach = fields.Binary(string="Licence Attach")
    identity = fields.Selection([("identity", "Identity"),
                                 ("pancard", "Pan card"),
                                 ("voter id", "Voter id")],
                                required=True, string="Identity")
    compny = fields.Char(string="namec")
    Identity_img = fields.Binary(string="Identity Attach")
    squ = fields.Char(string="squ", readonly=True)
    exm = fields.Char(string="exm")
    car_booking = fields.Many2one("car.management", string="Cars")
    rent = fields.Integer(string="Rent", related="car_booking.rent")
    welcome_note = fields.Char("w")
    driver = fields.Boolean("DRIVER")
    driver_name = fields.Many2one("driver.salary", "DRIVER NAME")


    def leave_filter_act(self):
        action=self.env.ref("car_Rental.customer_wizard_action_window")
        return action