# Copyright (c) 2023, Karthik and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class GymWorkoutPlans(Document):
	def before_save(self):
		if not self.get("exercises", {"exercise_name": "Body build",}):
			row = self.append("exercises", {})
			row.exercise_name = "Body build"
			row.sets ="5"
			row.reps="10"


		# if not self.get("add_ons", {"item": "Egg",}):
		# 	row = self.append("add_ons", {})
		# 	row.item = "EGG" 
		# 	row.amount = egg
