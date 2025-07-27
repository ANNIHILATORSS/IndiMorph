from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Response

morph_requests = Counter('morph_requests_total', 'Total morph requests')
reset_requests = Counter('reset_requests_total', 'Total reset requests')
status_requests = Counter('status_requests_total', 'Total status requests')


def register_metrics(app):
    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST) 