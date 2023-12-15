from odoo import models,fields,api


class Driver_Salary(models.Model):
    _name = "driver.salary"
    _description = "Car Rental"

    name = fields.Char(string="Name", required=True)
    email=fields.Char(string="Email")
    phone=fields.Char(string="phone")
    salary = fields.Integer(string="Salary")
    licence = fields.Char(string="Licence",required=True)


