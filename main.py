import argparse
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load data from JSON file
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Save data to JSON file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Setup command line argument parsing
parser = argparse.ArgumentParser(description='Run a REST API server for a JSON file.')
parser.add_argument('--file', required=True, help='Path to the JSON file to be loaded')
args = parser.parse_args()

# Load initial data from the JSON file
data_file = args.file
data = load_data(data_file)

# Home page
@app.route('/', methods=['GET'])
def display_home_page():
    return jsonify({'/user/<email>': 'display user with a given e-mail address', '/users': 'display all users'})

# CRUD operations
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)

@app.route('/user/<email>', methods=['GET'])
def get_user(email):
    user = next((user for user in data if user['email'] == email), None)
    return jsonify(user) if user else ('', 404)

@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.json
    existing_user = next((user for user in data if user['email'] == new_user['email']), None)
    if existing_user:
        return jsonify({"error": "User with this email already exists"}), 400
    data.append(new_user)
    save_data(data_file, data)
    return jsonify(new_user), 201

@app.route('/user/<email>', methods=['PUT'])
def update_user(email):
    updated_user_data = request.json
    user_index = next((index for (index, user) in enumerate(data) if user["email"] == email), None)

    if user_index is None:
        return ('', 404)

    data[user_index].update(updated_user_data)
    save_data(data_file, data)
    return jsonify(data[user_index])

@app.route('/user/<email>', methods=['DELETE'])
def delete_user(email):
    global data
    data = [user for user in data if user['email'] != email]
    save_data(data_file, data)
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
