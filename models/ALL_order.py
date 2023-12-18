from odoo import models,fields,api
from datetime import date


class New_Order(models.Model):
    _name = "all.order"
    _description = "Car Rental"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    star_date = fields.Date(string="Star Date")
    end_date = fields.Date(string="End Date")
    email = fields.Char(string="Email")
    phone = fields.Char(string="phone")
    # time = fields.time(hour=)
    driver=fields.Selection([("with driver","With Driver",),("without driver ","Without Driver")] , string="driver")
    rent = fields.Integer(string="Rent")
    status=fields.Char(string="Status",compute="_compute_your_status")
    cars=fields.Many2one("car.management",string="Cars")




    #
    def _compute_your_status(self):
        for rec in self:
            today= date.today()
            if(rec.end_date < today):
                rec.status = "COMPLETE"
            else:
                rec.status ="ORDER RUNNING"
