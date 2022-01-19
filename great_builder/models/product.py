# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductUpdate(models.Model):
    _name = 'product.update'
    _description = 'Product Update'

    product_id = fields.Many2one('product.product', string='Product')
    note = fields.Char(string="Note")
    new_product_name = fields.Char(string="New Product")

    def button_change(self):
        self.product_id.write({'name':self.new_product_name})

