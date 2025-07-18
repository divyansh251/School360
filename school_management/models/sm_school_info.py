
from odoo import models, fields, api

class SmSchoolInfo(models.Model):
    _name = 'school.info'
    _description = 'School Information'
    _rec_name = "name"

    name = fields.Char(string='Name')
    school_name = fields.Char(string='School Name', required=True)
    principal_name = fields.Char(string='Principal Name', required=True)
    class_ids = fields.One2many('class.info', 'class_id', string="Classes")

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['name'] = 'My School'
        return res

    def open_school_form(self):
        school = self.search([], limit=1)

        if len(school) == 1:
            school_info_form_view_ref = self.env.ref('school_management.view_sm_school_info_form', False)
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'school.info',
                'view_mode': 'form',
                'res_id': school.id,
                'views': [(school_info_form_view_ref.id, 'form')],
                'target': 'current',
            }

        school_creation_form_view_ref = self.env.ref('school_management.view_sm_school_creation_form', False)
        list_form_view_ref = self.env.ref('school_management.view_sm_school_info_list', False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'school.info',
            'view_mode': 'list,form',
            'views': [(list_form_view_ref.id, 'list'), (school_creation_form_view_ref.id, 'form')],
            'help': """
                    <p class="o_view_nocontent_smiling_face">
                        Add a New School
                    </p>
                    <p>
                        You have to create a school for the very first time only!!
                    </p>
                """,
            'target': 'current',
        }


