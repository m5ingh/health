import frappe
from healthcare.healthcare.doctype.patient.patient import get_patients_from_user

no_cache = 1

def get_context(context):
    context.no_cache = 1
    patients = get_patients_from_user(frappe.session.user)
    context.patients = patients

    appointments = frappe.get_all(
        "Patient Appointment",
        filters={'patient_name': ('in', [patient.get("full_name") for patient in patients])},
        fields=['name','appointment_date', 'appointment_time', 'practitioner_name']
    )
    context.appointments = appointments
