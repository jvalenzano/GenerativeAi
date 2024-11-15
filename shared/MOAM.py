##############################################
#Imports
##############################################
#Ask Chris if he wants debug to be pulled in.
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
import openai

import io
import math
import textwrap
import random
import glob
import time
from time import perf_counter
import subprocess
from multiprocessing import Pool
import backoff                    #annotation to support repeat calls on api failure

import debug



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Function Profiling
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import cProfile
import pstats
import io
from pstats import SortKey

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MS Excel Libraries
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill, GradientFill
from openpyxl.styles import Border, Side
from openpyxl.styles import Alignment
from openpyxl.styles import Font

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Data Science Libraries
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#debug.msg_debug("...classic data science libraries.")

#optimization routines
from numba import jit
import numpy as np
import scipy as sp
#from sklearn.linear_model import LinearRegression


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Additional libraries for this work
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#debug.msg_debug("...application specific libraries.")
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
from dotenv import load_dotenv

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Graphics
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#debug.msg_debug("...graphics.")
#import PIL
from PIL import Image
import PIL.ImageOps
import matplotlib as matplt
import matplotlib.pyplot as plt

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# progress bar
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#debug.msg_debug("...progress bars.")
from alive_progress import alive_bar
#from alive_progress.styles import showtime, Show
from tqdm.notebook import trange, tqdm
#from tqdm import trange, tqdm

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#- PII libraries (regular expressions)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#debug.msg_debug("...regular expressions for PII and transformers for prompt injection defense.")
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

#debug.msg_debug("...spacy (pii defense).")
import spacy
from spacy.language import Language
from spacy.tokens import Doc
nlp = spacy.load("en_core_web_trf")
import en_core_web_trf

#debug.msg_debug("...hugging face model support.")
#injection defense
from transformers import pipeline

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#- Tensorflow AI/ML libraries (seek to use GPU's)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#load first
try:
   # #debug.msg_debug("...TensorRT")    
    import tensorrt
    assert tensorrt.Builder(tensorrt.Logger())
except ImportError as ie:
  #  #debug.msg_warning("Failed to import tensorrt, this might be a problem if trying for enhanced processing.")
 #   #debug.msg_warning(f"...{repr(ie)}")
    pass

try:
    #load second
    #debug.msg_debug("...TensorFlow")        
    import tensorflow as tf
except ImportError as ie:
    #debug.msg_warning("Failed to import tensorflow, might not have a GPU or the proper environment loaded")
    #debug.msg_warning(f"...{repr(ie)}")
    pass

# try:
#     #debug.msg_debug("...CUDF")    
#     #import cudf
# except ImportError as ie:
#     #debug.msg_warning("Failed to import cudf, likely don't have a GPU")
#     #debug.msg_warning(f"...{repr(ie)}")
#     pass

try:
    #debug.msg_debug("...Torch")    
    import torch
except ImportError as ie:
    #debug.msg_warning("Failed to import torch, likely don't have a GPU or access to that library.")
    #debug.msg_warning(f"...{repr(ie)}")
    pass

#debug.msg_debug("...Pandas")    
import pandas as pd
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#- NLTK required resources
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#debug.msg_debug("...natural language processing.")
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

############################################
# NLTK instantiation
############################################
#debug.msg_debug(f"...StopWords instantiated.")
stop_words = set(stopwords.words("english"))
#debug.msg_debug(f"...PortStemmer instantiated.")
stemmer = PorterStemmer()
#debug.msg_debug(f"...Lemmatizer instantiated.")
lemmatizer = WordNetLemmatizer()

SPELL_CHECK_DISTANCE=2
TEXT_WIDTH=77

    
#spell checker
spell = SpellChecker(distance=SPELL_CHECK_DISTANCE)
    
#setup the text wrapper
#debug.msg_debug(f"...Text Wrapper instantiated.")
wrapper = textwrap.TextWrapper(width=TEXT_WIDTH)
    
BOLD_START = "\033[1m"
BOLD_END = "\033[0;0m"


the_endpoint=os.getenv("OPENAI_USFS_API_BASE")
the_key=os.getenv("OPENAI_USFS_API_KEY")
the_version=os.getenv("OPENAI_USFS_API_VERSION")
openai.api_key = the_key
if the_endpoint:
    openai.api_base = the_endpoint
    if the_version:
        openai.api_base = f"{the_endpoint}/{the_version}"

        
###############################################################
# Helper functions
###############################################################
class BoundBox:
	def __init__(self, xmin, ymin, xmax, ymax, objness = None, classes = None):
		self.xmin = xmin
		self.ymin = ymin
		self.xmax = xmax
		self.ymax = ymax
		self.objness = objness
		self.classes = classes
		self.label = -1
		self.score = -1

	def get_label(self):
		if self.label == -1:
			self.label = np.argmax(self.classes)

		return self.label

	def get_score(self):
		if self.score == -1:
			self.score = self.classes[self.get_label()]

		return self.score
     

def _sigmoid(x):
	return 1. / (1. + np.exp(-x))

def process_exception(inc_exception) -> None:
    print(f"{BOLD_START}(Exception encountered):{BOLD_END} {type(inc_exception).__name__}")
    print(f"Details: {str(inc_exception)}")
    print("Traceback:")
    traceback.print_exc()

##############################################
# Helper FUnctions end
##############################################



##############################################
#data_clean
##############################################


def clean_date(inc_str: str) -> str:
    resumeText = re.sub('httpS+s*', ' ', inc_str)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub(r'\r', '', resumeText)
    resumeText = re.sub(r'\n', '', resumeText)
    resumeText = re.sub(' +', ' ', resumeText)  # remove extra whitespace
    resumeText = re.sub(r'\t', ' ', resumeText)  # remove tabs

    resumeText = resumeText.rstrip()
    resumeText = resumeText.lstrip()
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,.:;<=>?@[]^_`{|}~"""), ' ', resumeText)  # remove punctuations

    resumeText = re.sub(r'\W+', ' ', resumeText)
    resumeText = re.sub(' +', ' ', resumeText)
    return resumeText

def clean_json(inc_str: str) -> str:
    text = re.sub(r'\r', '', inc_str)
    text = re.sub(r'\n', '', text)
    text = re.sub(' +', ' ', text) # remove extra whitespace
    text = re.sub(r'\t', ' ', text) #remove tabs
    text.rstrip()
    text.lstrip()
    text = re.sub('[%s]' % re.escape("""#*'"""), ' ', text)  # remove punctuations
    return text

def clean_lemmatizer_words(inc_str:str) -> str:
    filtered_list = []
    response=word_tokenize(inc_str)
    wordlist = [x for x in response if (len(x)>=2 and x.isalpha())]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in wordlist]
    return str(' '.join(lemmatized_words))


def clean_stem_words(inc_str:str) -> str:
    filtered_list = []
    response=word_tokenize(inc_str)
    wordlist = [x for x in response if (len(x)>=2 and x.isalpha())]
    stemmed_words = [stemmer.stem(word) for word in wordlist]
    return str(' '.join(stemmed_words))

def clean_stop_words(inc_str:str) -> str:
    filtered_list = []
    response=word_tokenize(inc_str)
    wordlist = [x for x in response if (len(x)>=2 and x.isalpha())]
    for word in wordlist:
        if word.casefold() not in stop_words:
          filtered_list.append(word)
    return str(' '.join(filtered_list))

def clean_string(inc_str: str) -> str:
    """
    Function to clean generic text.
    
    @param inc_str: str - Incoming text without modification.
    @returns: str - Transformed text with extra spaces removed and cleaned.
    """
    text = re.sub(r'http\S+', ' ', inc_str)  # remove URLs
    text = re.sub(r'RT|cc', ' ', text)  # remove RT and cc
    text = re.sub(r'#\S+', '', text)  # remove hashtags
    text = re.sub(r'@\S+', '  ', text)  # remove mentions
    text = re.sub(r'\r', '', text)  # remove carriage returns
    text = re.sub(r'\n', '', text)  # remove newlines
    text = re.sub(r'\t', ' ', text)  # remove tabs

    text = text.strip()  # strip leading and trailing whitespace
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # remove punctuations
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])  # remove non-ASCII characters

    text = re.sub(r'\W+', ' ', text)  # remove non-word characters
    text = re.sub(r' +', ' ', text)  # remove extra whitespace again
    
    return text

  
def cleanse_string(inc_str: str) -> str:
    response=clean_string(inc_str)
    response=clean_stop_words(response)
    response=clean_stem_words(response)
    response=clean_lemmatizer_words(response)
    response=word_tokenize(response)
    return response

def cleanse_text(inc_text:str) -> str:
    resultant=inc_text.translate(str.maketrans('','',string.punctuation))
    resultant=str(resultant).rstrip('\\r\\n').lstrip("b'")
    resultant=str(resultant).strip('\\n')
    resultnat = re.search(resultant, '\n\n')
    return resultant

## Per string modification of data for cleansing purposes
#  Note: Could be improved to run multi-processing or in batches across the entire payload for greater optimization
#  @param    (inc_text)    - str    - String to modify (cleanse)
#  @param    (run_pii)     - bool   - Do you want to sweep the string for PII and replace PII with constants?
#  @param    (run_cleanse) - bool   - Do you want to sweep the string for non-standard characters and remove them?
#  @param    (run_lemm)    - bool   - Do you want to lemmatize the string?
#  @param    (run_stop)    - bool   - Do you want to remove stop words?
#  @param    (run_stem)    - bool   - Do you want to Stemm the words?
#  @returns  (str)         - str    - Modified content
def data_cleansing(
                   inc_text: str,
                   run_pii: bool,
                   run_cleanse: bool, 
                   run_lemm: bool, 
                   run_stop: bool,
                   run_stem: bool,
                   ) -> str:

    value = inc_text
    if run_pii:
        # clean the text of PII first since Spacy NER requires complete sentences with lexical relevance
        # removal of special characters can mangle attempts to clean the PII as well
        try:
            # #debug.msg_debug("......clean_pii")
            value = clean_pii(value)
        except Exception as e:
            # #debug.msg_warning("Unable to remove PII from the dataset.")
            process_exception(e)
            pass
            
    if run_cleanse:
        try:
            # #debug.msg_debug("......clean_text")
            value = clean_string(value)
        except Exception as e:
            # #debug.msg_warning("Unable to cleanse the string.")
            process_exception(e)
            pass

    if run_stop:
        try:
            # #debug.msg_debug("......clean_stop_words")            
            # note used SpaCy to clean up stop words and it was actually slower, using NLTK
            value = clean_stop_words(value)
        except Exception as e:
            # #debug.msg_warning("Unable to remove stop words from the string.")
            process_exception(e)
            pass

    if run_lemm:
        try:
            # #debug.msg_debug("......clean_lemmatizer_words")            
            # note used SpaCy to lemmatize and it was slower
            value = clean_lemmatizer_words(value)
        except Exception as e:
            # #debug.msg_warning("Unable to lemmatize the string.")
            process_exception(e)
            pass

    if run_stem:
        try:
            # #debug.msg_debug("......clean_stem_words")            
            value = clean_stem_words(value)
        except Exception as e:
            # #debug.msg_warning("Unable to stem the string.")
            process_exception(e)
            pass
    
    # check for NULLs again
    return value


import pandas as pd

def data_varacity_check(inc_dataframe: pd.DataFrame, source_column_name: str, minimum_letter_length: int) -> pd.DataFrame:
    """
    Function to clean the DataFrame by removing rows with insufficient text length and converting text to lowercase.

    :param inc_dataframe: pd.DataFrame - The input DataFrame.
    :param source_column_name: str - The name of the column containing the text data.
    :param minimum_letter_length: int - The minimum length of text required.
    :return: pd.DataFrame - The cleaned DataFrame.
    """
    ##############################################
    #- Rows that don't have sufficient length
    ##############################################
    # Convert all text to lower case first.
    inc_dataframe[source_column_name] = inc_dataframe[source_column_name].str.lower()
    
    try:
        # Print the number of rows that will be removed due to insufficient length
        print(f"Failed: {len(inc_dataframe.loc[(inc_dataframe[source_column_name].str.len() < (minimum_letter_length + 1))])}")
        
        # Filter the DataFrame to keep only rows with text length greater than minimum_letter_length
        df_new = inc_dataframe.loc[(inc_dataframe[source_column_name].str.len() > minimum_letter_length)]
        df = df_new
        
    except Exception as e:
        # Handle any exceptions that occur during the filtering process
        process_exception(e)
    
    return df

def decode_netout(netout, anchors, obj_thresh, net_h, net_w):
	grid_h, grid_w = netout.shape[:2]
	nb_box = 3
	netout = netout.reshape((grid_h, grid_w, nb_box, -1))
	nb_class = netout.shape[-1] - 5
	boxes = []
	netout[..., :2]  = _sigmoid(netout[..., :2])
	netout[..., 4:]  = _sigmoid(netout[..., 4:])
	netout[..., 5:]  = netout[..., 4][..., np.newaxis] * netout[..., 5:]
	netout[..., 5:] *= netout[..., 5:] > obj_thresh

	for i in range(grid_h*grid_w):
		row = i / grid_w
		col = i % grid_w
		for b in range(nb_box):
			# 4th element is objectness score
			objectness = netout[int(row)][int(col)][b][4]
			if(objectness.all() <= obj_thresh): continue
			# first 4 elements are x, y, w, and h
			x, y, w, h = netout[int(row)][int(col)][b][:4]
			x = (col + x) / grid_w # center position, unit: image width
			y = (row + y) / grid_h # center position, unit: image height
			w = anchors[2 * b + 0] * np.exp(w) / net_w # unit: image width
			h = anchors[2 * b + 1] * np.exp(h) / net_h # unit: image height
			# last elements are class probabilities
			classes = netout[int(row)][col][b][5:]
			box = BoundBox(x-w/2, y-h/2, x+w/2, y+h/2, objectness, classes)
			boxes.append(box)
	return boxes


def markdown_escaper(text: str, type: str = 'json'):
    escape_length = len(f'```{type}')
    if text[:escape_length] == f'```{type}' and text[-3:] == '```':
        return text[escape_length:-3]
    else:
        return text
    
def markdown_to_json(md: str):
    return json.loads(markdown_escaper(md))

##############################################
#data_clean end
##############################################


##############################################
# Utilty
##############################################

# MOAM.py

def get_full_version(version_name, version_major, version_minor, version_release):
    
    resultant = f"{version_name} v{version_major}.{version_minor}.{version_release}"
    return resultant

def get_version(version_major, version_minor, version_release):

    resultant = f"{version_major}.{version_minor}.{version_release}"
    return resultant


## Outputs library version history of effort.
#
#  @returns (None)                  - None
def lib_diagnostics() -> None:
        """
        Perform library diagnostics by checking the installed packages and their versions,
        as well as the availability of certain libraries like TensorFlow, Torch, and OpenAI.

        This function prints the diagnostic information to the console.

        Returns:
                None
        """
        import pkg_resources
        
        #debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}") 
        
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
                from openai import __version__ as the_openai_version
        except ImportError:
                the_openai_version = None

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
            print(str(repr(e)))

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
                
        #debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}") 
        return

import netCDF4 as nc
def lib_diagnostics():
    debug.msg_debug("System version    #:{:>12}".format(sys.version))
    netcdf4_version_info = nc.getlibversion().split(" ")
    debug.msg_debug("netCDF4 version   #:{:>12}".format(netcdf4_version_info[0]))
    debug.msg_debug("Matplotlib version#:{:>12}".format(matplt.__version__))
    debug.msg_debug("Numpy version     #:{:>12}".format(np.__version__))
    debug.msg_debug("Pandas version    #:{:>12}".format(pd.__version__))
    debug.msg_debug("SciPy version     #:{:>12}".format(sp.__version__))

    return

def printversion():

    print(get_full_version())

def printusage():

    print("")
    printversion()
    print("  -v, --version    prints the version of this software package.")
    print("")
    print("  * - indicates required argument.")

def set_library_configuration() -> None:
    ############################################
    #- JUPYTER NOTEBOOK OUTPUT CONTROL / FORMATTING
    ############################################
    #pandas set floating point to 4 places to things don't run loose
    debug.msg_info("Setting Pandas and Numpy library options.")    
    pd.set_option('display.max_colwidth', 10) # None if you want to view the full json blob in the printed dataframe, use this
    pd.options.display.float_format = '{:,.4f}'.format
    np.set_printoptions(precision=4)


def split_text(text, chunk_size) -> list[str]:
    
  """
  Splits the given text into chunks of approximately the specified chunk size.
  
  Args:
  text (str): The text to split.
  
  chunk_size (int): The desired size of each chunk (in characters).
  
  Returns:
  List[str]: A list of chunks, each of approximately the specified chunk size.
  """
  
  chunks = []
  current_chunk = StringIO()
  current_size = 0
  sentences = sent_tokenize(text)
  for sentence in sentences:
    sentence_size = len(sentence)
    if sentence_size > chunk_size:
      while sentence_size > chunk_size:
        chunk = sentence[:chunk_size]
        chunks.append(chunk)
        sentence = sentence[chunk_size:]
        sentence_size -= chunk_size
        current_chunk = StringIO()
        current_size = 0
    if current_size + sentence_size < chunk_size:
      current_chunk.write(sentence)
      current_size += sentence_size
    else:
      chunks.append(current_chunk.getvalue())
      current_chunk = StringIO()
      current_chunk.write(sentence)
      current_size = sentence_size
  if current_chunk:
     chunks.append(current_chunk.getvalue())
  return chunks


#  @param ([])      - list   - list of text chunked into a list
#  @param (int)     - int    - size of maximum tokens allowed for the model response
#  @param (str)     - str    - prompt used to ask the generative AI a question
#  @return ([])     - list   - responses from generative AI.
@backoff.on_exception(backoff.expo, Exception, max_tries=3)
def summarize(chunks, inc_max_tokens, prompt, the_model, model_temperature, model_top_p, model_frequency_penalty, model_presence_penalty) -> str:

  #debug.msg_debug("Entered summarize")
  summaries = []
  summary = ""
  for index,chunk in enumerate(chunks):
    completion_message=""
    resultant=""
     
    #print(f"...iteration:{index}")
    new_prompt=prompt+chunk
    #print(f"      in summarize(), length of prompt is: {len(new_prompt)}")

    ########################################
    #Model Invocation
    ########################################
    try:
        dynamic_message_text = [
                    {"role":"system", "content": "You are an experienced secretary that summarizes documents." },
                    {"role":"user",   "content": "Please summarize and extract relevant information from the following text:"  + new_prompt }
                   ]        

        
        completion_message = openai.chat.completions.create(
              model=the_model,
              messages = dynamic_message_text,
              temperature=model_temperature,
              #max_tokens=model_max_tokens,
              max_tokens=inc_max_tokens+len(new_prompt),
              top_p=model_top_p,
              frequency_penalty=model_frequency_penalty,
              presence_penalty=model_presence_penalty,
              stop=None
        )
        resultant=str(completion_message.choices[0].message.content)

    except Exception as oops:
      process_exception(f"Failed to invoke summarize with chat completion api call with following error ({str(oops)})")
      resultant=f"{oops}"      

    #print(f"        Summary length is:{len(resultant)}")

    summaries.append(resultant)
    #debug.msg_debug("Exited summarize")

  return ''.join(summaries)

##############################################
# Utilty end
##############################################

##############################################
# Security
##############################################

prompt_defense_model_chunk_size=512  

id2label = {
    'LEGIT':    False,
    'POSITIVE': False,
    'LABEL_1':  False,
    'SAFE':     False,
        
    'INJECTION':True,
    'NEGATIVE': True,
    'LABEL_0':  True,
    'UNSAFE':   True,
}

#  @param (Incoming String to Chop)    - str
#  @param (Chunk Size)                 - int
#  @returns ([])                       - list 
def prompt_injection_split_string(your_string, n) -> list[str]:
    return [your_string[i:i + n] for i in range(0, len(your_string), n)]


#  @param (Transformer Pipeline)    - pipeline - Mechanism via "transformer" library to read neural layer and execute evaluation on it.
#  @param (Text to Analyze, String) - str      - Actual input to evaluate.
#  @returns ({})                    - dict     - Results of neural processing, dictionary of true/false:% quality response
def prompt_injection_predict(inc_pipe, inc_prompt: str) -> dict:
    return {id2label[x['label']]: x['score'] for x in inc_pipe(inc_prompt)}




#  @param (Text to Analyze, String) - String - Actual input to evaluate.
#  @param (Models to Use)            - list   - List of models to use for evaluation.
#  @returns (String)                - String - Transformed string abstracting name of person.
def detect_PromptInjection(inc_prompt:str, the_models: list) -> bool:

    resultant=False
    offending_content=[]
    keywords=["ignore", "pretend" ]
    prompt_detected=[]
    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")

    try:
        chunk_size=prompt_defense_model_chunk_size
        chunks=prompt_injection_split_string(inc_prompt, chunk_size)
        for model_idx,model_name in enumerate(the_models):
            #debug.msg_debug(f"......processing model {PROMPT_INJECTION_MODELS[model_idx]}")
            the_models[model_idx].to(device=0)
            for chunk_idx, chunk_value in enumerate(chunks):
                the_answer=prompt_injection_predict(the_models[model_idx],str(chunk_value))
                #if an offending answer is found store it for future analysis.
                if (True in list(the_answer.keys())):
                    offending_content.append(chunk_value)
                prompt_detected.append(the_answer)
            #print(results)

    except Exception as e:
        process_exception(f"ERROR predict prompt injection as follows: {str(e)}")
        prompt_detected.append({False:100.0})

    for status in prompt_detected:
        for the_status in status.keys():
            if (the_status):
                resultant=True

    #debug.msg_debug(f"......evaluating keywords")
    wordlist=word_tokenize(inc_prompt.lower())
    for word in wordlist:
        if word in keywords:
            resultant=True

    #debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")
    return resultant, offending_content

##############################################
# Security end
##############################################


##############################################
# Replace   
##############################################

import fitz
from pdfminer.psparser import PSLiteral, PSKeyword
from pdfminer.utils import decode_text


def decode_value(value):

    response=""
    # decode PSLiteral, PSKeyword
    if isinstance(value, (PSLiteral, PSKeyword)):
        response = value.name

    # decode bytes
    if isinstance(value, bytes):
        response = decode_text(value)

    return response

##############################################
# Replace end
##############################################

##############################################
# Promt_support
##############################################

import google.generativeai as genai
from google.cloud.aiplatform_v1beta1.types.openapi import Schema
from google.cloud.aiplatform_v1beta1.types.openapi import Type
from vertexai.preview.generative_models import GenerativeModel

JSON_ERROR = ' { \
    "Sentiment": -999.0, \
    "SentimentConfidence": -999.0, \
    "Category": "error", \
}'

def create_gpt35_response_template(system_content: str, user_content: str, assistant_content: str) -> str:
    data = {
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content}
        ]
    }
    json_string=json.dumps(data)
    return(json_string)

def create_pcpf_response_template (prompt_content: str, completion_content: str) -> str:
    data={
        "prompt": prompt_content,
        "completion": completion_content,
    }
    json_string=json.dumps(data)
    return(json_string)


def gcpgenai_prompt_json(inc_system: str, inc_user: str, the_model: str, model_max_token_response: int, model_temperature: float, model_top_p: float) -> str:
    resultant = ""
    response = ""
    generation_config = {}
    genai.configure(api_key=os.getenv("GEMINI_USFS_API_KEY"))

    
    response_schema = Schema({
        "type_": Type.OBJECT,
        "properties": {
            "Score": {
                "type_": Type.STRING,
            },
            "Strengths": {
                'type_': Type.STRING,
            },
            "Weaknesses": {
                'type_': Type.STRING,
            },
        },
    })

    try:
        model = genai.GenerativeModel(
            model_name=the_model,
            system_instruction=inc_system,
        )

        generation_config = {
            "max_output_tokens": model_max_token_response,
            "temperature": model_temperature,
            "top_p": model_top_p,
            "response_mime_type": "application/json",
        }
    except Exception as e:
        print(f"Failed to setup generative query: {e}")
        resultant = json.dumps({"error": "Failed to setup generative query"})

    try:
        response = model.generate_content(
            contents=inc_system + " " + inc_user,
            generation_config=generation_config,
            stream=False,
        )

        resultant = response.text
    except Exception as e:
        print(f"Failed to execute generative query: {e}")
        resultant = json.dumps({"error": "Failed to execute generative query"})

    return resultant
   

@backoff.on_exception(backoff.expo, Exception, max_tries=3)
def gcpgenai_prompt(inc_system: str, inc_user: str, the_model: str, model_max_token_response: int, model_temperature: float, model_top_p: float)-> str:

    #debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")       
    resultant=""
    response=""
    generation_config={}
    genai.configure(api_key=os.getenv("GEMINI_USFS_API_KEY"))

    ########################################
    #API Call
    ########################################
    try:
        # Using `response_mime_type` requires either a Gemini 1.5 Pro or 1.5 Flash model
        model = GenerativeModel(the_model, 
                                system_instruction=inc_system,
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
        debug.msg_error(f"Failed to execute generative query in {__name__}")
        resultant = json.dumps(JSON_ERROR)

    #debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")
        
    return resultant

@backoff.on_exception(backoff.expo, Exception, max_tries=3)
def openai_prompt(inc_system: str, inc_user: str, the_model: str, model_temperature: float, model_max_token_response: int, model_top_p: float, model_frequency_penalty: float, model_presence_penalty: float, JSON_ERROR: dict) -> str:
    resultant = ""
    message_text = [
        {"role": "system", "content": inc_system},
        {"role": "user", "content": inc_user}
    ]
    
    ########################################
    # API Call
    ########################################

    try:
        completion = openai.chat.completions.create(
            model=the_model,
            messages=message_text,
            temperature=model_temperature,
            max_tokens=model_max_token_response,
            top_p=model_top_p,
            frequency_penalty=model_frequency_penalty,
            presence_penalty=model_presence_penalty,
            stop=None
        )
        resultant = completion.choices[0].message.content

    except Exception as e:
        debug.msg_error(f"Failed to execute generative query in {__name__}")
        resultant = json.dumps(JSON_ERROR)

    return resultant

def genai_prompt(inc_system:str, inc_user:str, inc_format:str,environments:str )-> str:

    #debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")    
    resultant=""
    try:
        if environments=="GCP":
            if inc_format=="json":
                resultant=gcpgenai_prompt_json(inc_system, inc_user)
            else:
                resultant=gcpgenai_prompt(inc_system, inc_user)
        else:
            resultant=openai_prompt(inc_system, inc_user)
    except Exception as e:
        debug.msg_error(f"Failed to execute generative query in {__name__}")
        resultant = JSON_ERROR
        
    #debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")
    
    return resultant

##############################################
# Promt_support end
##############################################


##############################################
# plot
##############################################

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

def plot_history(history):

  hist = pd.DataFrame(history.history)
  fig=plt.figure()
  fig.suptitle('model accuracy', fontsize=14)
  plt.plot(history.history['accuracy'])
  plt.plot(history.history['val_accuracy'])
  plt.ylabel('accuracy')
  plt.xlabel('epoch')
  plt.legend(['train', 'test'], loc='upper left')
  plt.show()
  #plt.savefig("./"+PROJECT_OUTPUT+"_"+str(ACTIVE_MONTH)+"_depth_" + str(daDepth) + "_LossVsEpoch.png")    
  plt.close()
    
  # summarize history for loss
  fig=plt.figure()
  fig.suptitle('model loss', fontsize=14)
  plt.plot(history.history['loss'])
  plt.plot(history.history['val_loss'])
  plt.ylabel('loss')
  plt.xlabel('epoch')
  plt.legend(['train', 'test'], loc='upper left')
  plt.show()    
  #plt.savefig("./"+PROJECT_OUTPUT+"_"+str(ACTIVE_MONTH)+"_depth_" + str(daDepth) + "_AccuracyVsEpoch.png")
  plt.close()


def summarize_diagnostics_seaborn(history, title):
  # Create pandas DataFrame
  df_history = pd.DataFrame(history.history)
  #print(df_history)

  #turn values into real percents
  df_history['Training_Accuracy'] = df_history["accuracy"] * 100.0
  df_history['Validation_Accuracy'] = df_history["val_accuracy"] * 100.0

  #color palette
  palette = ['r','b','g']

  # Plot using Seaborn
  sns.set_style("darkgrid", {"axes.facecolor": ".9"})
  sns.set_context("notebook", font_scale=1.0, rc={"lines.linewidth": 2.5})
  fig = plt.figure(figsize=[7,5])
  ax = plt.subplot(111)
  my_plot = sns.lineplot(data=df_history[["Training_Accuracy","Validation_Accuracy"]],
                         markers=True, dashes=False,palette=palette)

  my_plot.set_xlabel('Epochs')
  my_plot.set_ylim(0,100)
  my_plot.yaxis.set_major_formatter(mpl.ticker.PercentFormatter())
  my_plot.set_ylabel('Accuracy')

  plt.title('Training and Validation Loss \n' + title)
  ttl = ax.title
  ttl.set_weight('bold')


  plt.show()

##############################################
# plot end
##############################################


##############################################
# nre
##############################################

## Looks for EMAIL object identified by spacy and abstracts the input to a constant "EMAILADDR"
#  https://spacy.pythonhumanities.com/02_02_matcher.html#:~:text=How%20to%20use%20the%20spaCy%20Matcher%201%206.1.,...%205%206.5.%20Finding%20Quotes%20and%20Speakers%20
#  @param (Spacy Model for Parsing)         - Spacy Model
#  @param (Spacy Matcher for Email Pattern) - Spacy Matcher
#  @param (Text to Analyze, String)         - String - Actual input to evaluate.
#  @returns (String)                        - String - Transformed string abstracting email
def replace_email_spacy(inc_model, inc_matcher, inc_text) -> str:

    text_chunks=[]
    cleansed_text=inc_text
    if len(inc_text) > inc_model.max_length:
        chunks=int(round(len(inc_text)/inc_model.max_length))
        start=0
        end=inc_model.max_length
        for idx, chunk in enumerate(chunks):
            start=idx*inc_model.max_length
            end=(idx+1) * inc_model.max_length
            text_chunks.append(inc_text[start:end])
    else:
        text_chunks.append(inc_text)

    try:
        for idx, chunk in enumerate(text_chunks):
            doc=inc_model(chunk)
            matches = inc_matcher(doc)            
            for match in matches:
                cleansed_text = re.sub(f"{str(doc[match[0]:match[1]])}", f"EMAIL", cleansed_text)
    except Exception as e:
        debug.msg_warning(f"clean_email_spacy threw an exception: {repr(e)}")
        pass  #allow it to continue processing, we have other was of managing email
    
    return(cleansed_text)


def clean_named_entity_recognition(inc_model, inc_text) -> str:

    doc = inc_model(inc_text)
    #nec_labels=["PERSON", "ORG", "DATE", "TIME"]
    nec_labels=["PERSON"]

    text_chunks=[]
    cleansed_text=inc_text
    if len(inc_text) > inc_model.max_length:
        chunks=int(round(len(inc_text)/inc_model.max_length))
        start=0
        end=inc_model.max_length
        for idx, chunk in enumerate(chunks):
            start=idx*inc_model.max_length
            end=(idx+1) * inc_model.max_length
            text_chunks.append(inc_text[start:end])
    else:
        text_chunks.append(inc_text)

    try:
        for idx, chunk in enumerate(text_chunks):
            doc=inc_model(chunk)    
            for ent in doc.ents:
                if ent.label_ in nec_labels:
                    #msg_warning(f" Encountered NER {ent}")
                    cleansed_text = re.sub(f"{ent}", f"{str(ent.label_)}", cleansed_text)
    except Exception as e:
        debug.msg_warning(f"clean_named_entity_recognition threw an exception: {repr(e)}")
        pass  #continue processing regardless, we'll accept loss of some Person identification to keep the code processing
        
    return(cleansed_text)


nlp = spacy.load("en_core_web_trf")
import en_core_web_trf
def clean_named_entity_recognition(inc_text: str) -> str:

    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")

    nlp = en_core_web_trf.load()
    doc = nlp(inc_text)
    nec_labels=["PERSON", "ORG", "DATE", "TIME"]

    cleansed_text = inc_text
    for ent in doc.ents:
        if ent.label in nec_labels:
            cleansed_text = re.sub(f"{ent}", f" {str(ent.label)} ", cleansed_text)

    debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")
    
    return(cleansed_text)


def detect_address(inc_text: str, inc_model) -> str:
    address=""
    zipcode=""
    city=""
    state=""
    resultant=""
    #add_reg=address_pattern.search(inc_text)
    zip_reg=zip_code.search(inc_text)
    #if add_reg:
    #    address = add_reg.group()
    if zip_reg:
        zipcode = zip_reg.group()
        
    doc=inc_model(inc_text)
    for token in doc.ents:
        if token.label_ == "GPE":  # Geopolitical Entity (City)
            city = token.text
        elif token.label_ == "LOC":  # Location (State/Province)
            state = token.text
        elif token.label_ == "DATE":  # Postal Code
            if zipcode == "":
                zipcode = token.text

    try:
        usaddress_values=usaddress.tag(inc_text, tag_mapping={
           'PlaceName': 'city',
           'StateName': 'state',
        })
    except Exception as e:
        debug.msg_warning(f"ADDRESS processing encountered a problem: {str(e)}")
        pass
        #CGW, FIX, TODO, if you have too many identified components the API gets wonky.
        #Need to reduce tokens

    try:
        if city == "":
           city=usaddress_values[0]['city']
    except Exception as e:
        pass
    try:
        if state == "":
            state=usaddress_values[0]['state']
    except Exception as e:
        pass
    try:
        if zipcode == "":
            zipcode=usaddress_values[0]['zip_code']
    except Exception as e:
        pass

    resultant=", ".join([str(city),str(state),str(zipcode)])
    if len(resultant) > 3:
        return resultant
    else:
        return ""
    
import re
import usaddress


# Define the zip code regular expression
zip_code = re.compile(r'\b\d{5}(?:-\d{4})?\b')

def detect_address(inc_text: str, inc_model) -> str:
    address = ""
    zipcode = ""
    city = ""
    state = ""
    resultant = ""

    # Extract zip code using regex
    zip_reg = zip_code.search(inc_text)
    if zip_reg:
        zipcode = zip_reg.group()

    # Process the text with the NER model
    doc = inc_model(inc_text)
    for token in doc.ents:
        if token.label_ == "GPE":  # Geopolitical Entity (City)
            city = token.text
        elif token.label_ == "LOC":  # Location (State/Province)
            state = token.text
        elif token.label_ == "DATE":  # Postal Code
            if zipcode == "":
                zipcode = token.text

    try:
        usaddress_values = usaddress.tag(inc_text, tag_mapping={
            'PlaceName': 'city',
            'StateName': 'state',
        })
    except Exception as e:
        debug.warning(f"ADDRESS processing encountered a problem: {str(e)}")
        usaddress_values = [{}]
    try:
        if city == "":
            city = usaddress_values[0].get('city', "")
    except Exception as e:
        pass
    try:
        if state == "":
            state = usaddress_values[0].get('state', "")
    except Exception as e:
        pass
    try:
        if zipcode == "":
            zipcode = usaddress_values[0].get('ZipCode', "")
    except Exception as e:
        pass

    resultant = ", ".join([str(city), str(state), str(zipcode)])
    if len(resultant) > 3:
        return resultant
    else:
        return ""
    

def detect_locations(inc_prompt:str, inc_model) -> list[str]:
        
    loc_detected=[]
    resultant=set()

    try:
        chunk_size=prompt_defense_model_chunk_size
        chunks=prompt_injection_split_string(inc_prompt, chunk_size)
        for chunk_idx, chunk_value in enumerate(chunks):
            doc=inc_model(chunk_value)
            for token in doc.ents:
                if token.label_ in ["LOC", "GPE"]:  # Geopolitical Entity (City)
                    loc_detected.append(token.text)
    except Exception as e:
        process_exception(f"ERROR finding organizations as follows: {str(e)}")

    resultant |= set(loc_detected)
        
    return list(resultant)


def detect_organizations(inc_prompt:str, inc_model) -> list[str]:
            
    org_detected=[]
    resultant=set()
    
    try:
        chunk_size=prompt_defense_model_chunk_size
        chunks=prompt_injection_split_string(inc_prompt, chunk_size)
        for chunk_idx, chunk_value in enumerate(chunks):
            doc=inc_model(chunk_value)  
            for token in doc.ents:
                if token.label_ == "ORG":  # Geopolitical Entity (City)
                    org_detected.append(token.text)
    except Exception as e:
        process_exception(f"ERROR finding organizations as follows: {str(e)}")
    
    resultant |= set(org_detected)
    
    return list(resultant)

##############################################
# nre end
##############################################


##############################################
# pii
##############################################


def clean_pii(inc_input:str) -> str:

    #names, countris, locations, date, time
    cleansed_text=inc_input
    
    #other PII data transformed with regular expressions
    cleansed_text=re.sub(email, "EMAIL", cleansed_text)
    cleansed_text=re.sub(credit_card, "CREDITCARD", cleansed_text)
    cleansed_text=re.sub(link, "URL", cleansed_text)
    cleansed_text=re.sub(ip, "IP", cleansed_text)
    cleansed_text=re.sub(ipv6, "IPV6", cleansed_text)
    cleansed_text=re.sub(phone, "PHONENUMBER", cleansed_text)
    cleansed_text=re.sub(street_address, "STREETADDRESS", cleansed_text)
    cleansed_text=re.sub(btc_address, "BTCADDRESS", cleansed_text)

    cleansed_text=re.sub('^\d{5}(?:[-\s]\d{4})?$',"ZIPCODE",cleansed_text)
    cleansed_text=re.sub(' \d{5}(?:[-\s]\d{4})?'," ZIPCODE2",cleansed_text)
    cleansed_text=re.sub(' .. \d{5}. ',"ZIPCODE3",cleansed_text)
   
    
    return cleansed_text


##############################################
# pii end
##############################################

##############################################
# decode_pdf
##############################################

def read_pd_pdf(inc_filename:str) -> str:

    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")     
    try:
        if not ( os.path.isfile(inc_filename) ):
            print(f"ERROR detected, the input data file for work further in the notebook is missing.  Aborting execution.")
            print(f"  Resolve the {inc_filename} missing file and repeat.")
            raise SystemExit("Unable to continue without data.")
    except Exception as e:
        process_exception(f"ERROR detected trying detect the PDF path as follows: {str(e)}")

    doc = fitz.open(inc_filename)
    output = []
    total_text=""
          
    for page in doc:
        output += page.get_text("blocks")
        total_text=""
    
        for block in output:
             if block[6] == 0: # We only take the text
                  plain_text = str(unidecode(block[4]))
                  #handle hyphenations and slashes
                  plain_text = " ".join( plain_text.split("/") )
                  plain_text = " ".join( plain_text.split("-") )
                  #plain_text = clean_string(plain_text)
                  #total_text=total_text+ " " + cleanResume(plain_text)
                  total_text=" ".join([total_text, plain_text])

    debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}") 
    return total_text


def read_pdf(inc_filename:str) -> str:

    debug.msg_info(f"Entering {__name__} {inspect.stack()[0][3]}")  

    try:
        if not ( os.path.isfile(inc_filename) ):
            debug.msg_error(f"ERROR detected, the input data file for work further in the notebook is missing.  Aborting execution.")
            debug.msg_error(f"  Resolve the {inc_filename} missing file and repeat.")
            raise SystemExit("Unable to continue without data.")
    except Exception as e:
        process_exception(f"ERROR detected trying detect the PDF path as follows: {str(e)}")

    doc = fitz.open(inc_filename)
    output = []
    total_text=""
          
    for page in doc:
        output += page.get_text("blocks")
        
        previous_block_id = 0 # Set a variable to mark the block id
        total_text=""
    
        for block in output:
             if block[6] == 0: # We only take the text
                  #if previous_block_id != block[5]: # Compare the block number 
                  #    print("\n")
                  plain_text = str(unidecode(block[4]))
                  #handle hyphenations and slashes
                  plain_text = " ".join( plain_text.split("/") )
                  plain_text = " ".join( plain_text.split("-") )
                  #plain_text = clean_string(plain_text)
                  #total_text=total_text+ " " + cleanResume(plain_text)
                  total_text=" ".join([total_text, plain_text])

    debug.msg_info(f"Exiting {__name__} {inspect.stack()[0][3]}")  
    return total_text

##############################################
# decode_pdf end
##############################################


##############################################
# metrics
##############################################

def calculate_string_size(inc_string:str) -> int:
    response=int(len(word_tokenize(inc_string)))
    return response

def get_metrics(inc_df: pd.DataFrame, source_columns: list) -> None:
    for idx, name in enumerate(source_columns):
        mylist = []
        try:
            for the_string in tqdm(inc_df[name]):
                mylist.append(calculate_string_size(the_string))
        except Exception as e:
            process_exception(f"Unable to tokenize, and gather metrics for {name}...investigate, continuing: {str(e)}")
        
        arr = np.array(mylist)
        debug.msg_debug(f"Metrics on tokens for {name}.\n")
        debug.msg_debug(f"..records: {len(arr):>30,}")
        debug.msg_debug(f"......max: {np.max(arr):>30,}")
        debug.msg_debug(f"......avg: {int(np.average(arr)):>30,}")
        debug.msg_debug(f"......min: {np.min(arr):>30,}")
        debug.msg_debug("Analyze the result and ensure you have solid data.")

##############################################
# metrics end
##############################################