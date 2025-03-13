// Generic function to fetch and display data
async function fetchData(url, elementId, formatter, emptyMessage = "No data available.") {
    try {
        const response = await fetch(url);
        const data = await response.json();
        const listElement = document.getElementById(elementId);
        listElement.innerHTML = data.length ? "" : `<li>${emptyMessage}</li>`;

        data.forEach(item => {
            const listItem = document.createElement("li");
            listItem.innerHTML = formatter(item);
            listElement.appendChild(listItem);
        });
    } catch (error) {
        console.error(`Error fetching data from ${url}:`, error);
    }
}

// Formatters for different data types
const formatDoctor = doctor => `${doctor.name} (${doctor.specialization})`;
const formatPatient = patient => `${patient.name} (${patient.blood_group}) - Assigned Doctor: ${patient.assigned_doctor || "Not Assigned"}`;
const formatConsultation = request => `${request.patient_name} - Status: ${request.status}`;

// Initial Fetch
fetchData('/api/doctors', 'doctor-list', formatDoctor, "No doctors available.");
fetchData('/api/patients', 'patient-list', formatPatient, "No patients available.");
fetchData('/api/consultations', 'consultation-list', formatConsultation);
