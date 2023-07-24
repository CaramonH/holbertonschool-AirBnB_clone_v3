import os
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage():
  """Closes the storage engine."""
  storage.close()

if __name__ == '__main__':
  host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
  port = os.environ.get('HBNB_API_PORT', 5000)
  app.run(host=host, port=port, threaded=True)
