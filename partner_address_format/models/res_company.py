# -*- coding: utf-8 -*-
# © 2016 Vauxoo (http://www.vauxoo.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# @author Nhomar Hernandez <nhomar@vauxoo.com>
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    address_format_id = fields.Many2one('ir.ui.view',
                                        domain=[('type', '=', 'qweb')],
                                        help='A normal view with the format to'
                                             'be used to format the address '
                                             'for this company.')
