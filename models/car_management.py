from odoo import models,fields,api


class Car_Management(models.Model):
    _name = "car.management"
    _description ="Car Rental"

    name = fields.Char(string="Name", required=True)
    img = fields.Binary("  ")
    avg = fields.Integer("Average")
    speed = fields.Integer("Speed")
    rent = fields.Integer("Rent")
    type = fields.Selection([("suv","SUV"),("hatchback","Hatchback"),("sedan","Sedan") ,("minivan","Minivan"),("convertible","convertible"),("Sports car","Sports car")],string="Type")
    id = fields.Char("id")
