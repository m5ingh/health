# healthcare/www/add_patient.py
import frappe

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
    # Get the current site URL
    site_url = frappe.utils.get_url()

    # Construct the redirect URL by prefixing it with the site URL
    redirect_url = frappe.utils.get_url() + '/departments'

    return {
        'name': new_patient.name,
        'message': 'Patient added successfully!'
        'redirect_url': redirect_url
    }
