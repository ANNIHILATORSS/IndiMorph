from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.morphing_api import morphing_api
from backend_ui.monitoring import register_metrics
from backend_ui.security import jwt_required
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
CORS(app)
app.register_blueprint(morphing_api, url_prefix='/api')
register_metrics(app)

@app.route('/')
def index():
    return '<h1>IndiMorph Backend API</h1>'

if __name__ == '__main__':
    log_handler = RotatingFileHandler('indimorph_backend.log', maxBytes=10*1024*1024, backupCount=5)
    log_handler.setLevel(logging.INFO)
    app.logger.addHandler(log_handler)
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port, debug=False) 