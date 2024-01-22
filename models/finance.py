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
    car_maintenance = fields.Integer(string="Car Maintenance")
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
            [("the_day", "=", self.month)])
        for rec in all_bills:
            self.car_maintenance += rec.cost

        payment = self.env["customer.invoices"].search([("the_day", "=", self.month)])
        for record in payment:
            if record.payment == "offline":
                self.offline_income += record.total
            elif record.payment == "online":
                self.online_income += record.total

        self.month_income = (self.online_income + self.offline_income) - (self.car_maintenance)
