frappe.ready(async () => {
    initializePage();
});

async function initializePage() {
    await fetchAndDisplayAppointments();
}

async function fetchAndDisplayAppointments() {
    // Use Frappe API to fetch appointments associated with the logged-in user
    const appointments = await frappe.call({
        method: 'your_appointment_module.get_user_appointments',
        args: { user: frappe.session.user },
    });

    // Display the fetched appointments on the page
    renderAppointments(appointments.message);
}

function renderAppointments(appointments) {
    // Logic to render appointments on the HTML page
    // You can use JavaScript DOM manipulation or a template library like Handlebars
    // Example: Update the DOM with appointment details
    const appointmentsContainer = document.getElementById('appointments-container');

    appointments.forEach(appointment => {
        const appointmentElement = document.createElement('div');
        appointmentElement.innerHTML = `
            <p>Date: ${appointment.date}</p>
            <p>Time: ${appointment.time}</p>
            <p>Practitioner: ${appointment.practitioner}</p>
            <button onclick="viewAppointment('${appointment.id}')">View</button>
            <button onclick="cancelAppointment('${appointment.id}')">Cancel</button>
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
