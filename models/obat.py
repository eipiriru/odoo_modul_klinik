from odoo import models, fields, api, _

class KategoriObat(models.Model):
    _name="nur_klinik.kategori_obat"

    name=fields.Char(
        string="Kategori Obat", required=True
    )

    deskripsi = fields.Text(
        string='Deskripsi Kategori Obat',
    )

class Obat(models.Model):
    _name="nur_klinik.obat"

    name = fields.Char(
        string="Nama",required=True,
    )

    kategori_obat_id = fields.Many2one(
        string='Kategori Obat',
        comodel_name='nur_klinik.kategori_obat',
        ondelete='restrict',
    )

    harga = fields.Integer(
        string="Harga Obat"
    )

    stok = fields.Integer(
        string="Persediaan",
    )

    image = fields.Binary(
        string='Gambar',
    )
    

    deskripsi = fields.Text(
        string='Deskripsi Obat',
    )
    
class Resep(models.Model):
    _name = "nur_klinik.resep"

    name = fields.Many2one(
        string='Nama Obat',
        comodel_name='nur_klinik.obat',
        ondelete='restrict',
    )

    pengambilan_resep_id = fields.Many2one(
        string='pemeriksaan ID',
        comodel_name='nur_klinik.pengambilan_resep',
        ondelete='cascade',
    )

    desc_resep = fields.Text(
        string='Resep konsumsi Obat',
        help="Takaran yang diberikan kepada pasien",
        required=True,
    )

    harga = fields.Integer(
        compute='_compute_harga', 
        string='Harga')
    
    @api.depends('name')
    def _compute_harga(self):
        for record in self:
            record.harga = record.name.harga

    deskripsi = fields.Text(
        compute='_pick_deskripsi', 
        string='Deskripsi')
    
    @api.depends('name')
    def _pick_deskripsi(self):
        for record in self:
            record.deskripsi = record.name.deskripsi
    
    qty = fields.Integer(
        string='Jumlah Beli',
        required=True,
    )

    total_harga = fields.Integer(
        compute='_compute_jumlah_harga', 
        string='Jumlah Harga')
    
    @api.depends('qty')
    def _compute_jumlah_harga(self):
        for record in self:
            record.total_harga = record.qty * record.harga
    