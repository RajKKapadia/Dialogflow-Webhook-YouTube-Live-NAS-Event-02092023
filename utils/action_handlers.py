from utils.helper_functions import format_dialogflow_response

def default_welcome_intent(body: dict) -> dict:
    session = body['session']
    output_contexts = [
        {
            'name': f'{session}/contexts/await-name',
            'lifespanCount': 1
        },
        {
            'name': f'{session}/contexts/session-parameters',
            'lifespanCount': 100,
            'parameters': {
                'userName': 'abcd1234',
                'isActive': True
            }
        }
    ]
    response_data = format_dialogflow_response(
        [
            'Hi, this is a chatbot, powered by Dialogflow.',
            'Please provide your name.'
        ],
        output_contexts
    )
    return response_data
