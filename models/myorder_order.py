from odoo import models, fields, api


class Order(models.Model):
    _name = "my.order.order"
    _description = "Car Rental"