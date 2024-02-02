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

    if mimetype == 'image':
#         return url_for('static', filename='test.png'), 200, CONTENT_TYPE_IMAGE_PNG
        return 'https://picsum.photos/200/300', 200, CONTENT_TYPE_IMAGE_PNG

    if mimetype == 'audio':
       return url_for('static', filename='audio.mp3'), 200, CONTENT_TYPE_AUDIO_MPEG

    if mimetype == 'video':
       return url_for('static', filename='video.mp4'), 200, CONTENT_TYPE_VIDEO_MP4

    if mimetype == 'youtube':
       return 'https://www.youtube.com/watch?v=j41bb5LdA5U', 200, CONTENT_TYPE_VIDEO_MP4

    if mimetype == 'text':
       return send_from_directory("static", 'test.txt'), 200, CONTENT_TYPE_PLAIN_TEXT

    if mimetype == 'html':
       return send_from_directory("static", 'test.html'), 200, CONTENT_TYPE_HTML

    if mimetype == 'json':
       return send_from_directory("static", 'test.json'), 200, CONTENT_TYPE_JSON

    return json.dumps({"error": "No sample is available for this mimetype"}), 404, CONTENT_TYPE_JSON
