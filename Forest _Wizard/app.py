from flask import Flask, request, jsonify, render_template
import requests
import json
import os

app = Flask(__name__)
api_key = os.getenv('OPENAI_API_KEY')
Ocp_Apim_Subscription_Key = '5bbf6c102d86484c818aba9d18588962'

#helper function to make call to the api
def make_post_request(json_body):
    """
    Makes a POST request to the specified API endpoint with the given JSON body.

    Args:
        json_body (dict): The JSON body to be sent in the request.

    Returns:
        dict: The response JSON if the request is successful, otherwise an error dictionary with the error message and response text.
    """
    
    #direct call to llm api
    #headers = {'Content-Type': 'application/json'}
    #api_url = 'https://oai-nonprd-openai-poc-01.openai.azure.com/openai/deployments/BASE2-gpt-35-turbo/chat/completions?api-version=2024-02-15-preview&api-key='+api_key

    #call to api pipeline
    headers = {'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key, 'Content-Type': 'application/json'}
    api_url = 'https://apim-com-nonprd-poc.azure-api.net/ai-pipeline/onepromt/v1/BASE2-gpt-35-turbo?api-version=2024-02-15-preview'

    try:
        response = requests.post(api_url, headers=headers,  data=json.dumps(json_body))
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Request failed with status code: " + str(response.status_code), "response": response.text}
    except Exception as e:
        return {"error": "An error occurred: " + str(e)}

#landing page
@app.route('/')
def home():
    return render_template('index.html')


#chat endpoint
@app.route('/api/chat', methods=['POST', 'GET'])
def chat():
    json_body = request.get_json()

    #call helperfunction to make api call
    response = make_post_request(json_body)

    #return response, just the content 
    content = response['choices'][0]['message']['content']
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)
