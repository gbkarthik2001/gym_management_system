$(window).on('hashchange', page_changed);
$(window).on('load', page_changed);

function page_changed(event) {
    frappe.after_ajax(function () {
        var route = frappe.get_route();

        if (route[0] == "Form") {
            frappe.ui.form.on(route[1], {
                onload: function (frm) {
                    frm.add_custom_button(__('Custom Button'), function() {
                        alert('From myBank button clicked');
                    });
                    frappe.msgprint("Please fill the details carefully")
                    
                }
            })
 

        }   
    })
}