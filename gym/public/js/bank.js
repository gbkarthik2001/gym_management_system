frappe.ui.form.on('Bank', {
    refresh: function(frm) {   
        frm.add_custom_button(__('Custom Button'), function() {
            alert('From myBank button clicked');
        });
    }
});