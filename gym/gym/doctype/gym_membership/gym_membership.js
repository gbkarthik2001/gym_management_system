// Copyright (c) 2023, Karthik and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', {
	 membership_type: function(frm) {
		if (frm.doc.membership_type == 'Weekly'){
			frm.set_value("price", "350");
			frm.set_value("duration", "3600");
		}
		if (frm.doc.membership_type == 'Monthly'){
			frm.set_value("price", "750");
			frm.set_value("duration", "5400");
		
	}
		if (frm.doc.membership_type == 'Yearly'){
			frm.set_value("price", "5000");
			frm.set_value("duration", "5400");
		
    }
 }
});

