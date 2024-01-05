# Copyright (c) 2023, Karthik and contributors
# For license information, please see license.txt
import frappe


def execute(filters=None):
    columns, data =[
        {
        "label":"Most class booking",
        "fieldname":"class_type",
        "fieldtype":"select",
    },
        {  
        "label":"Booking Count",
        "fieldname":"booking_count",
        "fieldtype":"int",
        },
        
        # {  
        # "label":"Height",
        # "fieldname":"member_hieght",
        # "fieldtype":"float",
        # },
        # {  
        # "label":"Calories",
        # "fieldname":"calories",
        # "fieldtype":"float",
        # },
		],[]
     
    data = frappe.db.sql("""
        SELECT class_type, COUNT(class_type) as `booking_count`
        FROM `tabGym Class Booking`
        GROUP BY `class_type`
        ORDER BY `booking_count` DESC;
        
    """, as_dict=1)
     
    return columns,data
