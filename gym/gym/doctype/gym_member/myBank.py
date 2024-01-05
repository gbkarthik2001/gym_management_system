
import frappe
from frappe.model.document import Document
from erpnext.accounts.doctype.bank.bank import Bank
class myBank(Bank):
    def validate(self):
        if not self.swift_number[:3].isalpha():
            frappe.msgprint("First 3 digits are Alphabets")
        super(myBank,self).validate()


@frappe.whitelist(allow_guest=True)
def get_user_info():
	return {
		"user": "Hello",
		"user_type": "hello Type"
	}