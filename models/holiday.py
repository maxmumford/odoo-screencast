# -*- coding: utf-8 -*-
from openerp.models import Model
from openerp.fields import Char, Integer

class holiday(Model):
    _name = "holidays.holiday"
    _inherit = ['mail.thread']

    name = Char()
    maximum_guests = Integer()
