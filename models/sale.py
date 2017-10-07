# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Rubén Bravo <rubenred18@gmail.com>
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
###############################################################################

from odoo import fields, models
from odoo.addons import decimal_precision as dp
import logging
_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _name = "sale.order.line"
    _inherit = 'sale.order.line'

    price_unit = fields.Float(digits=dp.get_precision('Product Price 2'))
    price_subtotal = fields.Float(digits=dp.get_precision('Product Price 2'))


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = 'sale.order'

    amount_untaxed = fields.Float(store=True, readonly=True,
                                    compute='_amount_all',
                                    track_visibility='onchange',
                                    digits=dp.get_precision('Product Price 2'))
    amount_tax = fields.Float(store=True, readonly=True, compute='_amount_all',
                                digits=dp.get_precision('Product Price 2'))
    amount_total = fields.Float(store=True, readonly=True,
                                compute='_amount_all',
                                track_visibility='always',
                                digits=dp.get_precision('Product Price 2'))
    amount_discount = fields.Float(digits=dp.get_precision('Product Price 2'))