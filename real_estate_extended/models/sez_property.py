from odoo import _, api, fields, models

class sez_property(models.Model):
    _name="estate.property"
    _inherit="estate.property"

    city = fields.Char(string="City")

# class sez_property(models.Model):
#     _name = "real.estate.property"
#     _inherit = "estate.property"

#     home_city = fields.Char()



