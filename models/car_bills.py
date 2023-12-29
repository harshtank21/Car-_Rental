from odoo import models, fields, api
from datetime import date, datetime


class CarBills(models.Model):
    _name = "car.bills"
    _description = "Car Rental"

    name = fields.Selection(
        [("gajanan_motors", "Gajanan Motors"), ("auto_club_car_dettling_studio", "Auto Club Car Dettling Studio"),
         ("steer_well_auto", "Steer Well Auto")], string="NAME")
    count = fields.Integer(string="Count ")
    total_pay_this_month = fields.Integer(string="TOTAL PAY THIS MONTH ")
    month = fields.Selection(
        [("1", "January"),
         ("2", "February"),
         ("3", "March"),
         ("4", "April"),
         ("5", "May"),
         ("6", "June"),
         ("7", "July"),
         ("8", "August"),
         ("9", "September"),
         ("10", "October"),
         ("11", "November"),
         ("12", "December")])
    last_entry = fields.Date(string="LAST ENTRY DATE", default=datetime.now())

    @api.onchange("month", "name")
    def onchange_month(self):
        reco = self.env["cleaning.maintenance"].search([("theday", "=", self.month), ("name", "=", self.name)])
        self.count = self.env["cleaning.maintenance"].search_count(
            [("theday", "=", self.month), ("name", "=", self.name)])
        month_world = 0

        if self.month:
            for rec in reco:
                month_world = month_world + rec.cost
            self.total_pay_this_month = month_world
