from odoo import fields, models

class TicketSoporte(models.Model):
    _name = 'ticket.soporte'
    _description = 'Modelo para reportes de soporte'

    name = fields.Char(string='Asunto del Ticket', required=True)
    descripcion = fields.Text(string='Descripción de la falla')
    prioridad = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta')
    ], string='Prioridad', default='1')
    fecha_reporte = fields.Date(string='Fecha', default=fields.Date.today)
