import frappe

def execute():
    gym_members = frappe.get_all("Gym Member",fields=["name","is_registered"])
    for gym_member in gym_members:
        if gym_member.is_registered:   
             frappe.db.set_value("Gym Member",gym_member.name,"registration_status","Completed")
        else:
            frappe.db.set_value("Gym Member",gym_member.name,"registration_status","Not Done")


   
