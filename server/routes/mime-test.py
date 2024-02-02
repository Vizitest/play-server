from flask import request, send_from_directory
from server.app import app
from server.constants import *
import json
from flask import url_for


@app.route('/server/<namespace>/mime-test/<path:mimetype>', methods=['GET'])
def mime_test(namespace: str, mimetype: str):
    """
    This endpoint returns sample data for the given mimetype.
    """

    sample_files = {
        'application/json': 'test.json',
        'text/html': 'test.html',
        'text/plain': 'test.txt',
        'audio/mpeg': 'test.mp3',
        'image/png': 'test.png',
        'video/webm': 'test.webm'
    }

    if mimetype == 'image/png':
        return url_for('static', filename='test.png'), 200, CONTENT_TYPE_IMAGE_PNG

    if mimetype == 'audio/mpeg':
       return url_for('static', filename='test.mp3'), 200, CONTENT_TYPE_IMAGE_PNG

    if mimetype == 'video/webm':
       return url_for('static', filename='test.webm'), 200, CONTENT_TYPE_AUDIO_WEBM

    if mimetype in sample_files:
        return send_from_directory("static", sample_files[mimetype])

    return json.dumps({"error": "No sample is available for this mimetype"}), 404, CONTENT_TYPE_JSON
