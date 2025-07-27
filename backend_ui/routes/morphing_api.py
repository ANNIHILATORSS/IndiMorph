from flask import Blueprint, request, jsonify
from backend_ui.monitoring import morph_requests, reset_requests, status_requests
from backend_ui.security import jwt_required

morphing_api = Blueprint('morphing_api', __name__)

# Dummy actuator state
ACTUATOR_STATE = {'angles': [90, 90, 90, 90], 'status': 'idle'}

@morphing_api.route('/morph', methods=['POST'])
@jwt_required
def morph():
    morph_requests.inc()
    data = request.json
    angles = data.get('angles', [90, 90, 90, 90])
    ACTUATOR_STATE['angles'] = angles
    ACTUATOR_STATE['status'] = 'morphing'
    # TODO: Send command to hardware
    return jsonify({'success': True, 'angles': angles})

@morphing_api.route('/reset', methods=['POST'])
@jwt_required
def reset():
    reset_requests.inc()
    ACTUATOR_STATE['angles'] = [90, 90, 90, 90]
    ACTUATOR_STATE['status'] = 'reset'
    # TODO: Send reset command to hardware
    return jsonify({'success': True})

@morphing_api.route('/status', methods=['GET'])
@jwt_required
def status():
    status_requests.inc()
    return jsonify(ACTUATOR_STATE) 