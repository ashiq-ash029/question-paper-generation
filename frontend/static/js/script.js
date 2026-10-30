document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    const response = await fetch("http://localhost:3000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password, role })
    });

    const data = await response.json();
    if (data.success) {
        // Store user details in session storage
        sessionStorage.setItem("username", username);
        sessionStorage.setItem("role", role);
        sessionStorage.setItem("department", document.getElementById("department").value);
        sessionStorage.setItem("semester", document.getElementById("semester").value);
        sessionStorage.setItem("subject", document.getElementById("subject").value);

        // Redirect to respective dashboard
        window.location.href = role === "student" ? "student.html" : "faculty.html";
    } else {
        alert("Invalid login credentials");
    }
});

// Load subjects dynamically
async function getSubjects(department_id, semester_id) {
    const response = await fetch(`http://localhost:3000/subjects?department_id=${department_id}&semester_id=${semester_id=2}`);
    const data = await response.json();
    // Populate the subject dropdown with the fetched data
  }
  async function getQuestions(department_id, semester_id, subject_id) {
    const response = await fetch(`http://localhost:3000/questions?department_id=${department_id}&semester_id=${semester_id}&subject_id=${subject_id=1}`);
    const data = await response.json();
    // Display the questions to the user
  }
  
  