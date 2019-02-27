# -*- coding: utf8 -*-
from odoo import models, fields, api
from odoo.addons.base.res.res_request import referenceable_models
from odoo.exceptions import ValidationError

class Tag(models.Model):
    _name = "todo.task.tag"
    _description = "Todo Tag"

    name = fields.Char(string="Name", size=40, translate=True)

    task_ids = fields.Many2many("todo.task", string="Tasks")

    _parent_store = True
    _parent_name = 'parent_id'  # the default

    parent_id = fields.Many2one('todo.task.tag', 'Parent Tag', ondelete='restrict')

    parent_left = fields.Integer("Parent Left", index = True)
    parent_right = fields.Integer("Parent Right", index = True)
    child_ids = fields.One2many("todo.task.tag", "parent_id", "Child Tags")


class Stage(models.Model):
    _name = "todo.task.stage"
    _description = "Todo Stage"
    _order = "sequence, name"
    _rec_name = 'name'  # the default
    _table_name = 'todo_task_stage'  # the default

    # String fields
    name = fields.Char(
        string='Name',
        # Common field attributes:
        copy=False,
        default='New',
        groups='base.group_user,base.group_no_one',
        help='The title for the stage.',
        index=True,
        readonly=False,
        required=True,
        states={'done': [('readonly', False)]},
        # String only attributes:
        size=40,
        translate=True,
    )
    desc = fields.Text("Description")
    state = fields.Selection([('draft', "News"), ('open', "Started"), ('done', "Closed")], "State")
    doc = fields.Html("Documentation")

    # Numeric Field
    sequence = fields.Integer("Sequence")
    perc_complete = fields.Float("% Complete", (3, 2))

    # Date Fields
    effective_date = fields.Date("Date Effective")
    write_date = fields.Date("Last Changed")

    # Other Field
    fold = fields.Boolean("Folded?")
    image = fields.Binary("Image")

    task = fields.One2many("todo.task", "stage_id", "Tasks in this Stage")
    # One2many inverse relation:
    task_ids = fields.One2many(
        'todo.task',
        'stage_id',
        'Tasks in this stage')

class TodoTask(models.Model):
    _inherit = 'todo.task'
    _sql_constraints = [('todo_task_name_uniq',
                         'UNIQUE (name, active)',
                         'TAsk Title Unique!')]

    stage_id = fields.Many2one("todo.task.stage", "Stage")
    tag_ids = fields.Many2many(
        'todo.task.tag',  # related= (model name)
        'todo_task_tag_rel',  # relation= (table name)
        'task_id',  # column1= ("this" field)
        'tag_id',  # column2= ("other" field)
        string='Tags',
        # Relational field attributes:
        auto_join=False,
        context={},
        domain=[],
        ondelete='cascade',
    )
    stage_fold = fields.Boolean(
        string='Stage Folded?',
        compute='_compute_stage_fold',
        search='_search_stage_fold',
        inverse='_write_stage_fold',
        store=False,  # the default
    )

    state = fields.Selection(
        related='stage_id.state',
        string='Stage State',
        store=True,  # optional
    )

    effort_esstimate = fields.Integer("Effort Esstimate")

    # stage_state = fields.Selection(related = "stage_id.state", string="Stage State")

    refers_to = fields.Reference(referenceable_models, 'Refers To')

    user_todo_count = fields.Integer("User Todo Count", compute="compute_user_todo_count")

    @api.depends("stage_id.fold")
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold

    def compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count([('user_id', '=', task.user_id.id)])

    def _search_stage_fold(self, operator, value):
        return [("stage_id.fold", operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError("Name must have >= 5 character !")