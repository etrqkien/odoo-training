from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.base.res.res_request import referenceable_models


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'

    name = fields.Char('Name', size=40, translate=True)
    # Many2many inverse relationship
    task_ids = fields.Many2many(
        'todo.task',
        string='Tasks')

    # quan hệ thứ bậc
    _parent_store = True  # thêm hỗ trợ tìm kiếm phân cấp
    _parent_name = 'parent_id'  # the default
    parent_id = fields.Many2one(
        'todo.task.tag',
        'Parent Tag',
        ondelete='restrict')
    parent_left = fields.Integer('Parent Left', index=True)
    parent_right = fields.Integer('Parent Right', index=True)
    child_ids = fields.One2many(
        'todo.task.tag',
        'parent_id',
        'Child Tags')


class Stage(models.Model):
    # _name : mã định danh
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    # đặt thứ tự mặc định để sử dụng khi hồ sơ của mô hình được duyệt hoặc hiển thị trong chế độ xem danh sách.
    _order = 'sequence,name'
    # cho biết trường để sử dụng làm mô tả bản ghi khi được tham chiếu từ các trường có liên quan,
    # Theo mặc định, nó sử fields=name, thường được tìm thấy
    # trường trong mô hình.thuộc tính này cho phép chúng ta sử dụng bất kỳ trường nào khác cho mục đích đó.
    _rec_name = 'name'  # the default
    _table_name = 'todo_task_stage'  # tên của CSDL mô hình

    name = fields.Char(
        string='Name',
        # Common field attributes:
        copy=False,  # no coppy
        default='New',  # value default
        groups='base.group_user,base.group_no_one',
        # nhóm cho phép giới hạn quyền truy cập và khả năng hiển thị của trường chỉ với một số nhóm
        help='The title for the stage.',
        index=True,  # tạo chỉ mục scdl trên fields
        readonly=False,  # làm cho trường theo mặc định không thể bị chỉnh sửa
        required=True,  # trường theo mặc định bắt buộc phải có
        states={'done': [('readonly', False)]},
        # rạng thái mong đợi một giá trị ánh xạ từ điển cho các thuộc tính UI tùy thuộc vào giá trị của trạng thái
        # String only attributes:
        size=40,
        translate=True,
    )

    # Other string fields:
    desc = fields.Text('Description')
    state = fields.Selection(
        [('draft', 'New'), ('open', 'Started'), ('done', 'Closed')],
        'State',
        # selection_add= When extending a Model, adds items to selection list
    )
    docs = fields.Html('Documentation')

    # Numeric fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))

    # Date fields:
    effective_date = fields.Date('Effective Date')
    write_date = fields.Datetime('Last Changed')

    # Boolean lưu trữ data true or false
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

    # One2many inverse relation:
    task_ids = fields.One2many(
        'todo.task',
        'stage_id',
        'Tasks in this stage')


class TodoTask(models.Model):
    _inherit = 'todo.task'

    # Relational fields
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many(
        'todo.task.tag',  # related= (model liên quan
        'todo_task_tag_rel',  # relation= (table quan hệ
        'task_id',  # column1= ("this" field)
        'tag_id',  # column2= ("other" field)
        string='Tags',
        # Relational field attributes:
        auto_join=False,
        context={},
        domain=[],
        ondelete='cascade',
    )
    # Dynamic Reference fields:
    refers_to = fields.Reference(
        # Set a Selection list, such as:
        # [('res.user', 'User'), ('res.partner', 'Partner')],
        # Or use standard "Referencable Models":
        referenceable_models,
        'Refers to',  # string= (title)
    )
    # Related fields:
    state = fields.Selection(
        related='stage_id.state',
        string='Stage State',
        store=True,  # optional
    )
    # Calculated fields:
    stage_fold = fields.Boolean(
        string='Stage Folded?',
        compute='_compute_stage_fold',
        search='_search_stage_fold',
        inverse='_write_stage_fold',
        store=False,  # the default
    )
    effort_estimate = fields.Integer('Effort Estimate')

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for todo in self:
            todo.stage_fold = todo.stage_id.fold

    # Hàm tìm kiếm được gọi bất cứ khi nào điều kiện (trường, toán tử, giá trị) trên trường này được tìm thấy
    # trong biểu thức miền tìm kiếm.
    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    # hàm nghịc đảo _search _stage_fold
    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    # Constraints Các rằng buộc sql| name:một tên ràng buộc SQL hợp lệ,
    # sql_definitionlà một biểu thức table_constraint
    # semessagelà thông báo lỗi.
    _sql_constraints = [(
        'todo_task_name_unique',
        'UNIQUE (name, active)',
        'Task title must be unique!'
    )]

    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Title must have 5 chars!')

    # hàm tính toán số task của user
    def compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count(
                [('user_id', '=', task.user_id.id)])

    user_todo_count = fields.Integer(
        'User To-Do Count',
        compute='compute_user_todo_count')
