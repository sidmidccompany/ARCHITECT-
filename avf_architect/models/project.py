from odoo import models, fields


class ArchitectProject(models.Model):
    _name = 'architect.project'
    _description = 'Architectural Project'

    name = fields.Char(required=True)
    description = fields.Text()
    project_manager_id = fields.Many2one('res.users', string='Project Manager')
    start_date = fields.Date()
    end_date = fields.Date()
    blueprint_ids = fields.One2many('architect.blueprint', 'project_id', string='Blueprints')


class ArchitectBlueprint(models.Model):
    _name = 'architect.blueprint'
    _description = 'Project Blueprint'

    name = fields.Char(required=True)
    file = fields.Binary(attachment=True)
    project_id = fields.Many2one('architect.project', required=True, ondelete='cascade')
