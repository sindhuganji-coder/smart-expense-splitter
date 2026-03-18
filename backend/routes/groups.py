from flask import Blueprint, request, jsonify

# Create a Blueprint for group management
groups_bp = Blueprint('groups', __name__)

# In-memory storage for groups (you may want to use a database)
groups = []

# API route to create a new group
@groups_bp.route('/groups', methods=['POST'])
def create_group():
    data = request.json
    group_name = data.get('name')
    if not group_name:
        return jsonify({'error': 'Group name is required'}), 400
    new_group = {'id': len(groups) + 1, 'name': group_name}
    groups.append(new_group)
    return jsonify(new_group), 201

# API route to get all groups
@groups_bp.route('/groups', methods=['GET'])
def get_groups():
    return jsonify(groups), 200

# API route to get a group by ID
@groups_bp.route('/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    group = next((g for g in groups if g['id'] == group_id), None)
    if group:
        return jsonify(group), 200
    return jsonify({'error': 'Group not found'}), 404

# API route to update a group
@groups_bp.route('/groups/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    data = request.json
    group = next((g for g in groups if g['id'] == group_id), None)
    if not group:
        return jsonify({'error': 'Group not found'}), 404
    group_name = data.get('name')
    if group_name:
        group['name'] = group_name
    return jsonify(group), 200

# API route to delete a group
@groups_bp.route('/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    global groups
    group = next((g for g in groups if g['id'] == group_id), None)
    if not group:
        return jsonify({'error': 'Group not found'}), 404
    groups = [g for g in groups if g['id'] != group_id]
    return jsonify({'message': 'Group deleted'}), 200
