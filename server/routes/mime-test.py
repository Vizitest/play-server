from flask import request, send_from_directory
from server.app import app
from server.constants import CONTENT_TYPE_JSON
import json


@app.route('/mime-test/<path:mimetype>', methods=['GET'])
def mime_test(mimetype: str):
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

    if mimetype in sample_files:
        return send_from_directory("static", sample_files[mimetype])

    return json.dumps({"error": "No sample is available for this mimetype"}), 404, CONTENT_TYPE_JSON
