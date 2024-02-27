frappe.ready(async () => {
    initializePage();
});

async function initializePage() {
    await fetchAndDisplayAppointments();
}

async function fetchAndDisplayAppointments() {
    try {
        // Use Frappe API to fetch appointments associated with the logged-in user
        let patient_id = document.getElementById('patient-list');
        const response = await frappe.call({
            method: 'healthcare.www.view-and-edit-appointments.get_user_appointments',
            args: { user: patient_id.value },
        });

        console.log(response);

        if (response.message && response.message.length > 0) {
            renderAppointments(response.message);
        } else {
            // Handle case where no appointments are found
            const appointmentsContainer = document.getElementById('appointments-container');
            appointmentsContainer.innerHTML = '<p>No appointments found.</p>';
        }
    } catch (error) {
        console.error('Error fetching appointments:', error);
        // Handle error, show message, or log it as needed
    }
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
