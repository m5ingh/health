function fetchAndDisplayAppointments() {

    // Use Frappe API to fetch appointments associated with the logged-in user
    let patient_id = document.getElementById('patient-list');
    let user = patient_id.value;
    console.log(user);
    frappe.call({
        method: 'healthcare.www.view-and-edit-appointments.get_user_appointments',
        args: { user: user },
        callback: (r) => {
            if (!r.exc && r.message) {
                renderAppointments(r.message);  // Corrected from response.message to r.message
            } else {
                // Handle case where no appointments are found
                const appointmentsContainer = document.getElementById('appointments-container');
                appointmentsContainer.innerHTML = '<p>No appointments found.</p>';
            }
        }
    });
}

function renderAppointments(appointments) {
    const appointmentsContainer = document.getElementById('appointments-container');

    appointments.forEach(appointment => {
        const appointmentElement = document.createElement('div');
        appointmentElement.innerHTML = `
            <p>Date: ${appointment.appointment_date}</p>
            <p>Time: ${appointment.appointment_time}</p>
            <p>Practitioner: ${appointment.practitioner}</p>
            <button onclick="viewAppointment('${appointment.name}')">View</button>
            <button onclick="cancelAppointment('${appointment.name}')">Cancel</button>
            <hr>
        `;
        appointmentsContainer.appendChild(appointmentElement);
    });
}

function viewAppointment(appointmentId) {
    // Logic to handle viewing appointment details
    // You may navigate to a new page or show a modal with detailed information
}

function cancelAppointment(appointmentId) {
    // Logic to handle canceling the appointment
    // You may show a confirmation dialog and then use Frappe API to cancel the appointment
}
