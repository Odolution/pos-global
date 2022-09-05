from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.addons.point_of_sale.models.pos_config import PosConfig as AV
import threading
class Pos_Setting(models.Model):
    _inherit = "pos.config"
    is_master=fields.Boolean("Is Master",compute='_ismaster')
    def _ismaster(self):
        main_pos=self.env['res.config.settings'].search([]).select_shop
        if main_pos.id == self.id:
            self.is_master=True
        else:
            self.is_master=False
    def change_all(self):
        main_pos=self.env['res.config.settings'].search([])
        fields_to_chnage=self.env['ir.model.fields'].search([('model_id','=','pos.config')])
        except_main_pos=self.env['pos.config'].search([('id','!=',main_pos.select_shop.id)])
        for pos in except_main_pos:
            for fl in fields_to_chnage:
                if fl.name not in ['id','name']:
                    pos.write({
                        fl.name:main_pos.select_shop[fl.name]
                    })

class Conf_Setting(models.TransientModel):
    _inherit = "res.config.settings"
    
    select_shop = fields.Many2one("pos.config", string="Select Master Shop")

    @api.model
    def get_values(self):
        res = super(Conf_Setting, self).get_values()
        # raise UserError(type(self.env['ir.config_parameter'].sudo().get_param('pos_master_setting.select_shop')))
        res.update(
            select_shop = int(self.env['ir.config_parameter'].sudo().get_param('pos_master_setting.select_shop')),
        )
        return res

    def set_values(self):
        super(Conf_Setting, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        field1 = self.select_shop and self.select_shop.id or False

        param.set_param('pos_master_setting.select_shop', field1)
