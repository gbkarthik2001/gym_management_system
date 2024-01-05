# Copyright (c) 2023, Karthik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymLockerBooking(Document):
    def before_save(self):
        total_lockers = 50
        doc_type = 'Gym Locker Booking'
        entries = frappe.get_all(doc_type,fields=['name'])
        count = len(entries)+1
        self.remaining_lockers = total_lockers - count
        
    
        
    
    

    
    
    
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		# remaining_lockers = frappe.db.get_value('Gym Locker Booking', 'remaining_lockers')
		# if remaining_lockers <= 0:
		# 	frappe.throw('No More Lockers Available')

		# new_remaining_lockers = remaining_lockers - 1
		# frappe.db.set_value('Gym Locker Booking', 'remaining_lockers', new_remaining_lockers)
		


																																
