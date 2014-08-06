# -*- coding: utf-8 -*-
from openerp import http

class main(http.Controller):
    @http.route('/holidays/main', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world!"

