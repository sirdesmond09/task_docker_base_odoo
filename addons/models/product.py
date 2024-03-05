from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools import slugify


class ProductTemplate(models.Model):
    _inherit = "product.template"

    slug = fields.Char(string="Slug", compute="_compute_slug", store=True)
    additional_barcode = fields.Char(string="Additional Barcode", unique=True)

    @api.depends("name")
    def _compute_slug(self):
        for record in self:
            record.slug = slugify(record.name)

    @api.constrains("additional_barcode")
    def _check_additional_barcode_unique(self):
        for record in self:
            if record.additional_barcode:
                existing_product = self.env["product.template"].search(
                    [("additional_barcode", "=", record.additional_barcode)]
                )
                if existing_product:
                    raise ValidationError("Additional barcode must be unique.")
