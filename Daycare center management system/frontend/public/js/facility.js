// facility.js

document.addEventListener('DOMContentLoaded', () => {
    // Function to fetch all facilities
    async function fetchFacilities() {
        try {
            const response = await fetch('/facility');
            const facilities = await response.json();
            // Render facilities in UI
            renderFacilities(facilities);
        } catch (error) {
            console.error('Error fetching facilities:', error);
        }
    }

    // Function to render facilities in UI
    function renderFacilities(facilities) {
        const facilityList = document.getElementById('facilityList');
        facilityList.innerHTML = ''; // Clear previous entries
        facilities.forEach((facility) => {
            const facilityItem = document.createElement('li');
            facilityItem.textContent = facility.name;
            facilityList.appendChild(facilityItem);
        });
    }

    // Fetch facilities on page load
    fetchFacilities();

    // Add form submission event listener
    const addForm = document.getElementById('addForm');
    addForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const name = document.getElementById('name').value;
        try {
            const response = await fetch('/facility', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name })
            });
            if (response.ok) {
                // Refresh facility list
                fetchFacilities();
            } else {
                console.error('Error adding facility:', response.statusText);
            }
        } catch (error) {
            console.error('Error adding facility:', error);
        }
    });
});
