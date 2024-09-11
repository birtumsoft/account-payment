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
{
    'name': "MSI settings for Mercado Pago",
    'version': '17.0.0.1',
    'category': 'Accounting/Payment Providers',
    'sequence': 350,
    'summary': "Extension for Mercado Pago adding MSI settings.",
    'description': "Extension for Mercado Pago adding MSI settings.",
    'depends': ['payment', 'payment_mercado_pago'],
    'data': [
        'views/payment_provider_views.xml',
    ],
    'license': 'LGPL-3',
}
