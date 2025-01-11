// Fetch teachers and display them on the page
window.addEventListener('DOMContentLoaded', () => {
    fetchTeachers();
});

// Function to fetch teachers from the backend
async function fetchTeachers() {
    try {
        const response = await fetch('/teacher');
        const teachers = await response.json();
        displayTeachers(teachers);
    } catch (error) {
        console.error('Error fetching teachers:', error);
    }
}

// Function to display teachers on the page
function displayTeachers(teachers) {
    const teacherList = document.getElementById('teacherList');
    teacherList.innerHTML = ''; // Clear existing content

    teachers.forEach(teacher => {
        const li = document.createElement('li');
        li.textContent = `${teacher.firstname} ${teacher.lastname} ${teacher.room}`;
        teacherList.appendChild(li);
    });
}
