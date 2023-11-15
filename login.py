from flask import Flask, request, jsonify

app = Flask(__name__)


# Handle POST request to '/login'
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()  # Get the JSON data from the request
        username = data.get('username')
        hashed_password = data.get('hashedPassword')

        # Here, you would typically handle authentication logic
        # For example, check credentials against a database

        # Dummy response for demonstration
        if username == 'john_doe' and hashed_password == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8':
            response = jsonify({'success': True, 'message': 'Login successful'})
            response.headers.add('Allow', 'POST')  # Add Allow header for POST method
            return response
        else:
            response = jsonify({'success': False, 'message': 'Login failed'})
            response.headers.add('Allow', 'POST')  # Add Allow header for POST method
            return response, 401
    else:
        # Handle other methods (e.g., if someone tries a different method for /login)
        response = jsonify({'message': 'Method Not Allowed'})
        response.headers.add('Allow', 'POST')  # Add Allow header for POST method
        return response, 405


if __name__ == '__main__':
    print("Running")
    app.run(debug=True)  # Run the app
