from odoo import models, fields, api


class DriverSalary(models.Model):
    _name = "driver.salary"
    _description = "Car Rental"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="phone")
    salary = fields.Integer(string="Salary")
    licence = fields.Char(string="Licence", required=True)
    car_name = fields.Many2many(comodel_name='car.management', string="Car Name")

    def write(self, vals):
        res = super(DriverSalary, self).write(vals)
        record = self.search([])
        for rec in record:
            if rec.id != self.id:
                if self.car_name in rec.car_name :
                    print(self.car_name,rec.car_name)
        return res
