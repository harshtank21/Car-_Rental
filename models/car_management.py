from odoo import models, fields, api


class Car_Management(models.Model):
    _name = "car.management"
    _description = "Car Rental"
    # _rec_name = "squ"

    name = fields.Char(string="Name", required=True)
    img = fields.Binary("img")
    avg = fields.Integer("Average")
    speed = fields.Integer("Speed")
    rent = fields.Integer("Rent")
    type = fields.Selection([("suv", "SUV"), ("hatchback", "Hatchback"), ("sedan", "Sedan"), ("minivan", "Minivan"),
                             ("convertible", "convertible"), ("Sports car", "Sports car"),("luxurious","Luxurious")], string="Type")
    squ = fields.Char(string="squ" ,readonly=True)


    @api.model
    def create(self, vals):
        vals['squ'] = self.env['ir.sequence'].next_by_code('my.sequence.code')
        return super(Car_Management, self).create(vals)
