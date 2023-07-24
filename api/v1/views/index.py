from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
  """Returns the status of the API."""
  status_code = 200
  status_message = "OK"
  return jsonify({
    "status_code": status_code,
    "status_message": status_message
  })