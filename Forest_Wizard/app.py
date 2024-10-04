from flask import Flask, request, jsonify, render_template
import requests
import json
import os 
import nltk
from flask_wtf.csrf import CSRFProtect

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# progress bar
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from tqdm import tqdm

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#- Natural Language Processing (NLP) specific libs
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer  # A word stemmer based on the Porter stemming algorithm.  Porter, M. "An algorithm for suffix stripping." Program 14.3 (1980): 130-137.
from nltk import sent_tokenize, word_tokenize, PorterStemmer
from nltk.corpus import stopwords
import time
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#- Required to load necessary files to support NLTK
#- NLTK required resources
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("words")
nltk.download('punkt_tab')
#nltk.download("all")  #<- Only do this if you want the full spectrum of all possible packages, it's a LOT!

stemmer = PorterStemmer()

# Noun Part of Speech Tags used by NLTK
# More can be found here
# http://www.winwaed.com/blog/2011/11/08/part-of-speech-tags/
NOUNS = ['NN', 'NNS', 'NNP', 'NNPS']
VERBS = ['VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ']


app = Flask(__name__)

app.secret_key  = os.getenv('secret_key')
csrf = CSRFProtect()
csrf.init_app(app)

api_key = os.getenv('OPENAI_API_KEY') 

if not api_key:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

Ocp_Apim_Subscription_Key = os.getenv('APIM_SUBSCRIPTION_KEY')
if not Ocp_Apim_Subscription_Key:
    raise ValueError("No Ocp_Apim_Subscription_Key found. Please set the APIM_SUBSCRIPTION_KEY environment variable.")



Prompt_pre_user = 'Answer only about the forest service, if the question is not about the forest service answer it in a way to relate it to the forest service. Do not provide any personal information. Do not provide any medical advice. Do not provide any legal advice. Do not provide any financial advice. Do not provide any professional advice. Do not provide any emergency services. Do not provide any crisis services. Do not provide any support for self. '

is_file = True

tokens_in_files = 0
token_limit = 7000

temp_filtered_list =[]
###########################################
#- Demonstrate use of tokens and stopwords
###########################################
def tokenize_and_stopwords(data):
    response=sent_tokenize(data)
    print(f"There are {len(response)} sentences.")

    response=word_tokenize(data)
    print(f"There are {len(response)} words.")
    stop_words = set(stopwords.words("english"))
    filtered_list = []

    response=word_tokenize(data.lower())
    wordlist = [x for x in response if (len(x)>=2 and x.isalpha())]

    for word in tqdm(wordlist):
        if word.casefold() not in stop_words:
            filtered_list.append(word)

    print("\n")
    print(f"There are {len(filtered_list)} remaining words after cleaning them up.")
    return filtered_list

#####################################
#####################################
#OpenAI APIM API call

#####################################
#####################################

def make_post_request_pipeline(json_body):
    """
    Makes a POST request to the specified AI APIM endpoint with the given JSON body.

    Args:
        json_body (dict): The JSON body to be sent in the request.

    Returns:
        dict: The response JSON if the request is successful, otherwise an error dictionary with the error message and response text.
    """
    for message in json_body['messages']:
        if message['role'] == 'user':
            temp = message['content']
            message['content'] = Prompt_pre_user + temp

    headers = {'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key, 'Content-Type': 'application/json'}
    api_url = 'https://apim-com-nonprd-poc.azure-api.net/ai-pipeline/onepromt/v1/BASE2-gpt-35-turbo?api-version=2024-02-15-preview'

    try:
        response = requests.post(api_url, headers=headers,  data=json.dumps(json_body))
        return response.json()
    except Exception as e:
        return {"error": "An error occurred: " + str(e)}



#pipeline chat endpoint
@app.route('/ai/pipeline/chat', methods=['POST'])
def chat_pipeline():
    json_body = request.get_json()

    #call helperfunction to make api call
    response = make_post_request_pipeline(json_body)
    

     
    if 'choices' in response:
        #return response, just the content
        content = response['choices'][0]['message']['content']
        return jsonify(content)
    else:
         #if error return the whole response

        return jsonify(response)

#####################################
#####################################
#OpenAI API call
##################################### 
#####################################


def make_post_request_openai(json_body):
    if(is_file):
        time.sleep(1)
    """
    Makes a POST request to the specified openAI endpoint with the given JSON body.

    Args:
        json_body (dict): The JSON body to be sent in the request.

    Returns:
        dict: The response JSON if the request is successful, otherwise an error dictionary with the error message and response text.
    """
    global temp_filtered_list
    if json_body is None:
        print("Error: json_body is None")
        return {"error": "json_body is None"}
    for message in json_body['messages']:
        if message['role'] == 'user':
            temp = message['content']
            message['content'] = Prompt_pre_user + temp

            message['content'] = message['content'] + ' '.join(temp_filtered_list)
    headers = {'Content-Type': 'application/json'}
    api_url = 'https://oai-nonprd-openai-poc-01.openai.azure.com/openai/deployments/BASE2-gpt-35-turbo/chat/completions?api-version=2024-02-15-preview&api-key='+api_key
    try:
        response = requests.post(api_url, headers=headers,  data=json.dumps(json_body))
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        return {"error": "An error occurred: " + str(e)}


@app.route('/openai/direct/chat', methods=['POST'])
def chat_openai():
    json_body = request.get_json()

    #call helperfunction to make api call
    response = make_post_request_openai(json_body)

    if 'choices' in response:
        #return response, just the content
        content = response['choices'][0]['message']['content']
        return jsonify(content)
    else:
        #if error return the whole response
        return jsonify(response)

#File reader endpoint for openai
@app.route('/openai/direct/chat/pdf', methods=['POST'])
def openai_read_file(): 
    global is_file
    global temp_filtered_list
    if request.method == 'POST':
        if 'file' in request.files:
            is_file = True
            file = request.files['file']
            if file:
                # Read the file data
                data = file.read()
                # Convert the data to string
                data = data.decode('utf-8')
                
                    
                data = tokenize_and_stopwords(data)
                temp_filtered_list = data

                is_file= False
                return 'testing'
        is_file = False
        return 'No file found'
    is_file= False 
    return 'No file found'



#landing page
@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)