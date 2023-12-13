from odoo import models,fields,api


class Customer_Invoices(models.Model):
    _name = "customer.invoices"
    _description = "Car Rental"



    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    star_date=fields.Date(string="Star Date")
    end_date=fields.Date(string="End Date")
    rent_time=fields.Char(string="Rent Time")
    licence = fields.Char(string="Licence",required=True)
    licence_attach = fields.Binary(string="Licence Attach",required=True)
    identity = fields.Selection([("identity","Identity"),("pancard","Pan card"),("voter id","Voter id")], required=True, string="Identity")
    Identity_img = fields.Binary(string="Identity Attach", required=True)