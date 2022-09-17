# -*- coding: utf-8 -*-


from odoo import models, fields


class FleetReservedTime(models.Model):
    _name = "rental.fleet.reserved"
    _description = "Waktu Reservasi"

    customer_id = fields.Many2one('res.partner', string='Customer')
    date_from = fields.Date(string='Tanggal Mulai Reservasi')
    date_to = fields.Date(string='Tanggal Revervasi Hingga')
    reserved_obj = fields.Many2one('fleet.vehicle')


class EmployeeFleet(models.Model):
    _inherit = 'fleet.vehicle'

    rental_check_availability = fields.Boolean(default=True, copy=False)
    color = fields.Char(string='Color', default='#FFFFFF')
    rental_reserved_time = fields.One2many('rental.fleet.reserved', 'reserved_obj', String='Waktu Reservasi', readonly=1,
                                           ondelete='cascade')
    fuel_type = fields.Selection([('petrol', 'Bensin'),
                                  ('diesel', 'Diesel'),
                                  ('electric', 'Electric'),
                                  ('hybrid', 'Hybrid')],
                                 'Type Bahan Bakar', help='Bahan Bakar yang Digunakan oleh kendaraan')

    _sql_constraints = [('vin_sn_unique', 'unique (vin_sn)', "Nomor Sasis sudah ada !"),
                        ('license_plate_unique', 'unique (license_plate)', "Plat nomor sudah ada !")]
