import time
import os
import uuid
from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
from flasgger import Swagger
from dotenv import dotenv_values
from firebase_admin import credentials, firestore, initialize_app

config = dotenv_values(".env")
url_prefix = "/api/v1"

app = Flask(__name__)

# Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
reminders_col = db.collection('reminders')

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

@bp.route('/add', methods=['POST'])
def create():
    """Add a remind to the database
    ---
    tags:
      - Reminds
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: remind
          type: "object"
          required:
            - remind
          properties:
            remind:
              type: string
              default: ""
    responses:
      200:
        description: The remind is inserted in the database
        schema:
          type: "object"
          properties:
            success:
              type: boolean
              default: true
      400:
        description: An error ocurred
    """
    try:
        data_to_add = request.json.copy()
        data_to_add["addedTime"] = datetime.utcnow().isoformat()
        reminders_col.document(str(uuid.uuid4())).set(data_to_add)
        return jsonify({"success": True}), 200

    except Exception as e:
        return f"An Error Occured: {e}", 400

@bp.route('/update', methods=['PUT'])
def update():
    """Modify a remind in the database
    ---
    tags:
      - Reminds
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: remindUpdate
          type: "object"
          required:
            - id
            - remind
          properties:
            id:
              type: string
              default: "383a40ae-5fad-46ba-8890-5d7e085ab697"
            remind:
              type: string
              default: ""
    responses:
      200:
        description: The remind is modified in the database
        schema:
          type: "object"
          properties:
            success:
              type: boolean
              default: true
      400:
        description: An error ocurred
    """
    try:
        data_to_modify = request.json.copy()
        del data_to_modify["id"]
        data_to_modify["modifyTime"] = datetime.utcnow().isoformat()
        reminders_col.document(request.json["id"]).update(data_to_modify)
        return jsonify({"success": True}), 200

    except Exception as e:
        return f"An Error Occured: {e}", 400

@bp.route('/delete', methods=['DELETE'])
def delete():
    """Delete a remind in the database
    ---
    tags:
      - Reminds
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: remindDelete
          type: "object"
          required:
            - id
          properties:
            id:
              type: string
              default: "383a40ae-5fad-46ba-8890-5d7e085ab697"
    responses:
      200:
        description: The remind is deleted in the database
        schema:
          type: "object"
          properties:
            success:
              type: boolean
              default: true
      400:
        description: An error ocurred
    """
    try:
        reminders_col.document(request.json["id"]).delete()
        return jsonify({"success": True}), 200

    except Exception as e:
        return f"An Error Occured: {e}", 400

@bp.route('/read')
def read():
    """Get all the reminds in the database
    ---
    tags:
      - Reminds
    responses:
      200:
        description: The remind is deleted in the database
        schema:
          type: "object"
          properties:
            success:
              type: boolean
              default: true
      400:
        description: An error ocurred
    """
    try:
      return jsonify([dict(doc.to_dict(), **{"id": doc.id}) for doc in reminders_col.stream()]), 200

    except Exception as e:
        return f"An Error Occured: {e}", 400

app.register_blueprint(bp, url_prefix=url_prefix)

port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
