# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "poultry"
app_title = "Erpnext Poultry Hatchery Feed Formulation"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Poultry Hatchery Feed Formulation for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/poultry/css/poultry.bundle.css"
app_include_js = "/assets/poultry/js/poultry.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "poultry.engine.on_document_submit",
        "on_cancel": "poultry.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "poultry.engine.daily_scheduled_sync"
    ]
}
