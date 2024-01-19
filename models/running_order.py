from odoo import models,fields,api
from datetime import date


class RunningOrder(models.Model):
    _name = "running.order"
    _description = "Car Rental"

    name = fields.Many2one("customer.customer",string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    star_date = fields.Date(string="Star Date")
    end_date = fields.Date(string="End Date")
    email = fields.Char(string="Email")
    phone = fields.Char(string="phone")
    # time = fields.time(hour=)
    driver=fields.Selection([("with driver","With Driver",),("without driver ","Without Driver")] , string="driver")
    rent = fields.Integer(string="Rent")
    cars=fields.Many2one("car.management",string="Cars")





