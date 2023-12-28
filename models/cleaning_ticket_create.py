from odoo import models, fields, api


class CarBills(models.Model):
    _name = "cleaning.ticket.create"
    _description = "Car Rental"

    name = fields.Many2one("car.management", string="Name")
    phone = fields.Char(string="phone")
    type = fields.Selection([("car dry cleaning", "CAR DRY CLEANING"), ("CAR VACUUM cLEANING", "CAR VACUUM CLEANING"),
                             ("CAR wASHING", "CAR WASHING")], string="type")
    driver_name = fields.Many2one("driver.salary", string="driver_name")
    date = fields.Date(string="date")
    cost = fields.Integer(string="cost")
    washing = fields.Selection(
        [("gajanan_motors", "Gajanan Motors"), ("auto_club_car_dettling_studio", "Auto Club Car Dettling Studio"),
         ("steer_well_auto", "Steer Well Auto")],
        string="washing")

    def update_cleaning_maintenance(self):
        self.env["cleaning.maintenance"].create({
            "name": self.washing,
            "driver_name": self.driver_name.name,
            "washing": self.name.name,
            "date": self.date,
            "cost": self.cost,
            "phone": self.phone,
        })
