
from odoo import models, fields, api

class SmSchoolInfo(models.Model):
    _name = 'school.info'
    _description = 'School Information'
    _rec_name = "school_name"

    school_name = fields.Char(string='Name', required=True)
    class_ids = fields.One2many('class.info', 'class_id', string="Classes")

    def action_view_classes(self):
        form_view_ref = self.env.ref('school_management.view_sm_school_classes_info_form', False)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Classes',
            'res_model': 'class.info',
            'view_mode': 'form',
            'views': [(form_view_ref.id, 'form')],
            'target': 'current',
        }

