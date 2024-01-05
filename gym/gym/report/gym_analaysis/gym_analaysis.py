# Copyright (c) 2023, Karthik and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns, data =[
        {
        "label":"Member",
        "fieldname":"member",
        "fieldtype":"link",
    },
        {  
        "label":"Weight",
        "fieldname":"member_weight",
        "fieldtype":"float",
        },
        
        {  
        "label":"Height",
        "fieldname":"member_hieght",
        "fieldtype":"float",
        },
        {  
        "label":"Calories",
        "fieldname":"calories",
        "fieldtype":"float",
        },
		],[]
    data = frappe.db.sql(
        """
        SELECT member_weight,member,member_hieght,calories
        FROM `tabGym Class Booking`
        """,	
        as_dict=1,
        
    )
	
    return columns,data


