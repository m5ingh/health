function add_patient() {
    // Collect patient data from the input fields
    let first_name = $("#first_name").val();
    let gender = $("#gender option:selected").val();
    let email = $("#email").val();
    let mobile = $("#mobile").val();
    // Make a request to the server-side API to add a new patient
    frappe.call({
        method: 'healthcare.www.add_patient.add_patient_reg',
        args: {
            first_name: first_name,
            gender: gender,
            email: email,
            mobile: mobile
        },
        callback: (r) => {
            if (!r.exc && r.message) {
                // Success message or redirect to a success page
                frappe.msgprint(__("Patient added successfully! Redirecting"));
                window.location.href = '/departments';
            } else {
                // Handle errors
                frappe.msgprint(__("Error adding patient. Please try again."));
            }
        }
    });
}

