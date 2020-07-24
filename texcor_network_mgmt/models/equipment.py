# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Equipment(models.Model):
    _name = 'equipment'

    MANUFACTURER = [
        ('moxa', 'Moxa'),
        ('cisco', 'Cisco'),
        ('cambium', 'Cambium'),
        ('paloalto', 'Palo Alto'),
    ]

    MODEL = [
        ('PA-850', 'PA-850'),
        ('ePMP 1000', 'ePMP 1000'),
        ('WS-C3650-24TS-L', 'WS-C3650-24TS-L'),
        ('EDS-P506E-4PoE-2GTXSFP-T', 'EDS-P506E-4PoE-2GTXSFP-T'),
        ('ICS-G7826A-20GSFP-4GTXSFP-2XG-HV-HV', 'ICS-G7826A-20GSFP-4GTXSFP-2XG-HV-HV'),
    ]

    DEVICE_TYPE = [
        ('backbone', 'Backbone'),
        ('wirelessptp', 'Wireless PTP'),
        ('wirelessptmp', 'Wireless PTMP'),
        ('l2switch', 'L2 Switch'),
        ('edge', 'Edge'),
    ]

    name = fields.Char(string='DNS Hostname')
    serial_number = fields.Char(string='Serial Number')
    mac_address = fields.Char(string='Eth Mac Address')
    firmware_version = fields.Char(string='Firmware Version')

    in_service = fields.Boolean(string='In Service')
    cpe_device = fields.Boolean(string='CPE Device')
    number_of_ports = fields.Integer(string='Number of Ports')

    model  = fields.Selection(MODEL, 'Model')
    device_type = fields.Selection(DEVICE_TYPE, 'Device Type')
    manufacturer = fields.Selection(MANUFACTURER, 'Manufacturer')
    
    ip_management_id = fields.Many2one(string='Management IP', comodel_name='ip_management', ondelete='cascade')
    pop_id = fields.Many2one(string='POP', comodel_name='pop', ondelete='cascade')
    circuit_ids = fields.One2many(string='Circuit IDs', comodel_name='circuit', inverse_name='ap_name_id', ondelete='cascade')
