# Copyright (c) 2025, s and contributors
# For license information, please see license.txt


import frappe
from frappe.utils import getdate

def execute(filters=None):
    filters = filters or {}

    columns = [
        {"label": "Request ID", "fieldname": "name", "fieldtype": "Link", "options": "Service Request Form", "width": 150},
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": "Request Type", "fieldname": "request_type", "fieldtype": "Data", "width": 150},
        {"label": "Priority", "fieldname": "priority", "fieldtype": "Data", "width": 100},
        {"label": "Status", "fieldname": "workflow_state", "fieldtype": "Data", "width": 120},
        {"label": "Estimated Hours", "fieldname": "total_estimated_hours", "fieldtype": "Float", "width": 130},
        {"label": "Estimated Cost", "fieldname": "total_estimated_cost", "fieldtype": "Currency", "width": 130},
        {"label": "Created On", "fieldname": "created_on", "fieldtype": "Datetime", "width": 160}
    ]

    conditions = "1=1"
    values = {}

    if filters.get("request_type"):
        conditions += " AND request_type = %(request_type)s"
        values["request_type"] = filters["request_type"]

    if filters.get("priority"):
        conditions += " AND priority = %(priority)s"
        values["priority"] = filters["priority"]

    if filters.get("from_date") and filters.get("to_date"):
        conditions += " AND DATE(created_on) BETWEEN %(from_date)s AND %(to_date)s"
        values["from_date"] = filters["from_date"]
        values["to_date"] = filters["to_date"]

    data = frappe.db.sql(f"""
        SELECT
            name, customer, request_type, priority,
            workflow_state, total_estimated_hours,
            total_estimated_cost, created_on
        FROM `tabService Request Form`
        WHERE {conditions}
        AND workflow_state NOT IN ('Approved', 'Rejected')
        ORDER BY created_on DESC
    """, values, as_dict=True)

    return columns, data
