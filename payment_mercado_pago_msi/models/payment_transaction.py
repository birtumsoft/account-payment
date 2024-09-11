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

from odoo import models

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _mercado_pago_prepare_preference_request_payload(self):
        """ Method that modifies the payment attempt creation preferences to add the number of interest-free
            installments to be offered if the option to use installments is enabled.
            :return: The request payload.
            :rtype: dict
        """

        payload = super()._mercado_pago_prepare_preference_request_payload()
        if self.provider_id.use_installments:
            payload['payment_methods'].update(dict(
                installments=max(self.provider_id.installments, 1)
            ))

        return payload
