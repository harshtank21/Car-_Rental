from odoo import models, fields, api
from datetime import date, datetime


class CustomerInvoices(models.Model):
    _name = "customer.invoices"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Car Rental"

    name = fields.Many2one("customer.customer", string="Name", required=True)
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
    your_bill = fields.Integer(string="You Payable Amount", compute="_compute_your_bills")
    gst = fields.Integer(string="gst", compute="_compute_your_gst", )
    # total = fields.Integer(string="TOTAL BILL", compute="_compute_your_total")
    total = fields.Integer(string="TOTAL BILL", compute="_compute_your_driver", tracking=True, store=True)
    payment = fields.Selection([("online", "Online"), ("offline", "Offline")])
    car_ids = fields.One2many(comodel_name="car.management", inverse_name="invoice_id", string=" car")
    in_driver = fields.Boolean(string="driver")
    driver = fields.Integer(string="indriveer", )
    driver_name = fields.Many2one("driver.salary",string="Driver Name", )
    the_day = fields.Integer(string="Date", compute="_compute_date", store=True)

    # @api.depends("end_date")
    def _compute_rent_time(self):
        for rec in self:
            if rec.end_date:
                rec.rent_time = rec.end_date.day - rec.star_date.day

    @api.depends("end_date")
    def _compute_date(self):
        for rec in self:
            if rec.end_date:
                rec.the_day = rec.end_date.month

    # @api.depends("rent_time")
    def _compute_your_bills(self):
        for rec in self:
            rec.your_bill = rec.rent * rec.rent_time

    def _compute_your_gst(self):
        for rec in self:
            rec.gst = (rec.your_bill * 18) / 100


    # @api.onchange("in_driver")
    # def onchange_your_driver(self):
    @api.depends("in_driver")
    def _compute_your_driver(self):
        for selff in self:
            if (selff.in_driver == True):
                selff.driver = selff.rent_time * 1000
                selff.total = selff.your_bill + selff.gst + selff.driver
            else:
                selff.driver = 0
                selff.total = selff.your_bill + selff.gst + selff.driver

    @api.model
    def create(self, v):
        ret = super(CustomerInvoices, self).create(v)
        v['in_driver'] = True
        return ret

    def send_massages(self):
        self.message_post(body="Hello Good Morning!")

    def send_email(self):
        customer = self.search([])
        today = date.today()
        for rec in customer:
            remainder_template = rec.env.ref("car_Rental.email_rental_sale")
            provide_the_bill_template = rec.env.ref("car_Rental.email_rental_sale_provide_the_bill")
            remainder_date = (rec.end_date - today).days
            if remainder_date == -1:
                provide_the_bill_template.send_mail(rec.id, force_send=True, raise_exception=False)
            elif remainder_date == 1:
                remainder_template.send_mail(rec.id, force_send=True, raise_exception=False)

    def driver_true(self):
        self.in_driver = True
