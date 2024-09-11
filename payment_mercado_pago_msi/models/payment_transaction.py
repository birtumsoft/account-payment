
import logging
import pprint
from urllib.parse import quote as url_quote

from werkzeug import urls

from odoo import _, api, models
from odoo.exceptions import UserError, ValidationError

from odoo.addons.payment_mercado_pago import const
from odoo.addons.payment_mercado_pago.controllers.main import MercadoPagoController


_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _mercado_pago_prepare_preference_request_payload(self):

        payload = super()._mercado_pago_prepare_preference_request_payload()
        if self.provider_id.use_installments:
            payload['payment_methods'].update(dict(
                installments=max(self.provider_id.installments, 1)
            ))

        return payload
