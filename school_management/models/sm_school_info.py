
from odoo import models, fields, api

class SmSchoolInfo(models.Model):
    _name = 'school.info'
    _description = 'School Information'
    _rec_name = "school_name"

    school_name = fields.Char(string='Name', required=True)
    class_ids = fields.One2many('class.info', 'class_id', string="Classes")


