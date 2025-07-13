// Copyright (c) 2025, s and contributors
// For license information, please see license.txt


frappe.query_reports["Pending Service Requests"] = {
    "filters": [
        {
            "fieldname": "request_type",
            "label": "Request Type",
            "fieldtype": "Select",
            "options": "\nInstallation\nMaintenance\nRepair",
            "default": ""
        },
        {
            "fieldname": "priority",
            "label": "Priority",
            "fieldtype": "Select",
            "options": "\nLow\nMedium\nHigh",
            "default": ""
        },
        {
            "fieldname": "from_date",
            "label": "From Date",
            "fieldtype": "Date",
            "default": frappe.datetime.add_days(frappe.datetime.get_today(), -7)
        },
        {
            "fieldname": "to_date",
            "label": "To Date",
            "fieldtype": "Date",
            "default": frappe.datetime.get_today()
        }
    ]
}
