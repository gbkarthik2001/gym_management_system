// Copyright (c) 2023, Karthik and contributors
// For license information, please see license.txt

 frappe.ui.form.on('Gym Member', {
    refresh: function(frm) {
        frm.add_custom_button(__('Merge and Download'), function() {
             
                     const w = window.open("/api/method/gym.gym.doctype.gym_member.gym_member.download_pdf?&doc=" + encodeURIComponent((frm.doc.name)));
                     
                }    
             )}                       
});


