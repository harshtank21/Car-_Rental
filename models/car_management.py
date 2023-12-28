from odoo import models, fields, api


class CarManagement(models.Model):
    _name = "car.management"
    _description = "Car Rental"
    # _rec_name = "speed"

    name = fields.Char(string="Name", required=True)
    img = fields.Binary("img")
    avg = fields.Integer("Average")
    speed = fields.Integer("Speed")
    rent = fields.Integer("Rent")
    type = fields.Selection([("suv", "SUV"), ("hatchback", "Hatchback"), ("sedan", "Sedan"), ("minivan", "Minivan"),
                             ("convertible", "convertible"), ("Sports car", "Sports car"), ("luxurious", "Luxurious")],
                            string="Type")
    squ = fields.Char(string="squ", readonly=True)

    @api.model
    def create(self, vals):
        vals['squ'] = self.env['ir.sequence'].next_by_code('my.sequence.code')
        return super(CarManagement, self).create(vals)

    # @api.depends('name', 'speed')
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
        print("----------------------------------_>",limit)
        args = args or []
        domain = []
        if name:
            domain = ['|', ('type', operator, name), ('name', operator, name)]
            # domain = [('type', operator, name),('type', "=", "suv")]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     name="luxurious"
    #     ids = self._name_search(name, args, operator, limit=limit)
    #     return self.browse(ids).sudo().name_get()
