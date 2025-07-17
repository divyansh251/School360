
from odoo import models, fields, api

class SmSchoolInfo(models.Model):
    _name = 'school.info'
    _description = 'School Information'
    _rec_name = "name"

    name = fields.Char(string='Name', required=True)
    school_name = fields.Char(string='School Name', required=True)
    principle_name = fields.Char(string='Principal Name', required=True)
    class_ids = fields.One2many('class.info', 'class_id', string="Classes")

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['name'] = ''
        if self.school_name:
            res['name'] = 'My School'
        return res

    def open_school_form(self):
        school = self.search([], limit=1)
        if len(school) == 1:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'school.info',
                'view_mode': 'form',
                'res_id': school.id,
                'target': 'current',
            }
        else:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'school.info',
                'view_mode': 'list,form',
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


