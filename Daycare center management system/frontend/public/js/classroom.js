// classroom.js

document.addEventListener('DOMContentLoaded', () => {
    const addClassroomForm = document.getElementById('addClassroomForm');
    const classroomList = document.getElementById('classroomList');

    // Event listener for form submission
    addClassroomForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        // Get form data
        const formData = new FormData(addClassroomForm);
        const name = formData.get('name');
        const capacity = formData.get('capacity');
        const facility_id = formData.get('facility_id');

        try {
            // Send POST request to add classroom
            const response = await fetch('/classroom', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, capacity, facility_id })
            });

            if (response.ok) {
                // Classroom added successfully, update UI
                const classroom = await response.json();
                const listItem = document.createElement('li');
                listItem.textContent = `Name: ${classroom.name}, Capacity: ${classroom.capacity}, Facility_id: ${classroom.facility_id}`;
                classroomList.appendChild(listItem);

                // Clear form fields
                addClassroomForm.reset();
            } else {
                // Handle error
                console.error('Failed to add classroom:', response.statusText);
            }
        } catch (error) {
            console.error('Error adding classroom:', error);
        }
    });
});
