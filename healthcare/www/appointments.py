import frappe
from healthcare.healthcare.doctype.patient.patient import get_patients_from_user

no_cache = 1

def get_context(context):
    context.no_cache = 1
    context.users = frappe.get_list("User", fields=["first_name", "last_name"])
    patients = get_patients_from_user(frappe.session.user)
    context.patients = patients

    for patient in patients:
        patient_name = patient.get("full_name")  # Access the full_name attribute using get method
        # Do something with patient_name if needed

    # Corrected the loop to access each patient's name
    appointments = frappe.get_all(
        "Patient Appointment",
        filters={'patient_name': ('in', [patient.get("full_name") for patient in patients])},
        fields=['naming_series','appointment_date', 'appointment_time', 'practitioner_name']
    )
    context.appointments = appointments
