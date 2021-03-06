# -*- coding: utf-8 -*-
#
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#
#    Coded by: Luis Torres (luis_t@vauxoo.com)
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
'''
This file add a constraint to unique vat.
'''
from openerp import models, api
from openerp.tools.translate import _


class res_partner(models.Model):
    '''
    Inherit res.partner to added constraint to unique vat of partner
    '''
    _inherit = 'res.partner'

    @api.one
    @api.constrains('vat')
    def _check_unique_vat(self):
        if self.vat:
            partner_ids = self.search(
                [('vat', '=', self.vat),
                 ('id', '!=', self.id)])
            for partner in partner_ids:
                if not((partner.child_ids and self.id in partner.child_ids.ids)
                       or (partner.parent_id and
                           self.parent_id == partner.parent_id)):
                    raise Warning(_(
                        'Error! Specified VAT Number already exists for any '
                        'other registered partner.'))
