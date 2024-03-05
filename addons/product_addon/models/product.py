from odoo import models, fields, api
from odoo.exceptions import ValidationError
from slugify import slugify


class ProductTemplate(models.Model):
    _inherit = "product.template"

    slug = fields.Char(string="Slug", compute="_compute_slug", store=True)
    additional_barcode = fields.Char(string="Additional Barcode")

    @api.depends("name")
    def _compute_slug(self):
        for record in self:
            if record.name:
                record["slug"] = slugify(str(record.name))
            else:
                record["slug"] = ""

    @api.constrains("additional_barcode")
    def _check_additional_barcode_unique(self):
        for record in self:
            if record["additional_barcode"]:
                existing_product = self.env["product.template"].search(
                    [
                        ("additional_barcode", "=", record.additional_barcode),
                        ("id", "!=", record.id),
                    ]
                )
                if existing_product:
                    raise ValidationError("Additional barcode must be unique.")
