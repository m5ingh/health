import frappe
from healthcare.healthcare.doctype.patient.patient import get_patients_from_user
def get_context(context):
    context.users = frappe.get_list("User", fields=["first_name", "last_name"])
    patients = get_patients_from_user(frappe.session.user)
	context.patients = patients
