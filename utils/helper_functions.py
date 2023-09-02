def format_dialogflow_response(messages: list[str], output_contexts: list[dict] = 0) -> dict:
    response_data = {'fulfillmentMessages': []}
    for message in messages:
        response_data['fulfillmentMessages'].append(
            {
                'text': {
                    'text': [message]
                }
            }
        )
    if len(output_contexts) > 0:
        response_data['outputContexts'] = output_contexts
    return response_data
