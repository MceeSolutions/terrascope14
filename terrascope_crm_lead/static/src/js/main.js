odoo.define('terrascope_crm_lead.dest_onchange', function(require){
    
    'use_strict';
    
    function myFunction() {
        var x = document.getElementById("mySelect").value;
        document.getElementById("demo").innerHTML = "You selected: " + x;
    }

});
