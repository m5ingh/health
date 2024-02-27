import frappe
from frappe import _
from healthcare.healthcare.doctype.patient.patient import get_patients_from_user

no_cache = 1

@frappe.whitelist()
def get_user_appointments(user, context):
    patients = get_patients_from_user(frappe.session.user)
    context.patients = patients

    # Fetch appointments associated with the logged-in user
    try:
        appointments = frappe.get_all(
            'Patient Appointment',
            filters={'patient': user},
            fields=['name', 'appointment_date', 'appointment_time', 'practitioner']
        )
        return appointments
    except Exception as e:
        frappe.msgprint(f"Error fetching appointments: {str(e)}")
        return []
