from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

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

    @api.model
    def create(self, values):
        obat = self.env['nur_klinik.obat'].search([('id','=',values['name'])])
        stok = obat.stok
        stok_sisa = stok - values['qty']
        self.env['nur_klinik.obat'].search([('id','=',values['name'])]).write({'stok': stok_sisa})
        return super(Resep, self).create(values)

    @api.model
    def write(self, values):
        obat = self.env['nur_klinik.obat'].search([('id','=',self.name.id)])
        stok = obat.stok
        stok_sisa = (stok + self.qty) - values['qty']
        self.env['nur_klinik.obat'].search([('id','=',self.name.id)]).write({'stok': stok_sisa})
        return super(Resep, self).write(values)
    
    @api.model
    def unlink(self):
        obat = self.env['nur_klinik.obat'].search([('id','=',self.name.id)])
        stok = obat.stok
        stok_sisa = stok + self.qty
        self.env['nur_klinik.obat'].search([('id','=',self.name.id)]).write({'stok': stok_sisa})
        return super(Resep, self).unlink()

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

    @api.onchange('qty')
    def _onchange_qty(self):
        if self.qty > self.name.stok:
            raise ValidationError("Jumlah beli melebihi stok yang tersedia")

    total_harga = fields.Integer(
        compute='_compute_jumlah_harga', 
        string='Jumlah Harga')
    
    @api.depends('qty')
    def _compute_jumlah_harga(self):
        for record in self:
            record.total_harga = record.qty * record.harga
    