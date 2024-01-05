# Copyright (c) 2023, Karthik and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymMember(FrappeTestCase):
	def test_fullname_is_set_automatically(self):
		test_driver = frappe.get.doc ({
			"doctype":"Gym Member",
			"first_name":"Rohit",
			"last_name":"Sharma"
		}).insert()

		self.assertEqual(test_driver.full_name,"Rohit Sharma")
		
		def test_fullname_is_set_correctly_when_no_last_name(self):
			test_driver = frappe.get.doc ({
			"doctype":"Gym Member",
			"first_name":"Rohit",
			"last_name":"Sharma"
		}).insert()

		self.assertEqual(test_driver.full_name,"Rohit")

