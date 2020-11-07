from odoo import fields, models


class Costing(models.Model):
    _name = "costing.cost"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "costing table"

    name = fields.Char(required=True)
    customer = fields.Many2one(comodel_name='res.partner')
    season = fields.Char(string='Season')
    style = fields.Char(string='Style/ Ref Name')
    concept = fields.Char(string='Product Concept')
    type = fields.Many2one(comodel_name='costing.types')
    company = fields.Many2one(comodel_name='res.company')
    pricelist = fields.Many2one(comodel_name='product.pricelist')
    currency = fields.Many2one(comodel_name='res.currency')
    stage = fields.Many2one(comodel_name='costing.stages')
    cost_sheet_details = fields.Char(string='Cost Sheet Details')
    board = fields.Char(string='Board')
    order_quantity = fields.Char(string='Order Quantity')
    size_range = fields.Char(string='Size/Range')
    sample_size = fields.Char(string='Sample Size')
    specification = fields.Char(string='Specification')
    merch_of_division = fields.Char(string='Merch Of Division')
    merch_fabrication = fields.Char(string='Merch Offerings')
    merch_size_offerings = fields.Char(string='Merch Size Offerings')
    spec_pattern = fields.Char(string='Spec/Pattern')
    child_id = fields.One2many('costing.cost_sheet_lines', 'parent_id', string="Cost Sheet Lines")

    class Costsheetlines(models.Model):
        _name = "costing.cost_sheet_lines"
        _description = "Cost sheet lines tab"
        name = fields.Char(string='Particulars', required=True)
        display_type = fields.Selection([
            ('line_section', "Section"),
            ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
        description = fields.Char(string="Description")
        placement = fields.Char(string="placement")
        supplier = fields.Char(string="Supplier")
        cuttable_width = fields.Char(string="Cuttable Width")
        consumption = fields.Char(string="Consumption")
        uom = fields.Many2one(comodel_name='uom.uom')
        currency = fields.Many2one(comodel_name='res.currency')
        cost_of_item = fields.Char(string="Cost Of Item(Ex-works/CIF/CFR)")
        parent_id = fields.Many2one('costing.cost', string="Cost Sheet Lines")








