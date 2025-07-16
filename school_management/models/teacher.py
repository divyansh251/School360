
from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    subject = fields.Char(string='Subject')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    join_date = fields.Date(string='Join Date')
