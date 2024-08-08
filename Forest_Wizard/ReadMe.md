# Project Setup

To build the environment, the requirements are listed in the `requirements.txt` file. You can install them by running:

```bash
pip install -r requirements.txt
```
To start the Flask application, run:
```python
python app.py
```
## API Endpoint
The API endpoint can be changed in `app.py`. The api_url variable determines the API endpoint:
```python
   headers = {
    'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key,
    'Content-Type': 'application/json'
}
api_url = 'https://apim-com-nonprd-poc.azure-api.net/ai-pipeline/onepromt/v1/BASE-gpt-35-turbo?api-version=2024-02-15-preview'
```


## Authentication
The authentication is done thorugh APIM and is contained in the header for the post request

```python
    Ocp_Apim_Subscription_Key = '5bbf6c102d86484c818aba9d18588962'
```

To add a new endpoint, for example an endpoint to Vertex AI platform, ensure that the varible is being updated here in `def make_post_request(json_body)`

```python
    try:
        response = requests.post(api_url, headers=headers,  data=json.dumps(json_body))
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Request failed with status code: " + str(response.status_code), "response": response.text}
    except Exception as e:
        return {"error": "An error occurred: " + str(e)}
```
For the return value ensure that the response is being correclty extracted in `def chat()`

```python
    content = response['choices'][0]['message']['content']
    return jsonify(content)
```
# app.py documentation

This Python script uses the Flask framework to create a web application with two endpoints: a landing page and a chat API.

## Dependencies

- Flask
- requests
- json

## Global Variables

- `Ocp_Apim_Subscription_Key`: This is the authentication key used for making API calls.

## Functions

### make_post_request(json_body)

This function makes a POST request to a specified API endpoint with a given JSON body.

**Arguments:**

- `json_body` (dict): The JSON body to be sent in the request.

**Returns:**

- dict: The response JSON if the request is successful, otherwise an error dictionary with the error message and response text.

### home()

This function serves as the landing page of the web application. It renders the 'index.html' template.

### chat()

This function serves as the chat API endpoint. It accepts both POST and GET requests. It retrieves the JSON body from the request, makes an API call using the `make_post_request` function, and returns the content of the response.

## Execution

If this script is run as the main program, it starts the Flask application with debugging enabled.


# index.html documentation 

This is the main HTML file for a web application. It contains the HTML structure and JavaScript code for a chatbot user interface.

## Dependencies

- CSS stylesheet: /static/style.css
- jQuery library: https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js

## Structure

The chatbot UI consists of:

- An image at the top: /static/chatbot-ui-images/grey-content-top.png
- A chat widget with an input form for user input
- A popup window for displaying chatbot responses
- An image at the bottom: /static/chatbot-ui-images/grey-content-bottom.png

## JavaScript Functions

### submitChatForm

Handles the submission of the chat form and sends user input to the chat API.

### submitContinueForm

Handles the submission of the continue form in the popup window.

### hidePopup

Hides the popup window.

### showAskText

Shows or hides the "Ask me anything..." text based on user input.

## Note

The file paths for CSS stylesheets and images are relative to the web application's static directory.


