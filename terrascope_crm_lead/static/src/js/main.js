// odoo.define('terrascope_crm_lead.dest_onchange', function(require){
    
//     'use_strict';
    
//     function myFunction() {
//         var x = document.getElementById("mySelect").value;
//         document.getElementById("demo").innerHTML = "You selected: " + x;
//     }

// });
function myFunction() {
    odoo.define( function (require) {
    var rpc = require('web.rpc');
    var model = 'product.product';
    // Use an empty array to search for all the records
    var dest_id = document.getElementById("destination").value;
    var product_id = parseInt(document.getElementById("product_id").value);
    var domain = [['product_tmpl_id', '=', product_id],['product_template_attribute_value_ids.name', '=', dest_id]];
    // Use an empty array to read all the fields of the records
    var fields = ['id','name','lst_price','currency_id'];
    rpc.query({
        model: model,
        method: 'search_read',
        args: [domain, fields],
    }).then(function (data) {
        boat = data[0];
        currency = boat.currency_id;
        document.getElementById("estimated_cost").innerHTML = currency[1] + boat.lst_price;
    });
    });
}
