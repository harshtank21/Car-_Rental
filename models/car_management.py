from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CarManagement(models.Model):
    _name = "car.management"
    _description = "Car Rental"
    # _rec_name = "speed"
    name = fields.Char(string="Name", required=True)
    rental_name_one = fields.Char(string="Rental name")
    img = fields.Binary("img")
    avg = fields.Integer("Average")
    speed = fields.Integer("Speed")
    rent = fields.Integer("Rent")
    type = fields.Selection([("suv", "SUV"), ("hatchback", "Hatchback"), ("sedan", "Sedan"), ("minivan", "Minivan"),
                             ("convertible", "convertible"), ("Sports car", "Sports car"), ("luxurious", "Luxurious")],
                            string="Type")
    squ = fields.Char(string="squ", readonly=True)
    invoice_id = fields.Many2one("customer.invoices",string="invoice")
    customer_details_ids = fields.One2many("customer.customer", "car_details_id","DRIVER NAME")

    @api.model
    def create(self, vals):
        vals['squ'] = self.env['ir.sequence'].next_by_code('my.sequence.code')
        print(vals)
        vals["rental_name_one"] = "my cars"
        return super(CarManagement, self).create(vals)

    @api.model
    def name_get(self):
        res = []
        for record in self:
            name = record.rent
            if record.rent:
                name = record.name + "-" + str(name)
            res.append((record.id, name))
        return res

    @api.model
    def _name_search(self, name="suv", args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('type', operator, name), ('name', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    @api.constrains('name')
    def _check_car_names(self):
        for rec in self:
            recorde = self.search([("name", "=", rec.name), ("id", "!=", rec.id)])
            if recorde:
                raise ValidationError('%s Already Exists In Car List.' % rec.name)
