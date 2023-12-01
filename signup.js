function validateSignup() {
    var newUsername = document.getElementById("newUsername").value;
    var newPassword = document.getElementById("newPassword").value;
    var signupError = document.getElementById("signup-error");

    // Basic validation - checking if the fields are not empty
    if (newUsername === "" || newPassword === "") {
        signupError.textContent = "Please fill in all fields.";
        return;
    }

    document.getElementById("signupForm").reset();
    signupError.textContent = ""; 
}