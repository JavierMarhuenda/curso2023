from odoo import fields, models

class HelpDeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Manager helpdesk tickets"

    name = fields.Char()
    sequence = fields.Integer()
    date = fields.Date()
