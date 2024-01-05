from odoo import models, fields, api
from datetime import date


class OfflineTransaction(models.Model):
    _name = "offline.transaction"
    _description = "Car Rental"

    name = fields.Char("Name", compute="_compute_name")
    month_income = fields.Integer("Month income")
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

    date = fields.Date(month="Date")

    def _compute_name(self):
        self.name = " Hertz Global "

    @api.onchange("month")
    def onchange_month_to_monthincome(self):
        reco = self.env["customer.invoices"].search([("theday", "=", self.month)])
        month_world = 0
        for rec in reco:
            if (rec.pythment == "offline"):
                month_world = month_world + rec.total
        self.month_income = month_world
