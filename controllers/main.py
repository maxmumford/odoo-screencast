# -*- coding: utf-8 -*-
from openerp import http

class main(http.Controller):
    @http.route('/holidays/main', auth='public', website=True)
    def index(self, **kw):
        cr, uid, context, pool = http.request.cr, http.request.uid, http.request.context, http.request.registry
        holiday_ids = pool['holidays.holiday'].search(cr, uid, [], context=context)
        holidays = pool['holidays.holiday'].browse(cr, uid, holiday_ids, context=context)
        return http.request.website.render('holidays.website_list', {'holidays': holidays})

    @http.route('/holidays/<model("holidays.holiday"):holiday>', auth='public', website=True)
    def show(self, holiday, **kw):
        return http.request.website.render('holidays.website_show', {'holiday': holiday})
