import time
import os
from flask import Flask, Blueprint
from flasgger import Swagger
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__)

# Access swagger in endpoint /apidocs
Swagger(app)

bp = Blueprint('v1', __name__, template_folder='templates')

@bp.route('/time')
def get_current_time():
    """Example endpoint which returns the current time.
    ---
    responses:
      200:
        description: The current time in UNIX format
        examples:
          time: {'time': '12342.314'}
    """
    return {'time': time.time()}

app.register_blueprint(bp, url_prefix='/api/v1')



port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
