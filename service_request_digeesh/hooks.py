app_name = "service_request_digeesh"
app_title = "Service Request Digeesh"
app_publisher = "s"
app_description = "s"
app_email = "digeeshsekara@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "service_request_digeesh",
# 		"logo": "/assets/service_request_digeesh/logo.png",
# 		"title": "Service Request Digeesh",
# 		"route": "/service_request_digeesh",
# 		"has_permission": "service_request_digeesh.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/service_request_digeesh/css/service_request_digeesh.css"
# app_include_js = "/assets/service_request_digeesh/js/service_request_digeesh.js"

# include js, css files in header of web template
# web_include_css = "/assets/service_request_digeesh/css/service_request_digeesh.css"
# web_include_js = "/assets/service_request_digeesh/js/service_request_digeesh.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "service_request_digeesh/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "service_request_digeesh/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "service_request_digeesh.utils.jinja_methods",
# 	"filters": "service_request_digeesh.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "service_request_digeesh.install.before_install"
# after_install = "service_request_digeesh.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "service_request_digeesh.uninstall.before_uninstall"
# after_uninstall = "service_request_digeesh.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "service_request_digeesh.utils.before_app_install"
# after_app_install = "service_request_digeesh.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "service_request_digeesh.utils.before_app_uninstall"
# after_app_uninstall = "service_request_digeesh.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "service_request_digeesh.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"service_request_digeesh.tasks.all"
# 	],
# 	"daily": [
# 		"service_request_digeesh.tasks.daily"
# 	],
# 	"hourly": [
# 		"service_request_digeesh.tasks.hourly"
# 	],
# 	"weekly": [
# 		"service_request_digeesh.tasks.weekly"
# 	],
# 	"monthly": [
# 		"service_request_digeesh.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "service_request_digeesh.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "service_request_digeesh.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "service_request_digeesh.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["service_request_digeesh.utils.before_request"]
# after_request = ["service_request_digeesh.utils.after_request"]

# Job Events
# ----------
# before_job = ["service_request_digeesh.utils.before_job"]
# after_job = ["service_request_digeesh.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"service_request_digeesh.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    
    {
        "doctype": "Web Form",
        "filters": {
            "module": "Service Request Digeesh"
        }
    },

    
    {
        "doctype": "Workflow State",
        "filters": {
            "name": ["in", [
                "Draft",
                "Submitted",
                "Under Review",
                "Approved",
                "Rejected",
                "Reopened",
                "Pending"
            ]]
        }
    },


    {
        "doctype": "Workflow Action Master",
        "filters": {
            "name": ["in", [
                "Submit",
                "Review",
                "Approve",
                "Reject",
                "Reopen",
                "Resend for Review",
                "Draft"
            ]]
        }
    },

    {
        "doctype": "Role",
        "filters": {
            "name": ["in", [
                "Assigned Technician",
                "Service Manager",
                "Service Coordinator"
            ]]
        }
    },
    {
        "doctype": "Report",
        "filters": {
            "ref_doctype": "Service Request Form",
            "report_type": ["in", ["Script Report"]]
        }
    }


]
