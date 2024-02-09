# healthcare/www/add_patient.py
import frappe

@frappe.whitelist()
def add_patient_reg(first_name, gender, email):
    print("Received values - First Name:", first_name)
    print("Received values - Gender:", gender)
    print("Received values - Email:", email)
    # Create a new patient document
    new_patient = frappe.get_doc({
        'doctype': 'Patient',
        'first_name': first_name,
        'gender': gender,
        'email': email
        # Add other fields as needed
    })

    # Save the new patient document
    new_patient.insert(ignore_permissions=True)

    return {
        'name': new_patient.name,
        'message': 'Patient added successfully!'
    }
