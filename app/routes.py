from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({
        "message": "Parking Lot API is running",
        "status": "ok"
    })

@main.route('/slots')
def get_slots():
    return jsonify({
        "total_slots": 10,
        "available": 7,
        "occupied": 3
    })

@main.route('/slots/<int:slot_id>')
def get_slot(slot_id):
    return jsonify({
        "slot_id": slot_id,
        "status": "available"
    })