from odoo import models, fields, api
from datetime import date, datetime


class Advancorder(models.Model):
    _name = "advanc.order"
    _description = "Car Rental"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    star_date = fields.Date(string="Star Date")
    end_date = fields.Date(string="End Date")
    email = fields.Char(string="Email")
    phone = fields.Char(string="phone")
    # time = fields.time(hour=)
    driver = fields.Selection([("with driver", "With Driver",), ("without driver ", "Without Driver")], string="driver")
    rent = fields.Integer(string="Rent")
    cars = fields.Many2one("car.management", string="Cars")

    def refresh_avd_oder(self):
        recode = self.search([("star_date", "<=", date.today())])
        print("--------------------->",recode)
        for rec in recode:
            rec.unlink()

    def unlink(self):
        print("---------------------------------------------------->")
        # print(super(Advancorder, self).unlink())
        self.env["running.order"].create({
            "name": self.name,
            "address": self.address,
            "star_date": self.star_date,
            "rent": self.rent,
            "end_date": self.end_date,
            "phone": self.phone,
            "email": self.email
        })
        new= super(Advancorder, self).unlink()
        print(new)
        return new

