##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api
# import odoo.addons.decimal_precision as dp
# from odoo.exceptions import ValidationError
# from dateutil.relativedelta import relativedelta
# import datetime


class AccountPayment(models.Model):
    _inherit = "account.payment"

    automatic = fields.Boolean(
    )
    withholding_accumulated_payments = fields.Selection(
        related='tax_withholding_id.withholding_accumulated_payments',
    )
    withholdable_invoiced_amount = fields.Float(
        'Importe imputado sujeto a retencion',
        # compute='get_withholding_data',
        readonly=True,
    )
    withholdable_advanced_amount = fields.Float(
        'Importe a cuenta sujeto a retencion',
        # compute='get_withholding_data',
        readonly=True,
    )
    accumulated_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    total_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    withholding_non_taxable_minimum = fields.Float(
        'Non-taxable Minimum',
        # compute='get_withholding_data',
        readonly=True,
    )
    withholding_non_taxable_amount = fields.Float(
        'Non-taxable Amount',
        # compute='get_withholding_data',
        readonly=True,
    )
    withholdable_base_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    period_withholding_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    previous_withholding_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    computed_withholding_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )

    payment_date = fields.Date(related='date', string="Payment date")

    # == Payment difference fields ==
    payment_difference = fields.Monetary(
        compute='_compute_payment_difference')
    payment_difference_handling = fields.Selection([
        ('open', 'Keep open'),
        ('reconcile', 'Mark as fully paid'),
    ], default='open', string="Payment Difference Handling")
    writeoff_account_id = fields.Many2one('account.account',
                                          string="Difference Account",
                                          copy=False,
                                          domain="[('deprecated', '=', False), ('company_id', '=', company_id)]")
    writeoff_label = fields.Char(string='Journal Item Label',
                                 default='Write-Off',
                                 help='Change label of the counterpart that will hold the payment difference')

    @api.depends('amount', 'currency_id')
    def _compute_payment_difference(self):
        for rec in self:
            if rec.payment_group_id.currency_id == rec.currency_id:
                # Same currency.
                rec.payment_difference = rec.payment_group_id.to_pay_amount - rec.amount
            elif rec.currency_id == rec.company_id.currency_id:
                # Payment expressed on the company's currency.
                rec.payment_difference = rec.payment_group_id.to_pay_amount - rec.amount
            else:
                # Foreign currency on payment different than the one set on the journal entries.
                amount_payment_currency = rec.company_id.currency_id._convert(
                    rec.payment_group_id.to_pay_amount - rec.payment_group_id.payments_amount, rec.currency_id, rec.company_id,
                    rec.payment_date)
                rec.payment_difference = amount_payment_currency - rec.amount

    def _get_counterpart_move_line_vals(self, invoice=False):
        vals = super(AccountPayment, self)._get_counterpart_move_line_vals(
            invoice=invoice)
        if self.payment_group_id:
            # we check they are code withholding and we get taxes
            taxes = self.payment_group_id.payment_ids.filtered(
                lambda x: x.payment_method_code == 'withholding').mapped(
                'tax_withholding_id')
            vals['tax_ids'] = [(6, False, taxes.ids)]
        return vals

class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    automatic = fields.Boolean(
    )
    withholding_accumulated_payments = fields.Selection(
        related='tax_withholding_id.withholding_accumulated_payments',
    )
    withholdable_invoiced_amount = fields.Float(
        'Importe imputado sujeto a retencion',
        # compute='get_withholding_data',
        readonly=True,
    )
    withholdable_advanced_amount = fields.Float(
        'Importe a cuenta sujeto a retencion',
        # compute='get_withholding_data',
        readonly=True,
    )
    accumulated_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    total_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    withholding_non_taxable_minimum = fields.Float(
        'Non-taxable Minimum',
        # compute='get_withholding_data',
        readonly=True,
    )
    withholding_non_taxable_amount = fields.Float(
        'Non-taxable Amount',
        # compute='get_withholding_data',
        readonly=True,
    )
    withholdable_base_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    period_withholding_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    previous_withholding_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )
    computed_withholding_amount = fields.Float(
        # compute='get_withholding_data',
        readonly=True,
    )


    def _create_payment_vals_from_batch(self, batch_result):
        res = super(AccountPaymentRegister,self)._create_payment_vals_from_batch(batch_result)
        res.update({
            'automatic': self.automatic,
            'withholding_accumulated_payments': self.withholding_accumulated_payments,
            'withholdable_invoiced_amount': self.withholdable_invoiced_amount,
            'withholdable_advanced_amount': self.withholdable_advanced_amount,
            'accumulated_amount': self.accumulated_amount,
            'total_amount': self.total_amount,
            'withholding_non_taxable_minimum': self.withholding_non_taxable_minimum,
            'withholding_non_taxable_amount': self.withholding_non_taxable_amount,
            'withholdable_base_amount': self.withholdable_base_amount,
            'period_withholding_amount': self.period_withholding_amount,
            'previous_withholding_amount': self.previous_withholding_amount,
            'computed_withholding_amount': self.computed_withholding_amount,

        })
        return res