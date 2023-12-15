from odoo import models, fields, api
from datetime import date


class Customer(models.Model):
    _name = "customer"
    _description = "Car Rental"
    _rec_name = "squ"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    star_date = fields.Date(string="Star Date")
    end_date = fields.Date(string="End Date")
    email = fields.Char(string="Email")
    phone = fields.Char(string="phone")
    licence = fields.Char(string="Licence", required=True)
    licence_attach = fields.Binary(string="Licence Attach")
    identity = fields.Selection([("identity", "Identity"), ("pancard", "Pan card"), ("voter id", "Voter id")],
                                required=True, string="Identity")
    Identity_img = fields.Binary(string="Identity Attach")
    squ = fields.Char(string="squ", readonly=True)
    car_booking = fields.Many2one("car.management", string="Cars")
    rent = fields.Integer(string="Rent", related="car_booking.rent")

    def update_customer_invoices(self):
        self.env["customer.invoices"].create({
            "name": self.name,
            "address": self.address,
            "star_date": self.star_date,
            "rent": self.rent,
            "end_date": self.end_date,
            "licence": self.licence,
            "licence_attach": self.licence_attach,
            "identity": self.identity,
            "Identity_img": self.Identity_img,
            "phone": self.phone,
        })

    def update_order(self):
        self.env["new.order"].create({
            "name": self.name,
            "address": self.address,
            "star_date": self.star_date,
            "rent": self.rent,
            "end_date": self.end_date,
            "phone": self.phone,
            "email": self.email
        })

    @api.model
    def create(self, vals):
        vals['squ'] = self.env['ir.sequence'].next_by_code('my.sequence')
        return super(Customer, self).create(vals)
