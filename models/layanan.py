from odoo import models, fields, api, _
import datetime


class Layanan(models.Model):
    _name = "nur_klinik.layanan"

    name = fields.Char(
        string='Nama Layanan',
        required=True,
        help="Pemeriksaan Kesehatan"
    )

    biaya_obat = fields.Boolean(
        string='Butuh Obat-Obatan',
        default=False
    )

    biaya_admin = fields.Boolean(
        string='Biaya Admin',
        default=True
    )

    harga_admin = fields.Integer(
        string = "Nominal Biaya Admin",
    )

    deskripsi = fields.Text(
        string='Deskripsi layanan',
    )
        
    