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

    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                # FORWARDPORT UP TO 10.0
                if order.company_id.tax_calculation_rounding_method == 'round_globally':
                    taxes = line.taxes_id.compute_all(line.price_unit, line.order_id.currency_id, line.product_qty, product=line.product_id, partner=line.order_id.partner_id)
                    amount_tax += sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
                else:
                    amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
            })

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