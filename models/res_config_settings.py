from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    _description = "task"
    is_covid = fields.Boolean(string="Is covid", config_parameter='car_Rental.is_covid')
