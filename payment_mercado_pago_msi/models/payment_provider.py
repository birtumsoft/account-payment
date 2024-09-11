
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
