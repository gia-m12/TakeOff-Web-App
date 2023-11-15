from flask import Flask, request, jsonify

app = Flask(__name__)


# Handle POST request to '/login'
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Get the JSON data from the request
    print("Received Info")
    username = data.get('username')
    hashed_password = data.get('hashedPassword')

    # Here, you would typically handle authentication logic
    # For example, check credentials against a database

    # Dummy response for demonstration
    if username == 'john_doe' and hashed_password == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8':
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Login failed'}), 401


if __name__ == '__main__':
    print("Running")
    app.run(debug=True)  # Run the app
