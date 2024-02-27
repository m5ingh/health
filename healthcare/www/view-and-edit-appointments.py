import frappe
from frappe import _
from healthcare.healthcare.doctype.patient.patient import get_patients_from_user

no_cache = 1

def get_context(context):
	context.no_cache = 1
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)


@frappe.whitelist()
def get_user_appointments(user):
    patients = get_patients_from_user(frappe.session.user)
    appointments = frappe.get_all(
        'Patient Appointment',
        filters={'patient': user},
        fields=['name', 'appointment_date', 'appointment_time', 'practitioner']
    )
    return appointments
