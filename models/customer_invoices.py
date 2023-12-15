from odoo import models, fields, api
from datetime import date

class Customer_Invoices(models.Model):
    _name = "customer.invoices"
    _description = "Car Rental"



    name = fields.Char(string="Name", required=True)
    GST_ID = fields.Char(string="GST_No ", releted="5442GFT29NE")
    ret = fields.Many2one("customer", "ret")
    address = fields.Char(string="Address", required=True)
    star_date = fields.Date(string="Star Date")
    end_date = fields.Date(string="End Date")
    rent_time = fields.Integer(string="Rent Time", compute="_compute_rent_time")
    rent = fields.Integer(string="Rant")
    # rent_time=fields.Integer(string="Rent Time")
    phone = fields.Char(string="phone")
    licence = fields.Char(string="Licence", required=True)
    licence_attach = fields.Binary(string="Licence Attach")
    identity = fields.Selection([("identity", "Identity"), ("pancard", "Pan card"), ("voter id", "Voter id")],
                                required=True, string="Identity")
    Identity_img = fields.Binary(string="Identity Attach")
    yourbill = fields.Integer(string="You Payable Amount", compute="_compute_your_bills")
    gst = fields.Integer(string="gst", compute="_compute_your_gst")
    # total = fields.Integer(string="TOTAL BILL", compute="_compute_your_total")
    total = fields.Integer(string="TOTAL BILL")
    adv = fields.Boolean(string="pay ment Done")
    adev = fields.Many2one("new.order", string="Done")
    indriver = fields.Boolean(string="driver")
    driver = fields.Integer(string="indriveer")
    thatday= fields.date(string="Date")
    def _compute_rent_time(self):
        for rec in self:
            if rec.end_date:
                rec.rent_time = rec.end_date.day - rec.star_date.day

    def _compute_your_bills(self):
        for rec in self:
            rec.yourbill = rec.rent * rec.rent_time

    def _compute_your_gst(self):
        for rec in self:
            rec.gst = (rec.yourbill * 18) / 100

    @api.onchange("indriver")
    def onchange_your_driver(self):
        print(self.indriver)
        if (self.indriver == True):
            self.driver = self.rent_time * 1000
            self.total = self.yourbill + self.gst + self.driver
        else:
            self.driver = 0
            self.total = self.yourbill + self.gst + self.driver

        # def _compute_your_total(self):
        #     for rec in self:
        #         rec.total = rec.yourbill + rec.gst + rec.driver

    @api.onchange("name")
    def onchange_your_driver(self):
        to=date 



