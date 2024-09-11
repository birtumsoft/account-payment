
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
