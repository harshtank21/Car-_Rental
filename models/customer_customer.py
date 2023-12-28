from odoo import models, fields, api
from datetime import date


class CustomerCustomer(models.Model):
    _name = "customer.customer"
    _description = "Car Rental"
    _rec_name = "squ"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    star_date = fields.Date(string="Star Date")
    end_date = fields.Date(string="End Date")
    email = fields.Char(string="Email")
    company_img = fields.Binary("img")
    phone = fields.Char(string="phone")
    licence = fields.Char(string="Licence", required=True)
    licence_attach = fields.Binary(string="Licence Attach")
    identity = fields.Selection([("identity", "Identity"),
                                 ("pancard", "Pan card"),
                                 ("voter id", "Voter id")],
                                required=True, string="Identity")
    compny = fields.Char(string="namec")
    Identity_img = fields.Binary(string="Identity Attach")
    squ = fields.Char(string="squ", readonly=True)
    exm = fields.Char(string="exm")
    car_booking = fields.Many2one("car.management", string="Cars")
    rent = fields.Integer(string="Rent", related="car_booking.rent")
    welcome_note = fields.Char("w")
    driver = fields.Boolean("DRIVER")
    driver_name = fields.Many2one("driver.salary","DRIVER NAME")

    def update_customer_invoices(self):
        self.env["customer.invoices"].create({
            "name": self.name,
            "address": self.address,
            "star_date": self.star_date,
            "rent": self.rent,
            "end_date": self.end_date,
            "licence": self.licence,
            "licence_attach": self.licence_attach,
            "identity": self.identity,
            "Identity_img": self.Identity_img,
            "phone": self.phone,
        })

    def update_order(self):
        today = date.today()
        if (self.star_date >= today):
            self.env["all.order"].create({
                "name": self.name,
                "address": self.address,
                "star_date": self.star_date,
                "rent": self.rent,
                "end_date": self.end_date,
                "phone": self.phone,
                "email": self.email
            })
            self.env["advanc.order"].create({
                "name": self.name,
                "address": self.address,
                "star_date": self.star_date,
                "rent": self.rent,
                "end_date": self.end_date,
                "phone": self.phone,
                "email": self.email
            })
        elif (self.star_date < today and self.end_date > today):
            self.env["all.order"].create({
                "name": self.name,
                "address": self.address,
                "star_date": self.star_date,
                "rent": self.rent,
                "end_date": self.end_date,
                "phone": self.phone,
                "email": self.email
            })
            self.env["running.order"].create({
                "name": self.name,
                "address": self.address,
                "star_date": self.star_date,
                "rent": self.rent,
                "end_date": self.end_date,
                "phone": self.phone,
                "email": self.email
            })

    @api.model
    def create(self, vals):
        vals['squ'] = self.env['ir.sequence'].next_by_code('my.sequence')
        vals['compny'] = "Hertz Global Pvt.Ltd"
        return super(CustomerCustomer, self).create(vals)

    def write(self, vals):
        vals['compny'] = "Hertz Global Pvt.Ltd"
        # x=self.env["car.management"].read_group([],["speed"],["speed"])
        x = self.env["car.management"].search_read([("type", "=", "suv")], fields=['name', "speed"])
        print(x)
        return super(CustomerCustomer, self).write(vals)

        # def try_button(self):
        #     partners = self.env['res.partner'].search([]).read(['name', 'phone'])
        #     print("\n\n\nn partners", partners)

        # def default_get(self):

    @api.model
    def default_get(self, fields):
        # print(fields)
        res = super(CustomerCustomer, self).default_get(fields)
        # print(res)
        # if res.get('model'):
        #     res['model_id'] = self.env['ir.model']._get(res.pop('model')).id
        res['welcome_note'] = "Welcome to Hertz Global Pvt.Ltd"
        # print(res)

        return res
