from flask import Blueprint, request, jsonify

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify({'message': 'List of expenses'})

@expenses_bp.route('/expenses', methods=['POST'])
def create_expense():
    data = request.json
    return jsonify({'message': 'Expense created', 'data': data}), 201

@expenses_bp.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    return jsonify({'message': f'Expense {expense_id}'})

@expenses_bp.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    data = request.json
    return jsonify({'message': f'Expense {expense_id} updated', 'data': data})

@expenses_bp.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    return jsonify({'message': f'Expense {expense_id} deleted'})
