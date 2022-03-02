from . import __version__ as app_version

app_name = "ecosoft_support_app"
app_title = "Ecosoft Support App"
app_publisher = "Ecosoft"
app_description = "Ehanced support features for Ecosoft"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kittiu@ecosoft.co.th"
app_license = "MIT"

fixtures = [
    {
		"dt": "Custom Field",
		"filters": [("name", "in", [
			"Issue-time_spent",
			"Issue-project_name",
			"Project-support_hours",
			"Project-support_hours_used",
		])],
	},
    {
		"dt": "Project Type",
		"filters": [["project_type", "in", ["Support Package"]]],
	},
	{
		"dt": "Property Setter",
		"filters": [["name", "in", [
			"Issue-project-mandatory_depends_on",
			"Issue-project-allow_in_quick_entry",
			"Issue-customer-fetch_if_empty",
		]]],
	},
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ecosoft_support_app/css/ecosoft_support_app.css"
# app_include_js = "/assets/ecosoft_support_app/js/ecosoft_support_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/ecosoft_support_app/css/ecosoft_support_app.css"
# web_include_js = "/assets/ecosoft_support_app/js/ecosoft_support_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ecosoft_support_app/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ecosoft_support_app.install.before_install"
# after_install = "ecosoft_support_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ecosoft_support_app.uninstall.before_uninstall"
# after_uninstall = "ecosoft_support_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ecosoft_support_app.notifications.get_notification_config"

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

doc_events = {
	"Issue": {
		"on_update": [
			"ecosoft_support_app.ecosoft_support_app.support.update_project_support_hours",
		],
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ecosoft_support_app.tasks.all"
# 	],
# 	"daily": [
# 		"ecosoft_support_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"ecosoft_support_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ecosoft_support_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ecosoft_support_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ecosoft_support_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ecosoft_support_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ecosoft_support_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ecosoft_support_app.auth.validate"
# ]

