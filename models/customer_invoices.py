from odoo import models, fields, api
from datetime import date


class CustomerInvoices(models.Model):
    _name = "customer.invoices"
    _description = "Car Rental"

    name = fields.Char(string="Name", required=True)
    # GST_ID = fields.Char(string="GST_No ", releted="5442GFT29NE")
    ret = fields.Many2one("customer.customer", "ret")
    address = fields.Char(string="Address", required=True)
    star_date = fields.Date(string="Star Date")
    end_date = fields.Date(string="End Date")
    rent_time = fields.Integer(string="Rent Time", compute="_compute_rent_time", )
    rent = fields.Integer(string="Rant")
    # rent_time=fields.Integer(string="Rent Time")
    phone = fields.Char(string="phone")
    licence = fields.Char(string="Licence", required=True)
    licence_attach = fields.Binary(string="Licence Attach")
    identity = fields.Selection([("identity", "Identity"), ("pancard", "Pan card"), ("voter id", "Voter id")],
                                required=True, string="Identity")
    Identity_img = fields.Binary(string="Identity Attach")
    yourbill = fields.Integer(string="You Payable Amount", compute="_compute_your_bills", )
    gst = fields.Integer(string="gst", compute="_compute_your_gst", )
    # total = fields.Integer(string="TOTAL BILL", compute="_compute_your_total")
    total = fields.Integer(string="TOTAL BILL", compute="_compute_your_driver")
    pythment = fields.Selection([("online", "Online"), ("offline", "Offline")])
    adev = fields.Many2one("all.order", string="Done")
    indriver = fields.Boolean(string="driver")
    driver = fields.Integer(string="indriveer", )
    theday = fields.Integer(string="Date", compute="_compute_date", store=True)

    # @api.depends("end_date")
    def _compute_rent_time(self):
        for rec in self:
            if rec.end_date:
                rec.rent_time = rec.end_date.day - rec.star_date.day

    @api.depends("end_date")
    def _compute_date(self):
        for rec in self:
            if rec.end_date:
                rec.theday = rec.end_date.month

    # @api.depends("rent_time")
    def _compute_your_bills(self):
        for rec in self:
            rec.yourbill = rec.rent * rec.rent_time

    def _compute_your_gst(self):
        for rec in self:
            rec.gst = (rec.yourbill * 18) / 100

    # @api.onchange("indriver")
    # def onchange_your_driver(self):
    def _compute_your_driver(self):
        for selff in self:
            if (selff.indriver == True):
                selff.driver = selff.rent_time * 1000
                selff.total = selff.yourbill + selff.gst + selff.driver
            else:
                # self.driver = 0
                selff.total = selff.yourbill + selff.gst + selff.driver

    @api.model
    def create(self, v):

        print("beforeeeee vvvvvvvvvvvvvvvvvvvvv-------------------->",v)
        print("self------------------------------------>",self)
        ret = super(CustomerInvoices,self).create(v)
        v['indriver'] = True
        print("afterr---------------->",v)
        print("--------------------------->",ret)
        return ret

        # def _compute_your_total(self):
        #     for rec in self:
        #         rec.total = rec.yourbill + rec.gst + rec.driver

    # @api.onchange("name")
    # def onchange_your_driver(self):
    #     to=date
