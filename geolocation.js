// Check if the Geolocation API is available in the browser
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(sendPosition);
} else {
    // Geolocation is not available in this browser
    console.log("Geolocation is not supported in your browser.");
}

function sendPosition(position) {
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;

    // Send this data to your Python backend
    fetch('http://localhost:5000/get_coordinates', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ lat, lng }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
}