
from odoo import models, fields

class SmStudentInfo(models.Model):
    _name = 'school.student.info'
    _description = 'Students Information'

    name = fields.Char(string='Name', required=True)
    roll_no = fields.Char(string='Roll No')
    class_name = fields.Char(string='Class')
    parent_contact = fields.Char(string='Parent Contact')
    admission_date = fields.Date(string='Admission Date')
    student_id = fields.Many2one('class.info', string="Student")

