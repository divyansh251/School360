
from odoo import models, fields

class SmClassInfo(models.Model):
    _name = 'class.info'
    _description = 'Class Information'
    _rec_name = "class_standard"

    class_standard = fields.Char(string='Class Name')
    student_ids = fields.One2many('school.student.info', 'student_id', string="Students")
    class_id = fields.Many2one('school.info', string="Class")
