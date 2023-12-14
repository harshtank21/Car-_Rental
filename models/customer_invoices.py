from odoo import models,fields,api


class Customer_Invoices(models.Model):
    _name = "customer.invoices"
    _description = "Car Rental"



    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    star_date=fields.Date(string="Star Date")
    end_date=fields.Date(string="End Date")
    rent_time=fields.Integer(string="Rent Time",compute="compute_rent_time",stor=True)
    rent = fields.Integer(string="Rant")
    # rent_time=fields.Integer(string="Rent Time")
    licence = fields.Char(string="Licence",required=True)
    licence_attach = fields.Binary(string="Licence Attach")
    identity = fields.Selection([("identity","Identity"),("pancard","Pan card"),("voter id","Voter id")], required=True, string="Identity")
    Identity_img = fields.Binary(string="Identity Attach")
    gst=fields.Integer(string="gst")
    yourbill=fields.Integer(string="You Payable Amount")
    adv=fields.Boolean(string="pay ment Done")



    def compute_rent_time(self):
        for rec in self:
            if rec.end_date:
                rec.rent_time=rec.end_date.day - rec.star_date.day

    @api.onchange('yourbill')
    def _onchange_phone_validation(self):
        for rec in self:
            rec.yourbill = rec.rent * rec.rent_time

