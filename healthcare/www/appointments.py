import frappe
from frappe import _
from healthcare.healthcare.doctype.patient.patient import get_patients_from_user

no_cache = 1

def get_context(context):
    context.no_cache = 1
    if frappe.session.user=='Guest':
        frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)
    patients = get_patients_from_user(frappe.session.user)
    context.patients = patients

    appointments = frappe.get_all(
        "Patient Appointment",
        filters={'patient_name': ('in', [patient.get("full_name") for patient in patients])},
        fields=['name','appointment_date', 'appointment_time', 'practitioner_name']
    )
    context.appointments = appointments

@frappe.whitelist()
def update_appointment_status(appointment_id):
    status = "Cancelled"
    appointment = frappe.get_doc({
        'doctype': 'Patient Appointment',
        'name': appointment_id,
        'status': status
        })
    appointment.update_status(appointment_id, status)
    if appointment:
        frappe.msgprint(_("Appointment Cancelled"))
    else:
        frappe.msgprint(_("Appointment not Cancelled"))

