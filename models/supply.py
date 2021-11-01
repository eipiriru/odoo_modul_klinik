from odoo import models, fields, api, _

class Supplier(models.Model):
    _name = 'nur_klinik.supplier'
    _description = 'Supplier'

    name = fields.Char(
        string = 'Nama Supplier',
        required = True
    )

    desc = fields.Text(
        string='Deskripsi',
    )

class Pemesanan(models.Model):
    _name = "nur_klinik.pemesanan"

    name = fields.Many2one(
        string='Supplier',
        comodel_name='nur_klinik.supplier',
        ondelete='restrict',
    )

    transaksi_ids = fields.One2many(
        string='Transaksi',
        comodel_name='nur_klinik.transaksi',
        inverse_name='pemesanan_id',
    )

class Transaksi(models.Model):
    _name = "nur_klinik.transaksi"

    name = fields.Many2one(
        string='Barang',
        comodel_name='nur_klinik.obat',
        ondelete='restrict',
        domain=[('stok','<',10)] 
    )
    
    pemesanan_id = fields.Many2one(
        string='Pemesanan ID',
        comodel_name='nur_klinik.pemesanan',
        ondelete='cascade',
    )

    qty = fields.Integer(
        string='Jumlah Beli',
        required=True,
    )
    