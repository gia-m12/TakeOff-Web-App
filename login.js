function validateLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const loginError = document.getElementById("login-error");

    // Basic login validation (replace with your own logic)
    if (username === "yourUsername" && password === "yourPassword") {
        // Redirect to the main page or perform other actions
        window.location.href = "main.html";
    } else {
        loginError.textContent = "Invalid username or password. Please try again.";
    }
}