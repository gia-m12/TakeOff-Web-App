var locationInfo = {
    // origin
    lat: null,
    lng: null,
    // destination
    addr: null
};

// Get user origin
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(updateUserOrigin);
} else {
    // Check if browser supports Geolocation API
    console.log("Geolocation is not supported in your browser.");
}

function updateUserOrigin(position) {
    locationInfo.lat = position.coords.latitude;
    locationInfo.lng = position.coords.longitude;
}

// Reads user destination from html text box
function getUserDestination() {
    locationInfo.addr = document.getElementById("user-destination-input").value;

    if (locationInfo.lat != null && locationInfo.lng != null) {
        sendLocationInfo();
    }
}

// Sends location information stored in locationInfo
function sendLocationInfo() {
    const{lat, lng, addr} = locationInfo;

    console.log(`lat: ${lat}, lng: ${lng}, address: ${addr}`);

    // Send this data to your Python backend
    if (lat != null && lng != null && addr != null) {
        fetch('http://localhost:5001/get_coordinates', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "lat": lat, "lng": lng, "address": addr}),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json(); // Parse the JSON in the response
        })
        .then(data => {
            // Handle the data received from the backend
            console.log('Response from server:', data);
            updateAirportInfo(data);
            // You can do more with the data here if needed
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}

function updateAirportInfo(data) {
    if (data.origin_airport && data.des_airport) {
        document.getElementById('origin-airport-name').innerText = data.origin_airport.name;
        document.getElementById('destination-airport-name').innerText = data.des_airport.name;

        updateMap(data.origin_airport, data.des_airport); // From mapdata.js
    }
}
