from odoo import fields, models, api
# from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    rejected_check_account_id = fields.Many2one(
        'account.account',
        compute='compute_check_accounts',
        #readonly=True,
    )
    deferred_check_account_id = fields.Many2one(
        'account.account',
        compute='compute_check_accounts',
        #readonly=True,
    )
    holding_check_account_id = fields.Many2one(
        'account.account',
        compute='compute_check_accounts',
        #readonly=True,
    )

    def compute_check_accounts(self):
        for rec in self:
            company_id = rec.company_id
            rec.rejected_check_account_id = company_id.rejected_check_account_id
            rec.deferred_check_account_id = company_id.deferred_check_account_id
            rec.holding_check_account_id = company_id.holding_check_account_id
