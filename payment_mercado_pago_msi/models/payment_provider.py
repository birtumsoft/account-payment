# -*- coding: utf-8 -*-
######################################################################
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2024 Birtum - https://www.birtum.com
# All Rights Reserved.
#
# Developer(s): Joanner Paz Martínez
#               jpm@birtum.com
######################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
######################################################################

import logging

from odoo import _, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    use_installments = fields.Boolean("Use installments")
    installments = fields.Integer("Installments", default=1, help="The number of maximum installments to offer.")

    def write(self, vals):
        if 'installments' in vals and vals['installments'] <= 0:
            raise UserError(_("The installments value must be greater than cero"))
        res = super().write(vals)
        return res
