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


def update_appointment_status(appointment_id):
    """
    Update the status of a Patient Appointment.

    :param appointment_id: ID or name of the appointment to update.
    """
    try:
        appointment = frappe.get_doc("Patient Appointment", appointment_id)
        appointment.update_status("Cancelled")  # Replace "Your New Status" with the desired status
        frappe.msgprint(_("Appointment status updated successfully."))
    except frappe.DoesNotExistError:
        frappe.msgprint(_("Appointment not found."))
    except Exception as e:
        frappe.msgprint(_("Error updating appointment status: {0}".format(str(e))))

# ... Existing code ...
