# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2021 Birtum - https://www.birtum.com
# All Rights Reserved.
#
# Developer(s): Alfredo Bello Telles
#               (abt@wedoo.tech)
#########################################################
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
#########################################################

from odoo import models, fields


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    """
    Este campo se encuentra en la vista de account_withholding
    """
    payment_method_code = fields.Char(
        related='payment_method_id.code'
    )
