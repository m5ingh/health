import frappe
from frappe import _

@frappe.whitelist()
def get_user_appointments(user):
    # Fetch appointments associated with the logged-in user
    appointments = frappe.get_all('Patient Appointment', filters={'patient': user}, fields=['name', 'appointment_date', 'appointment_time', 'practitioner'])
    return appointments
