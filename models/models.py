# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime
from odoo.exceptions import UserError, ValidationError


class Pasien(models.Model):
    _name = 'nur_klinik.pasien'
    _description = 'Pasien'

    name = fields.Char(
        string = 'Nama',
        required = True
    )
    nik = fields.Char(
        string = 'NIK',
        required=True
    )

    tgl_lahir = fields.Date(
        string='Tanggal Lahir',
    )
    
    umur = fields.Char(
        string='Umur',
        compute = "_hitung_umur",
    )

    @api.depends('tgl_lahir')
    def _hitung_umur(self):
        if self.tgl_lahir:
            year = str(self.tgl_lahir)
            year = year.split("-")
            now = int(datetime.datetime.now().year)
            self.umur = now - int(year[0])
        else:
            self.umur = 0

    alamat = fields.Text(
        string='Alamat',
        required=True,
    )

    riwayat_ids = fields.One2many(
        string='Pengambilan resepID',
        comodel_name='nur_klinik.pengambilan_resep',
        inverse_name='pasien_id',
    )
    

class PengambilanResep(models.Model):
    _name = "nur_klinik.pengambilan_resep"

    name = fields.Char(
        string='Kode Pemeriksaan',
        readonly=True,
        default = 'New'
    )

    @api.model
    def create(self, values):
        values['name'] = self.env['ir.sequence'].next_by_code('nur_klinik.seq_kp') or _('New')
        return super(PengambilanResep, self).create(values)

    pasien_id = fields.Many2one(
        string='Pasien',
        comodel_name='nur_klinik.pasien',
        ondelete='restrict',
        delegate=True,
    )

    layanan_id = fields.Many2one(
        string='Layanan Kesehatan',
        comodel_name='nur_klinik.layanan',
        ondelete='restrict',
        delegate=True,
    )

    tgl_periksa = fields.Date(
        string='Tanggal Periksa',
        default=fields.Date.context_today,
    )

    diagnosa = fields.Text(
        string = "Diagnosis",
    )

    resep_ids = fields.One2many(
        string='Resep',
        comodel_name='nur_klinik.resep',
        inverse_name='pengambilan_resep_id',
    )

    sudah_diperiksa = fields.Boolean(
        string = "Sudah Diperiksa",
        default=False,
    )

    sudah_dibayar = fields.Boolean(
        string = "Sudah Dibayar",
        default=False,
    )

    total_harga = fields.Integer(
        compute='_compute_total_harga', 
        string='Total Tagihan'
    )
   
    @api.model
    def _compute_total_harga(self):        
        for record in self:           
            total = sum(self.env['nur_klinik.resep'].search([('pengambilan_resep_id','=', record.id)]).mapped('total_harga'))
            record.total_harga = total
    
    tagihan = fields.Integer(
        compute='_compute_tagihan', 
        string='Tagihan',
    )

    @api.model
    def _compute_tagihan(self):        
        for record in self:           
            total = self.total_harga + self.layanan_id.harga_admin
            record.tagihan = total