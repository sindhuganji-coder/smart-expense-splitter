from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Create a Blueprint for auth routes
auth_bp = Blueprint('auth', __name__)

# In-memory user storage (replace with database in production)
users = {}

@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if username already exists
    if username in users:
        return jsonify({'message': 'User already exists!'}), 400

    # Hash password and store user
    users[username] = generate_password_hash(password)
    return jsonify({'message': 'User registered successfully!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if user exists
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful!'}), 200
