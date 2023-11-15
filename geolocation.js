// Check if the Geolocation API is available in the browser
if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;

        console.log("Your current location is:\nLatituted: " + lat 
            + "\nLongitude: " + lng);
    }, function(error) {
        console.log("Error getting location: " + error.message);
    });
} else {
    // Geolocation is not available in this browser
    console.log("Geolocation is not supported in your browser.");
}