from odoo import models


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    def button_undo_reconciliation(self):
        
        self.payment_ids.write({'move_name': False})
        payment_groups = self.payment_ids.mapped('payment_group_id')
        res = super(AccountBankStatementLine, self).button_undo_reconciliation()
        if payment_groups:
            payment_groups.write({'state': 'draft'})
            payment_groups.unlink()
        return res

    def _prepare_counterpart_move_line_vals(self, counterpart_vals, move_line=None):
        """ Pass reconcilation parameters by context in order to
        capture them in the post() method and be able to get a better
        partner_id/partner_type interpetration
        """
        return super(AccountBankStatementLine, self.with_context(
            counterpart_vals=counterpart_vals,
            move_line=move_line,
            create_from_statement=True,
            ))._prepare_counterpart_move_line_vals(counterpart_vals, move_line=move_line)
