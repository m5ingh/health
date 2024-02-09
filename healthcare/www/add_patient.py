# healthcare/www/add_patient.py
import frappe

@frappe.whitelist()
def add_patient_reg(first_name, gender,email):
    new_patient = frappe.get_doc({
        'doctype': 'Patient',
        'first_name': first_name,
        'sex': gender,
	'email': email
    })

    # Save the new patient document
    new_patient.insert(ignore_permissions=True)

    return {
        'name': new_patient.name,
        'message': 'Patient added successfully!'
    }
