# healthcare/www/add_patient.py
import frappe

no_cache = 1

@frappe.whitelist()
def add_patient_reg(first_name, gender,email,mobile,context):
    # Check if the user is logged in
    context.no_cache = 1
    if frappe.session.user == 'Guest':
        frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

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
