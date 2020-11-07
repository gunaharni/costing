from odoo import fields, models


class Stages(models.Model):
    _name = "costing.stages"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'costing.approval']
    _description = "costing stages table"
    _order = "sequence"

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer('sequence', help="Sequence for the handle.", default=10)
    type = fields.Many2one(comodel_name='costing.types')
    folded_in_kanban_view = fields.Boolean(string='Folded in kanban view', required=True)
    allow_to_apply_changes = fields.Boolean(string='Allow to apply changes', required=True)
    final_stage = fields.Boolean(string='Final stage', required=True)
    child_id = fields.One2many('costing.approval', 'parent_id', string="Approval")

    class Approval(models.Model):
        _name = "costing.approval"
        _description = "Approval tab"

        role = fields.Char(string="Role")
        users = fields.Many2many('res.users', string="Users")
        approval_type = fields.Selection(
            [('approves, but the approval is optional', 'Approves, but the approval is optional'),
             ('is required to approve', 'Is required to approve'), ('comments only', 'Comments only')])
        parent_id = fields.Many2one('costing.stages', string="Approval")
