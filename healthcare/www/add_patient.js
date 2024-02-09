function add_patient() {
    // Collect patient data from the input fields
    let first_name = $("#first_name").val();
    let gender = $("#gender option:selected").val();
    let email = frappe.session.user;  // Use frappe.session.user to get the logged-in user's email

    // Log the values to the console for debugging
    console.log("First Name:", first_name);
    console.log("Gender:", gender);
    console.log("Email:", email);

    // Make a request to the server-side API to add a new patient
    frappe.call({
        method: 'healthcare.www.add_patient.add_patient_reg',
        args: {
            first_name: first_name,
            gender: gender,
            email: email
            // Add other fields as needed
        },
        callback: (r) => {
            if (!r.exc && r.message) {
                // Success message or redirect to a success page
                frappe.msgprint(__("Patient added successfully!"));
            } else {
                // Handle errors
                frappe.msgprint(__("Error adding patient. Please try again."));
            }
        }
    });
}

