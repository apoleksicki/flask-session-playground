from flask import Flask, Response, request, session
from flask_session import Session


app = Flask(__name__)

SESSION_TYPE = 'mongodb'

SESSION_MONGODB_DB = 'screen'
SESSION_MONGODB_COLLECT = 'sessions'

app.config.from_object(__name__)

Session(app)


@app.route('/create-session', methods=['POST'])
def create_session() -> Response:
    session['val'] = request.json
    return Response(status=201)


@app.route('/session-data')
def get_session_data() -> dict:
    return session['val']
