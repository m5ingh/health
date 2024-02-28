import frappe
from healthcare.healthcare.doctype.patient.patient import get_patients_from_user

no_cache = 1

def get_context(context):
    context.no_cache = 1
    context.users = frappe.get_list("User", fields=["first_name", "last_name"])
    patients = get_patients_from_user(frappe.session.user)
    context.patients = patients
