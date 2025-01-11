// child.js

window.onload = () => {
    // Function to fetch and display children
    const fetchChildren = async () => {
        try {
            const response = await fetch('/child');
            const data = await response.json();
            const childList = document.getElementById('childList');
            // Clear existing list
            childList.innerHTML = '';
            // Populate list with fetched children
            data.forEach(child => {
                const li = document.createElement('li');
                li.textContent = `${child.firstname} ${child.lastname} - Age: ${child.age}, Room: ${child.room}`;
                childList.appendChild(li);
            });
        } catch (error) {
            console.error('Error fetching children:', error);
        }
    };

    // Fetch and display children when the page loads
    fetchChildren();

    // Add event listener to form for adding a new child
    const addChildForm = document.getElementById('addChildForm');
    addChildForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(addChildForm);
        const newChild = {
            firstname: formData.get('firstname'),
            lastname: formData.get('lastname'),
            age: formData.get('age'),
            room: formData.get('room')
        };
        try {
            const response = await fetch('/child', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newChild)
            });
            if (response.ok) {
                console.log('Child added successfully');
                // Refresh the list of children
                fetchChildren();
            } else {
                console.error('Failed to add child');
            }
        } catch (error) {
            console.error('Error adding child:', error);
        }
    });
};
