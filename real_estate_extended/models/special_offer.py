from odoo import _,api,fields,models

class special_offer(models.Model):
    _name="special.offer"
    _inherits = {'estate.property.offer': 'offer_ids'}

    offer_ids=fields.Many2one("estate.property.offer")
    discounted_price=fields.Float()

