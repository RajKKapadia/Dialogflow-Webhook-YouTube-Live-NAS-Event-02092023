from flask import Flask, request, jsonify

from utils.action_handlers import default_welcome_intent

app = Flask(__name__)


@app.route('/')
def handle_home():
    return 'OK', 200


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    body = request.get_json()
    action = body['queryResult']['action']
    '''TODO
    (1) Separate the incoming requests by action name
    (2) Parameters
    (3) Go to the database/API pass the order numer
    (4) Get the response from the API
    (5) Set the respone
    '''
    if action == 'defaultWelcomeIntent':
        response_data = default_welcome_intent(body)
    return jsonify(response_data)
