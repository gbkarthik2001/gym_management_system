# Copyright (c) 2023, Karthik and contributors
# For license information, please see license.txt

 # Copyright (c) 2023, Karthik and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns, data = [
        {
            "label": "Member",
            "fieldname": "member",
            "fieldtype": "Link",
            "options": "Gym Member", 
            "width": 120,
        },
        {
            "label": "Membership",
            "fieldname": "membership_type",
            "fieldtype": "Select",
            "width": 120,
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 120,
        },
    ], []

    records = frappe.db.sql(
        """
        SELECT member, membership_type, price
        FROM `tabGym Membership`;
        """,
        as_dict=1,
    )

    revenue_by_membership_type = {}
    for record in records:
        key = (record["member"], record["membership_type"])
        if key in revenue_by_membership_type:
            revenue_by_membership_type[key] += record["price"]
        else:
            revenue_by_membership_type[key] = record["price"]

    for (member, membership_type), revenue in revenue_by_membership_type.items():
        data.append({"member": member, "membership_type": membership_type, "revenue": revenue})

    return columns, data

