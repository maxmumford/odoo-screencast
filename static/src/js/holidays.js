openerp.holidays = function (instance) {

var _t = instance.web._t,
   _lt = instance.web._lt;
var QWeb = instance.web.qweb;

instance.web.WebClient.include({
    show_application: function () {
        console.log("Show application");
        return this._super.apply(this, arguments);
    };
});

};
