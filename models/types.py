from odoo import fields, models


class Types(models.Model):
    _name = "costing.types"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "costing types table"
    _order = "sequence,id"

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer('sequence', help="Sequence for the handle.", default=10)