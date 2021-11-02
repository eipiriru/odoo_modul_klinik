# -*- coding: utf-8 -*-
{
    'name': "nur_klinik",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "ainur",
    'website': "http://www.takada.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'data/kp_sequence.xml',
        'views/report_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/pasien_view.xml',
        'views/pendaftaran_view.xml',
        'views/pemeriksaan_view.xml',
        'views/kategori_obat_view.xml',
        'views/obat_view.xml',
        'views/pengambilan_resep_view.xml',
        'views/supplier_view.xml',
        'views/pemesanan_view.xml',
        'views/layanan_view.xml',
        'views/menu.xml',
        'report/report.xml',
        'report/struk.xml',
        'report/pemesanan.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
