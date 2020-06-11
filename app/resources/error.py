from flask import jsonify
from application import app

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404"""
    
    message = {"error": "Invalid URL"}
    resp = jsonify(message)
    resp.status_code = 404
    return resp