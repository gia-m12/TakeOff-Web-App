function validateLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const loginError = document.getElementById("login-error");
    const hashedPassword = CryptoJS.SHA256(password).toString();
    console.log(username);
    console.log(hashedPassword);
    console.log(loginError);
    // Basic login validation (replace with your own logic)
    fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, hashedPassword }),
      })
        .then(response => response.json())
        .then(data => {
          // Handle response from the server
          console.log(data);
          // Redirect or display appropriate message based on authentication result
        })
        .catch(error => {
          console.error('Error:', error);
        })};