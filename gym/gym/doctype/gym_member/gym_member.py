# Copyright (c) 2023, Karthik and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

from frappe.utils import get_site_path
from frappe.utils.pdf import get_pdf

class GymMember(Document):
	def before_save(self):
		if self.last_name:
			self.full_name = self.first_name +" "+ self.last_name
		else:
			self.full_name = self.first_name

 
@frappe.whitelist()
def download_pdf(doc):
	doc = frappe.get_doc("Gym Member", doc)
	html1 = frappe.get_print("Gym Member", doc, "Gym Member", doc=doc, no_letterhead="no_letterhead")
	html2 = frappe.get_print("Gym Member", doc, "Gym Member 2", doc=doc, no_letterhead="no_letterhead")
	html = html1+ '\n\n' + html2
	print(html)
	pdf_content = get_pdf(html)
	name = doc.name
	frappe.local.response.filename = f"{name}.pdf"
	frappe.local.response.type = "pdf"
	frappe.local.response.filecontent = pdf_content
	frappe.local.response.preview = 0
	# frappe.local.response.type = "download"

@frappe.whitelist()
def get_list_of_all_gym_member():
	return frappe.get_all('Gym Member')
	# return frappe.db.sql(
    #     """
    #     SELECT name,dob,trainer
    #     FROM `tabGym Member`;
    #     """,
    # )
	




