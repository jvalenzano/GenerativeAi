#!/usr/bin/env python
# coding: utf-8

# # Sentiment Analysis using Gemini, Llama3, and OpenAI
# ## EMC Comments Analysis
# ### 003 - Data Comments, Analysis, 1 to N Coded Comments
# 
# Read in pre-saved coded comments and attempt extraction of comments comparing to coded comments.
# 
# ### TODO
# + None
# 
# ### Version History
# + v0.1 - General access, no cleansing of data, df.apply() for OpenAI API call.  Gaps in data output.
# + v0.2 - Same dataset (Sonya Sachedeva), robust cleansing, lemmatizing, and stemming.  Summary of summary for token limit solved.
# + v0.3 - Added prompt defense, PII defense, df.apply() with defensive method, dropping lemmatizing/stemming.  Added libraries such as commonregex, spacy, and transformers.
# + v0.4 - Broke into data processing versus data prepping functions.
# + v0.5 - Moved core code into "main" to support multi-processing in future, backed up original data to 'Letter Text_ORIGINAL', explored multi-processing and GPU utilization.
# + v0.6 - New dataset to process direct from CARA extract.  Sonya Sachedeva's data inputs processed with v0.5 which has been tagged.
# + v0.7 - Added embeddings, added read of coded comments and save to binary file, started analysis of Coded Comments

# In[192]:


# -*- coding: utf-8 -*-


# ### Environment Validation
# 
# Using GCP or Azure read in arrays representing minimal library requirements (which might not be present in a Google Colab environment) and install / load the libraries as required.  Additional imports for standard libraries and tailored content to follow.

# In[193]:


###########################################
#- Minimal imports to start
###########################################
try:
    import sys
    import subprocess
    import importlib.util
    import atexit
except ImportError as e:
    print("There was a problem importing the most basic libraries necessary for this code.")
    print(repr(e))
    raise SystemExit("Stop right there!")

###########################################
#- Final Exit Routine
###########################################
@atexit.register
def goodbye():
    print("GOODBYE")

###########################################
#- Cloud Environment Setup (Priming)
###########################################
# variables establishing environments
ENV_GCP=0
ENV_AZURE=1
user_input=-1
environments=["GCP", "Azure"]
    
#prompt user for environment before continuing
user_input = 0
while True:
  try:
     if user_input > -1:
         break;
     user_input = int(input("Select the environment you're running: (0) GCP (1) Azure"))     
     if user_input > 1:
         print("Not a valid choice, please try again.")
         continue;
  except ValueError:
     print("Not a valid choice, please try again.")
     continue
  else:
     print(f"Environment selected is: {environments[user_input]}")
     break 
        
############################################
#- Import a custom library, in this case a fairly useful logging framework
############################################
from pathlib import Path
debug_lib_location = Path("../ML-Support")
sys.path.append(str(debug_lib_location))
import debug

libraries=["transformers", "langchain", "backoff","python-dotenv", "openai", "unidecode", 
           "alive-progress", "tqdm", "pyspellchecker", "wordcloud", "langchain", "icecream", "numba", 
           "fitz","dataclasses", "commonregex", "transformers", "spacy", "PyMuPDF", "PyPDF2", "pdfminer", 
           "pdfplumber","pdf2image","pytesseract"]    
debug.msg_info(f"Validating environment for the following pip packages: {libraries}")

#load environment for non-generative libraries
try:
    for library in libraries:
      if library == "Pillow":
        spec = importlib.util.find_spec("PIL")
      else:
        spec = importlib.util.find_spec(library)
      if spec is None:
        print("...installing library " + library)
        subprocess.run(["pip", "install" , library, "--quiet"])
      else:
        print("...library " + library + " already installed.")
except (subprocess.CalledProcessError, Exception) as e:
    print("Error: Failed to install required packages, your code might not run properly.")
    print(repr(e))

#load environment specific libraries for generative AI.
try:    
    if environments[user_input]=="GCP":
      subprocess.run(["pip", "install" , "--upgrade", "google-cloud-aiplatform", "--quiet"])
      subprocess.run(["pip", "install" , "--upgrade", "google-cloud-secret-manager", "--quiet"])
      gcp_libraries=["google-generativeai","google.protobuf", "google.generativeai", "google.cloud.aiplatform_v1beta1",]
      for library in gcp_libraries:
        spec = importlib.util.find_spec(library)
        if spec is None:
          print("...installing library " + library)
          try:
              subprocess.run(["pip", "install" , library, "--quiet"])
          except (subprocess.CalledProcessError, Exception) as e:
              print("Error: Failed to install required packages, your code might not run properly.")
              print(repr(e))
        else:
          print("...library " + library + " already installed.")
    
        from google.cloud import aiplatform
        import vertexai.preview
        import vertexai
        import openai
        from google.auth import default, transport
        from google.cloud import secretmanager
        import google.generativeai as genai
        from vertexai.preview.generative_models import GenerativeModel
        from vertexai.preview.generative_models import GenerationConfig
        from google.cloud.aiplatform_v1beta1.types.openapi import Schema
        from google.cloud.aiplatform_v1beta1.types.openapi import Type
        from google.protobuf.json_format import MessageToDict        
    elif environments[user_input]=="Azure":
      azure_libraries=["openai", ]
      for library in azure_libraries:
        spec = importlib.util.find_spec(library)
        if spec is None:
          print("...installing library " + library)
          try:
              subprocess.run(["pip", "install" , library, "--quiet"])
          except (subprocess.CalledProcessError, Exception) as e:
              print("Error: Failed to install required packages, your code might not run properly.")
              print(repr(e))
        else:
          print("...library " + library + " already installed.")
    else:
        print("There was a problem processing your request.  Only numeric input of 0 or 1 is allowed.")
        print("Continued operations is not possible without the proper installed tools.")
        raise SystemExit("Stop right there!")
except Exception as e:
    print("There was a problem processing library installs for Generative AI libraries")
    print(repr(e))
    raise SystemExit("Stop right there!")

debug.msg_debug("...dynamic environment installs complete.")


# ## Includes and Libraries

# In[194]:


debug.msg_info("Library imports")    
############################################
# INCLUDES
############################################

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# a set of libraries that perhaps should always be in Python source
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
debug.msg_debug("...core libraries.")
import os
import datetime
import gc
import socket
import sys
import getopt
import inspect
import traceback
import warnings
import json
import pickle
from pathlib import Path
import itertools
import datetime
import re
import shutil
import string
from io import StringIO
import tqdm


import io
import math
import textwrap
import random
import glob
import time
from time import perf_counter
import subprocess
import backoff
from dotenv import load_dotenv
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Function Profiling
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import cProfile
import pstats
import io
from pstats import SortKey

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Data Science Libraries
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
debug.msg_debug("...classic data science libraries.")

#optimization routines
from numba import jit
import numpy as np
import scipy as sp
#from sklearn.linear_model import LinearRegression


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Additional libraries for this work
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
debug.msg_debug("...application specific libraries.")
import math
from base64 import b64decode
from IPython.display import Image
import requests
from bs4 import BeautifulSoup                 #used to parse the text
from wordcloud import WordCloud, STOPWORDS    #custom library specifically designed to make word clouds
from spellchecker import SpellChecker
import fitz
#to handle strange characters
from unidecode import unidecode 

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Graphics
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
debug.msg_debug("...graphics.")
#import PIL
from PIL import Image
import PIL.ImageOps
import matplotlib as matplt
import matplotlib.pyplot as plt

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# progress bar
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
debug.msg_debug("...progress bars.")
from alive_progress import alive_bar
#from alive_progress.styles import showtime, Show
from tqdm.notebook import trange, tqdm
#from tqdm import trange, tqdm

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#- PII libraries (regular expressions)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
debug.msg_debug("...regular expressions for PII and transformers for prompt injection defense.")
from commonregex import CommonRegex
from commonregex import email
from commonregex import time
from commonregex import credit_card
from commonregex import ip
from commonregex import ipv6
from commonregex import link
from commonregex import phone
from commonregex import street_address
from commonregex import btc_address

debug.msg_debug("...spacy (pii defense).")
import spacy
from spacy.language import Language
from spacy.tokens import Doc

debug.msg_debug("...hugging face model support.")
#injection defense
from transformers import pipeline

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#- Tensorflow AI/ML libraries (seek to use GPU's)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#load first
try:
    debug.msg_debug("...TensorRT")    
    import tensorrt
    assert tensorrt.Builder(tensorrt.Logger())
except ImportError as ie:
    debug.msg_warning("Failed to import tensorrt, this might be a problem if trying for enhanced processing.")
    debug.msg_warning(f"...{repr(ie)}")
    pass

try:
    #load second
    debug.msg_debug("...TensorFlow")        
    import tensorflow as tf
except ImportError as ie:
    debug.msg_warning("Failed to import tensorflow, might not have a GPU or the proper environment loaded")
    debug.msg_warning(f"...{repr(ie)}")
    pass

try:
    debug.msg_debug("...CUDF")    
    import cudf
except ImportError as ie:
    debug.msg_warning("Failed to import cudf, likely don't have a GPU")
    debug.msg_warning(f"...{repr(ie)}")
    pass

try:
    debug.msg_debug("...Torch")    
    import torch
except ImportError as ie:
    debug.msg_warning("Failed to import torch, likely don't have a GPU or access to that library.")
    debug.msg_warning(f"...{repr(ie)}")
    pass

import pandas as pd
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#- NLTK required resources
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
debug.msg_debug("...natural language processing.")
import nltk
from nltk.stem import PorterStemmer  # A word stemmer based on the Porter stemming algorithm.  Porter, M. "An algorithm for suffix stripping." Program 14.3 (1980): 130-137.
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tree import tree
#from nltk.book import *
from nltk import FreqDist
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords    

nltk.download('punkt')
nltk.download("words")
nltk.download("stopwords")
#nltk.download('averaged_perceptron_tagger')      #looks like you have to download select neural layers for specific functions, head to read the erorr output to learn this.


# ## Functions

# ### Numpy / Pandas Configuration Settings

# In[195]:


def set_library_configuration() -> None:
    
    ############################################
    #- JUPYTER NOTEBOOK OUTPUT CONTROL / FORMATTING
    ############################################
    #pandas set floating point to 4 places to things don't run loose
    debug.msg_info("Setting Pandas and Numpy library options.")    
    pd.set_option('display.max_colwidth', 10) # None if you want to view the full json blob in the printed dataframe, use this
    pd.options.display.float_format = '{:,.4f}'.format
    np.set_printoptions(precision=4)


# ## Functions

# ### Custom Exception Display

# In[196]:


## Manages exception output.
#  @param   (Exception)             - Exception to expound upon
#  @returns (None)                  - None
def process_exception(inc_exception) -> None:
    print(f"{BOLD_START}(Exception encountered):{BOLD_END} {type(inc_exception).__name__}")
    print(f"Details: {str(inc_exception)}")
    print("Traceback:")
    traceback.print_exc()


# In[197]:


def profile_function(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return result
    return wrapper


# ### Library Versioning Display

# In[198]:


## Outputs library version history of effort.
#
#  @returns (None)                  - None
def lib_diagnostics() -> None:

    import pkg_resources
    
    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}") 
    
    package_name_length=40
    package_version_length=20

    # Get installed packages
    the_packages=["cupy", "jupyter-core", "langchain", "langchain-core", "nltk", "numba", "numpy", "pandas", "pydantic", "pyspellchecker", "spacy", "scipy", "scikit-learn", "seaborn", "usaddress", "xarray",]
    the_packages.sort()
    
    installed_dict = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    installed=list(installed_dict.keys())
    installed.sort()
    
    #for package_idx, package_name in enumerate(installed):
    for idx, name in enumerate(installed):
         if name in the_packages:
             installed_version = installed_dict[name]
             print(f"{name:<40}#: {str(pkg_resources.parse_version(installed_version)):<20}")
   
    try:
        print(f"{'TensorFlow version':<40}#: {str(tf.__version__):<20}")
        print(f"{'     gpu.count:':<40}#: {str(len(tf.config.experimental.list_physical_devices('GPU')))}")
        print(f"{'     cpu.count:':<40}#: {str(len(tf.config.experimental.list_physical_devices('CPU')))}")
    except Exception as e:
        pass

    try:
        print(f"{'Torch version':<40}#: {str(torch.__version__):<20}")
        print(f"{'     GPUs available?':<40}#: {torch.cuda.is_available()}")
        print(f"{'     count':<40}#: {torch.cuda.device_count()}")
        print(f"{'     current':<40}#: {torch.cuda.current_device()}")
    except Exception as e:
        pass


    try:
      print(f"{'OpenAI Azure Version':<40}#: {str(the_openai_version):<20}")
    except Exception as e:
      pass

    print(f"{BOLD_START}List Devices{BOLD_END} #########################################")
    try:
      from tensorflow.python.client import device_lib
      print(device_lib.list_local_devices())
      print("")
    except RuntimeError as e:
      # Visible devices must be set before GPUs have been initialized
      print(str(repr(åe)))

    print(f"{BOLD_START}Devices Counts{BOLD_END} ########################################")
    try:
      print(f"Num GPUs Available: {str(len(tf.config.experimental.list_physical_devices('GPU')))}" )
      print(f"Num CPUs Available: {str(len(tf.config.experimental.list_physical_devices('CPU')))}" )
      print("")
    except RuntimeError as e:
      # Visible devices must be set before GPUs have been initialized
      print(str(repr(e)))

    print(f"{BOLD_START}Optional Enablement{BOLD_END} ####################################")
    try:
      gpus = tf.config.experimental.list_physical_devices('GPU')
    except RuntimeError as e:
      # Visible devices must be set before GPUs have been initialized
      print(str(repr(e)))

    if gpus:
      # Restrict TensorFlow to only use the first GPU
      try:
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print( str( str(len(gpus)) + " Physical GPUs," + str(len(logical_gpus)) + " Logical GPU") )
      except RuntimeError as e:
        # Visible devices must be set before GPUs have been initialized
        print(str(repr(e)))
      print("")
        
    debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}") 
    return


# #### Generic OpenAI Prompt for all Generative Queries

# In[199]:


## Iterates through data directory reading PDF's in target location (must be PD's and PDF's), returns hashmap (dictionary) of PD's
#
#  @param (System Prompt as String) - String - Designates instructions to AI.
#  @param (User Prompt as String)   - String - Designates request from user.
def genai_prompt(inc_system:str, inc_user:str, )-> str:

    resultant=""
    try:
        if environments[user_input]=="GCP":
            resultant=gcpgenai_prompt(inc_system, inc_user)
        else:
            resultant=openai_prompt(inc_system, inc_user)
    except Exception as e:
        resultant = {
          "Score": 0,
          "Strengths": "Error founding during generative execution, see weakness.",
          "Weaknesses": f"{repr(e)}",
         }
    finally:
        return resultant

    #debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")


# In[200]:


## Iterates through data directory reading PDF's in target location (must be PD's and PDF's), returns hashmap (dictionary) of PD's
#
#  @param (System Prompt as String) - String - Designates instructions to AI.
#  @param (User Prompt as String)   - String - Designates request from user.
#  @returns (String)                - Response from the AI in JSON format.
@backoff.on_exception(backoff.expo, Exception, max_tries=3)
def gcpgenai_prompt(inc_system:str, inc_user:str)-> str:

       
    resultant=""
    genai.configure(api_key=os.getenv("GEMINI_USFS_API_KEY"))
    
    try:
        # Using `response_mime_type` requires either a Gemini 1.5 Pro or 1.5 Flash model
        model = GenerativeModel(the_model, 
                                system_instruction='You are a resume assistant that reviews resumes for a Human Resources Department.',
                                )

        generation_config = {
            "max_output_tokens": model_max_token_response,
            "temperature": model_temperature,
            "top_p": model_top_p,
        
        }

        response = model.generate_content(
                                        contents=inc_system + " " + inc_user,
                                        generation_config=generation_config,
                                        stream=False,
                                        )

        resultant = response.text
        
    except Exception as e:
        #msg_debug.error(f"ERROR detected trying invoke the openai.ChatCompletion.create() call as follows: {str(e)}")
        resultant = {
          "Score": 0,
          "Strengths": "Error founding during generative execution, see weakness.",
          "Weaknesses": f"{repr(e)}",
         }
    finally:
        return resultant
   


# In[201]:


## Iterates through data directory reading PDF's in target location (must be PD's and PDF's), returns hashmap (dictionary) of PD's
#
#  @param (System Prompt as String) - String - Designates instructions to AI.
#  @param (User Prompt as String)   - String - Designates request from user.
#  @returns (String)                - Response from the AI in JSON format.
@backoff.on_exception(backoff.expo, Exception, max_tries=3)
def openai_prompt(inc_system:str, inc_user:str)-> str:

    resultant=""
    #debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")
    message_text = [
                    {"role":"system", "content": inc_system },
                    {"role":"user",   "content": inc_user }
                   ]
    
    ########################################
    #API Call
    ########################################
    try:
        completion = client.chat.completions.create(
              model=the_model,
              messages = message_text,
              temperature=model_temperature,
              max_tokens=model_max_token_response,
              top_p=model_top_p,
              frequency_penalty=model_frequency_penalty,
              presence_penalty=model_presence_penalty,
              stop=None
            )
        resultant=completion.choices[0].message.content

    except Exception as e:
        #msg_debug.error(f"ERROR detected trying invoke the openai.ChatCompletion.create() call as follows: {str(e)}")
        resultant = {
          "Score": 0,
          "Strengths": "Error founding during generative execution, see weakness.",
          "Weaknesses": f"{repr(e)}",
         }
    finally:
        return resultant

    #debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")


# In[202]:


def setup_gcpgenai_client():
    
    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")
 
    vertexai.init(project=PROJECT_ID, location=LOCATION)

    # Programmatically get an access token
    credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    auth_request = transport.requests.Request()
    credentials.refresh(auth_request)

    try:
        # # OpenAI Client
        client = openai.OpenAI(
            base_url=f"https://{LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{LOCATION}/endpoints/openapi",
            api_key=credentials.token,
        )
    except Exception as e:
        process_exception(e)
        raise ConnectionError(f"Failed to initialize OpenAI client for GCP: {e}")

    debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")

    return client


# In[203]:


def setup_openai_client():
    
    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")
    from openai import AzureOpenAI
    
    #model connection values for client
    debug.msg_debug("...gathering API key information.")
    try:
        the_endpoint=os.getenv("OPENAI_USFS_API_BASE")
        the_key=os.getenv("OPENAI_USFS_API_KEY")
        the_version=os.getenv("OPENAI_USFS_API_VERSION")
    except (Exception, KeyError) as e:
        process_exception(e)
        raise EnvironmentError(f"Missing environment variable: {e}")
        
    debug.msg_debug("...creating Azure client.")
    try:
        client = AzureOpenAI(
            azure_endpoint = the_endpoint,
            api_key = the_key,
            api_version=the_version,
        )
    except Exception as e:
        process_exception(e)
        raise ConnectionError(f"Failed to initialize OpenAI client for Azure: {e}")
        
    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")

    return client


# In[212]:


## Main selection of coded comments from generative solution
#
#  @param (pd.DataFrame) - Pass in Prepped Comments
def generate_generative_comments(inc_df : pd.DataFrame) -> pd.DataFrame:
    
    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")
    
    local_df = inc_df
    local_df["GenCodedText"]=""
    sub_comments=""
    
    ##########################################################
    #- Generative Summary (unaltered text)
    ##########################################################   
    debug.msg_debug("......generative comments")
    system_prompt="You are an expert text analyst with a keen eye for extracting valuable information."
    
    

    try:
        for idx, row in tqdm(local_df.iterrows(), total=local_df.shape[0]):

           user_prompt=f"""
Your task is to carefully examine the following body of text and identify 
the most important and relevant comments or statements. Focus on:

1. Actionable insights or recommendations

Please list these important elements in a clear, concise format. Ignore any irrelevant or redundant information. If the text contains multiple topics, organize your findings by theme.

Here's the text to analyze:{row.Text_Original}
                        """

#1. Key points that summarize main ideas
#2. Crucial facts or data
#3. Significant opinions or arguments
#4. Notable quotes      
#For each item you extract, briefly explain why it's significant in the context of the overall text. After listing the key elements, provide a brief summary (2-3 sentences) that #encapsulates the most critical takeaways from the text.
            
           try:
                resultant=genai_prompt(system_prompt,user_prompt)
           except Exception as e:
                debug.msg_error(f"Failed to execute sub-comment parsing for {row.LetterId}.")
                resultant=f"ERROR encountered: {str(e)}"
                process_exception(e)
                pass #continue processing, error logged
            
           #print("########################################################################################")
           #print(f"Sub-Comments for LetterId: {row.LetterId}")
           #print("########################################################################################")
           #print(resultant)
           #print()
           #print(f"{row.CodedText}")
           #print("########################################################################################")
            
           local_df.loc[idx,"GenCodedText"]=resultant
           #break;
            
    except Exception as e:
        process_exception(e)
    #finally:
    #    df[SOURCE_COLUMN_NAME].astype(str)
    
    return local_df
    
    debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")


# In[213]:


## Main read routine of 001 output
#
#  @param (pd.DataFrame)
def read_comments_data(inc_years:list) -> pd.DataFrame:

    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")

    #establish data version, aligned with code, 2020_CMTANL-0-7-0_EMC_Comments_001.bin
    data_version_release="-".join([str(VERSION_NAME), str(VERSION_MAJOR), str(VERSION_MINOR), str(VERSION_RELEASE)])        
    target_folder=DATA_DIR
    years=inc_years
    df=pd.DataFrame()
    total_records=0
    
    for year in years:
        target_filename=f"{target_folder}" + os.sep + f"{str(year)}_{data_version_release}"+"_EMC_Comments_001.bin"
        try:
            current_df = pickle.load(open(target_filename, "rb"))
        except (pickle.UnpicklingError, FileNotFoundError, IOError, Exception)  as e:
            debug.msg_warning("FAILED to unpickle the saved binary file, you might have corruption, investigate.")
            process_exception(e)

        try:
            debug.msg_debug(f"...{year} - {len(current_df):,}")
            if (len(df) > 0):
                df = pd.concat([df, current_df], axis=0)
            else:
                df = current_df
        except (Exception)  as e:
            debug.msg_warning("FAILED to concatenate pd.DataFrames, you might have corruption, investigate.")
            process_exception(e)
            raise IOError("File corruption or file not found.")

        total_records += len(current_df)
            
    debug.msg_debug(f"You read in {total_records:,} prepped comments.")     
    debug.msg_info(f"Exited {__name__} {inspect.stack()[0][3]}")

    return df



# In[214]:


## Main read routine of 001 output
#
#  @param (pd.DataFrame)
def read_coded_data(inc_years:list) -> pd.DataFrame:

    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")

    #establish data version, aligned with code, 2020_CMTANL-0-7-0_EMC_CodedComments_003.bin
    data_version_release="-".join([str(VERSION_NAME), str(VERSION_MAJOR), str(VERSION_MINOR), str(VERSION_RELEASE)])        
    target_folder=DATA_DIR
    years=inc_years
    df=pd.DataFrame()
    total_records=0
    
    for year in years:
        target_filename=f"{target_folder}" + os.sep + f"{str(year)}_{data_version_release}"+"_EMC_CodedComments_003.bin"
        try:
            current_df = pickle.load(open(target_filename, "rb"))
        except (pickle.UnpicklingError, FileNotFoundError, IOError, Exception)  as e:
            debug.msg_warning("FAILED to unpickle the saved binary file, you might have corruption, investigate.")
            process_exception(e)

        try:
            debug.msg_debug(f"...{year} - {len(current_df):,}")
            if (len(df) > 0):
                df = pd.concat([df, current_df], axis=0)
            else:
                df = current_df
        except (Exception)  as e:
            debug.msg_warning("FAILED to concatenate pd.DataFrames, you might have corruption, investigate.")
            process_exception(e)
            raise IOError("File corruption or file not found.")

        total_records += len(current_df)
            
    debug.msg_debug(f"You read in {total_records:,} coded comments.")     
    debug.msg_info(f"Exited {__name__} {inspect.stack()[0][3]}")

    return df



# In[215]:


def output_csv(inc_filename:str, inc_df: pd.DataFrame) -> None:
    
    output_filename=inc_filename
    debug.msg_debug(f"Saving the data to a file ({output_filename}).")
    inc_df.to_csv(output_filename, sep="^", header=True, index=False)
    


# In[216]:


def output_excel(inc_filename:str, inc_df: pd.DataFrame) -> None:
    
    output_filename=inc_filename
    debug.msg_debug(f"Saving the data to a file ({output_filename}).")
    with pd.ExcelWriter(inc_filename, mode='w') as writer:  
        inc_df.to_excel(writer)
    


# In[217]:


def output_data(data_version_release: str, inc_df:pd.DataFrame)-> None:
        #save to textual output
        target_directory=OUTPUT_DIR+os.sep+f"{data_version_release}"
        target_filename=f"{target_directory}/{data_version_release}" + "_output.csv"    
        try:
            if not os.path.isdir(target_directory):
                os.makedirs(target_directory)        
        except (IOError, Exception)  as e:    
            debug.msg_warning("FAILED to create the target directory ({target_directory}).")
            process_exception(e)
            raise SystemError

        try:
            output_csv(target_filename, inc_df)
        except (pickle.UnpicklingError, FileNotFoundError, IOError, Exception)  as e:    
            debug.msg_warning("FAILED to process the file, you might have corruption, investigate.")
            debug.msg_warning(f"...target output filename: {target_filename}")
            process_exception(e)

        target_filename=f"{target_directory}/{data_version_release}/{data_version_release}" + "_output.xlsx"    
        #save to MS Excel
        try:
            output_excel(target_filename, inc_df)
        except (pickle.UnpicklingError, FileNotFoundError, IOError, Exception)  as e:    
            debug.msg_warning("FAILED to process the file, you might have corruption, investigate.")
            debug.msg_warning(f"...target output filename: {target_filename}")            
            process_exception(e)
        


# In[218]:


## Main routine that executes all code, does return a data frame of data for further analysis if desired.
#
#  @param (pd.DataFrame)
def process(inc_years:list)-> None:

    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")
    #establish data version, aligned with code
    data_version_release="-".join([str(VERSION_NAME), str(VERSION_MAJOR), str(VERSION_MINOR), str(VERSION_RELEASE)])

    ############################################
    # Read Prepped Comments
    ############################################    
    master_comments_df=read_comments_data(inc_years)
    #print("DataFrame ########################################")
    #print(master_comments_df)
    #print("DataFrame Info ########################################")
    #print(master_comments_df.info())
    #print("DataFrame Describe ####################################")
    #print(master_comments_df.describe())
    
    print("")
    print("")
    
    ############################################
    # Read Prepped Coded Comments (Human selected)
    ############################################    
    master_coded_df=read_coded_data(inc_years)
    #print("DataFrame ########################################")
    #print(master_coded_df)
    #print("DataFrame Info ########################################")
    #print(master_coded_df.info())
    #print("DataFrame Describe ####################################")
    #print(master_coded_df.describe())
    
    #find discrete fields that have the "[comment*]" so we can pare-down the payload for comparison
    print(f"Length of original: {len(master_coded_df)}")
    master_coded_df = master_coded_df.query('CodedText.str.contains("\[comment")')
    print(f"Length of new: {len(master_coded_df)}")    

    print("")
    print("")
    
    ############################################
    # Merge Datasets
    ############################################
    result = pd.merge(master_comments_df, master_coded_df, on="LetterId")
    debug.msg_debug(f"You read in {len(result):,} merged records.")     
    #print("DataFrame ########################################")
    #print(result)
    print("DataFrame Info ########################################")
    print(result.info())
    print("DataFrame Describe ####################################")
    print(result.describe())

    master_df=generate_generative_comments(result)    
   
    output_data(data_version_release, master_df)
    
    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")    



# ## Main

# In[ ]:


if __name__ == "__main__":

    set_library_configuration()
    start_t=perf_counter()
    print("BEGIN PROGRAM")
    
    #with warnings.catch_warnings():
    # To ignore specific warning types:
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    warnings.filterwarnings('ignore', category=FutureWarning)
    warnings.filterwarnings('ignore', category=UserWarning)
    
    ############################################
    # SECRETS & ENV VARIABLES
    ############################################
    load_dotenv()
    
    ############################################
    # GLOBAL CONFIGURATION
    ############################################
    #used for values outside standard ASCII, just do it, you'll need it
    ENCODING  ="utf-8"
    os.environ['PYTHONIOENCODING']=ENCODING
    #spacy requirement
    os.environ['TOKENIZERS_PARALLELISM']="false"

    debug.msg_info("Variable declaration.")    
    ############################################
    # GLOBAL VARIABLES
    ############################################
    DEBUG = 1
    DEBUG_DATA = 0
    
    # CODE CONSTRAINTS
    VERSION_NAME    = "CMTANL"
    VERSION_MAJOR   = 0
    VERSION_MINOR   = 7
    VERSION_RELEASE = 0
    
    TEXT_WIDTH=77
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0;0m"
    
    ###########################################
    #- API Parameters for things like WordCloud
    ###########################################
    IMG_BACKGROUND=None                        #None without quotes or "black", "white", etc...
    IMG_FONT_SIZE_MIN=14
    IMG_WIDTH=800
    IMG_HEIGHT=600
    
    ############################################
    # APPLICATION VARIABLES
    ############################################
    PROJECT_ID= "usfs-gcp-rand-test-3"
    BUCKET_ID = "usfs-gcp-rand-test3-data-usc1"
    LOCATION = "us-central1"    
    SPELL_CHECK_DISTANCE=2
    MINIMUM_AI_RESPONSE=25                     #words
    MINIMUM_AI_WAIT=15                         #seconds
    os.environ["MINIMUM_AI_WAIT"] = "str(MINIMUM_AI_WAIT)"
    MINIMUM_LETTER_LENGTH=15
    SOURCE_COLUMNS_NAME=["Letter Text"]        #body of text where the actual comment is
    SOURCE_COLUMNS_IDX=[ 10 ]                   #location in data frame AFTER removal of columns
    SOURCE_COLUMN_NAME=SOURCE_COLUMNS_NAME[0]
    EVALUATION_RECORDS=10
    ERROR_PHRASE = 'Error code: 400'
    OPENAI_RESULT="ResultOPENAI"
    #DATA_DIR=f"/home/jupyter/projects/data/{BUCKET_ID}/source_data/nlp/{VERSION_NAME}"
    DATA_DIR=f"/home/jupyter/projects/gcs/source_data/nlp/{VERSION_NAME}"
    OUTPUT_DIR=f"/home/jupyter/projects/gcs/working_data/{VERSION_NAME}"
    DELIM="^"
    
    
    ############################################
    # GENERATIVE MODEL PARAMETERS
    ############################################
    the_model="unknown"
    model_temperature=0.0
    model_max_tokens=0
    model_max_token_response=0
    model_top_p=0.0
    model_frequency_penalty=0
    model_presence_penalty=0
    summary_token_max=0
    if environments[user_input]=="GCP":
        #model parameters
            #Gemini 1.5 Flash	google/gemini-1.5-flash-001 
            #Gemini 1.5 Prov	google/gemini-1.5-pro-001
            #Gemini 1.0 Prov	google/gemini-1.0-pro-002
            #                   google/gemini-1.0-pro-001
            #                   google/gemini-1.0-pro
        #the_model="gemini-1.5-pro-001"
        the_model="gemini-1.5-flash-001"
        model_temperature=0.7
        model_max_tokens=8000
        model_max_token_response=8000
        model_top_p=0.95
        model_frequency_penalty=0
        model_presence_penalty=0
        summary_token_max=150
    else:
        #model parameters
        the_model="gpt-35-turbo-16k"
        model_temperature=0.7
        model_max_tokens=8000
        model_max_token_response=2000
        model_top_p=0.95
        model_frequency_penalty=0
        model_presence_penalty=0
        summary_token_max=150
    
    ########################################
    #Safety filter settings for Google GenAI
    ########################################
    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
    ]    
   
    ############################################
    # GLOBAL CONFIGURATION
    ############################################
    os.environ['PYTHONIOENCODING']=ENCODING
    os.environ['TOKENIZERS_PARALLELISM']="false"
    
    ############################################
    #- Invocation of functions and instantiation of system needs, nltk instantiation
    ############################################   
    #setup the text wrapper
    debug.msg_debug(f"...Text Wrapper instantiated.")
    wrapper = textwrap.TextWrapper(width=TEXT_WIDTH)
    
    #show your libraries
    lib_diagnostics()
    
    ###########################################
    #- OPENAI
    # Generative AI Library Configuration
    # Tailored for OpenAI environment on Azure for now.  API keys and other relevant information in .bashrc_keys environment variable on system for security.
    ###########################################
    if environments[user_input]=="GCP":
        debug.msg_info("GCP GenAI setup")
        client=setup_gcpgenai_client()
    else:
        debug.msg_info("OPENAI setup")
        client=setup_openai_client()
    
    ############################################
    #Core routine
    ############################################
    #years=[2020, 2021, 2022, 2023, 2024]
    years=[2020]
    process(years)

    
    
    end_t=perf_counter()
    print("END PROGRAM")
    print(f"Elapsed time: {end_t - start_t}")


# In[ ]:




