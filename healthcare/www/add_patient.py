# healthcare/www/add_patient.py
import frappe
from frappe import _

no_cache = 1

def get_context(context):
	context.no_cache = 1
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

@frappe.whitelist()
def add_patient_reg(first_name, gender,email,mobile):

    invite_user = 0
    new_patient = frappe.get_doc({
        'doctype': 'Patient',
        'first_name': first_name,
        'sex': gender,
        'email': email,
        'mobile': mobile,
        'invite_user': invite_user
    })

    # Save the new patient document
    new_patient.insert(ignore_permissions=True)

    return {
        'name': new_patient.name,
        'message': 'Patient added successfully!'
    }
