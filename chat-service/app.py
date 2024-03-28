from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
BASE_URL = 'https://oai-nonprd-openai-poc-01.openai.azure.com'

@app.route('/ai/chatbot/onepromt/v1/<deployment_id>', methods=['POST', "OPTIONS"])
def chat(deployment_id):
    received_body = request.json  # Assuming the body is in JSON format
    
    # Validate the received message format
    # if not validate_message_format(received_body):
    #     transform_payload(received_body)

    # Validate the prompt
    if not prompt_defense(received_body):
        return 'Invalid prompt detected', 400
    
    # Construct the API endpoint URL using the deployment ID
    api_endpoint = f'{BASE_URL}/openai/deployments/{deployment_id}/chat/completions'
    
    # Extract query parameters from the request URL
    api_params = request.args.to_dict()
    print(api_params)
    # Append query parameters to the endpoint URL
    if api_params:
        api_endpoint += '?' + '&'.join([f'{key}={value}' for key, value in api_params.items()])
        print(received_body)
    
    try:
        response = requests.post(api_endpoint, json=received_body)
        print(response.status_code)
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return 'Failed to send body to API endpoint', response.status_code
    except Exception as e:
        return f'Error occurred: {str(e)}', 500


def prompt_defense(received_body):
    # Placeholder for prompt defense logic
    return True



if __name__ == '__main__':
    app.run(debug=True)
