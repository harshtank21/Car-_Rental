from odoo import models, fields, api
from datetime import date

class Offline_Transaction(models.Model):
    _name = "offline.transaction"
    _description = "Car Rental"



    name=fields.Char("Name",compute="_compute_name")
    month=fields.Integer("Month",compute="_compute_month")
    day=fields.Char("Day")
    year=fields.Char("Year")

    # date=fields.date("Date")

    def _compute_name(self):
        for rec in self:
            rec.name=" Hertz Global "

    def _compute_month(self):
        reco=self.env["customer.invoices"].search([("star_date","in","month=12")])
        for i in reco:
            self.month=self.month + 1