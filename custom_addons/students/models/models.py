# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Students(models.Model):
    _name = 'students.students'  
    _description = 'Student Information'

    sid = fields.Char(string='Student ID', required=True, size=10,unique=True)
    name = fields.Char(string='Name', required=True, size=100)
    birthdate = fields.Date(string='Birthdate', required=True)
    nrc = fields.Char(string='NRC', required=True, size=50)
    fname = fields.Char(string='Father Name', required=True, size=20)
    state = fields.Char(string='State', required=True, size=20)
    division = fields.Char(string='Division', required=True, size=20)
    address = fields.Text(string='Address', required=True)
    phone = fields.Char(string='Phone', required=True, size=20)
    email = fields.Char(string='Email', size=100)
    student_details = fields.One2many('student.details', 'sid', string='Student Details')

   

class Details(models.Model):
    _name = 'student.details'
    _description = 'Student Details'

    sid = fields.Many2one('students.students', string='Student ID', required=True, ondelete='cascade')  # Foreign Key
    did = fields.Char(string='DID', required=True, size=10)
    year = fields.Char(string='Year', required=True, size=10)
    mark1 = fields.Integer(string='Mark1')
    mark2 = fields.Integer(string='Mark2')
    description = fields.Text()

    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
