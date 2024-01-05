from odoo import models, fields, api
from datetime import date


class Finance(models.Model):
    _name = "finance.finance"
    _description = "Car Rental"
    name = fields.Char("Name", compute="_compute_name")
    month_income = fields.Integer("Month income")
    online_income = fields.Integer("Online income")
    offline_income = fields.Integer("Offline income")
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
    # date = fields.Date(month="Date")
    car_bills_gajanan_motor = fields.Integer(string="Car Bills Gajanan Motor")
    car_bills_steer_well_auto_ = fields.Integer(string="Car Bills Steer Well Auto")
    car_bills_auto_club_car_dettling_studios = fields.Integer(string="Car Bills Auto Club")
    date = fields.Date(string="Date", compute="_compute_date_one")
    date_one = fields.Char(string="Date", compute="_compute_date")

    def _compute_date_one(self):
        self.date = date.today()

    def _compute_name(self):
        self.name = "Hertz Global Pvt.Ltd"

    @api.depends("date")
    def _compute_date(self):
        for rec in self:
            if rec.date:
                rec.date_one = rec.date.strftime('%B %d, %Y')

    @api.onchange("month")
    def total_month_account(self):
        all_bills = self.env["cleaning.maintenance"].search(
            [("theday", "=", self.month)])
        for rec in all_bills:
            if rec.name == "gajanan_motors":
                self.car_bills_gajanan_motor += rec.cost
            elif rec.name == "auto_club_car_dettling_studio":
                self.car_bills_auto_club_car_dettling_studios += rec.cost
            elif rec.name == "steer_well_auto":
                self.car_bills_steer_well_auto_ += rec.cost

        payment = self.env["customer.invoices"].search([("theday", "=", self.month)])
        for record in payment:
            if record.pythment == "offline":
                self.offline_income += record.total
            elif record.pythment == "online":
                self.online_income += record.total

        self.month_income = (self.online_income + self.offline_income) - (
                self.car_bills_gajanan_motor + self.car_bills_auto_club_car_dettling_studios + self.car_bills_steer_well_auto_)
