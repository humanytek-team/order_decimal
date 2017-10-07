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


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = 'purchase.order'

    amount_untaxed = fields.Float(store=True, readonly=True,
                                    compute='_amount_all',
                                    track_visibility='always',
                                    digits=dp.get_precision('Product Price 2'))
    amount_tax = fields.Float(store=True, readonly=True,
                                compute='_amount_all',
                                digits=dp.get_precision('Product Price 2'))
    amount_total = fields.Float(store=True, readonly=True,
                                    compute='_amount_all',
                                    digits=dp.get_precision('Product Price 2'))


class PurchaseOrderLine(models.Model):
    _name = "purchase.order.line"
    _inherit = 'purchase.order.line'

    price_unit = fields.Float(digits=dp.get_precision('Product Price 2'))
    price_subtotal = fields.Float(compute='_compute_amount', store=True,
                                    digits=dp.get_precision('Product Price 2'))
    price_total = fields.Float(compute='_compute_amount', store=True,
                                digits=dp.get_precision('Product Price 2'))
    price_tax = fields.Float(compute='_compute_amount', store=True,
                            digits=dp.get_precision('Product Price 2'))