import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import seaborn as sns
import matplotlib.pyplot as plt
import re
import MOAM
import os
import logging
import pandas as pd
import numpy as np
import json
from io import StringIO


import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords    


# Suppress TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0 = all logs, 1 = filter out INFO, 2 = filter out WARNING, 3 = filter out ERROR

# Configure logging to suppress warnings and errors
logging.getLogger('tensorflow').setLevel(logging.ERROR)

####################################################################################################
# Test cases for data_clean
####################################################################################################
class TestCleanDate(unittest.TestCase):

    def test_remove_urls(self):
        self.assertEqual(MOAM.clean_date("Check this link http://example.com"), "Check this link")  #the remove hastags only works on '#S...' if its #SN -> N
    def test_remove_hashtags(self):
        self.assertEqual(MOAM.clean_date("This is a #hashtag"), "This is a")

    def test_remove_mentions(self):
        self.assertEqual(MOAM.clean_date("Mentioning @user"), "Mentioning")

    def test_remove_newlines_and_carriage_returns(self):
        self.assertEqual(MOAM.clean_date("Line1\nLine2\rLine3"), "Line1Line2Line3")

    def test_remove_tabs(self):
        self.assertEqual(MOAM.clean_date("This\tis\ta\ttest"), "This is a test")

    def test_remove_extra_whitespace(self):
        self.assertEqual(MOAM.clean_date("This  is   a    test"), "This is a test")

    def test_remove_punctuations(self):
        self.assertEqual(MOAM.clean_date("Hello, world!"), "Hello world")

    def test_combined_cases(self):
        self.assertEqual(MOAM.clean_date("Check this link http://example.com #hashtag @user\nNew line\tTab!"), "Check this link New line Tab")
        
class TestCleanJson(unittest.TestCase):
    
    def test_remove_carriage_returns(self):
        self.assertEqual(MOAM.clean_json("Hello\rWorld"), "HelloWorld")
    
    def test_remove_newlines(self):
        self.assertEqual(MOAM.clean_json("Hello\nWorld"), "HelloWorld")
    
    def test_remove_extra_whitespace(self):
        self.assertEqual(MOAM.clean_json("Hello    World"), "Hello World")
    
    def test_remove_tabs(self):
        self.assertEqual(MOAM.clean_json("Hello\tWorld"), "Hello World")
    
    def test_strip_leading_trailing_whitespace(self):
        self.assertEqual(MOAM.clean_json("  Hello World  "), "Hello World")
    
    def test_remove_punctuations(self):
        self.assertEqual(MOAM.clean_json("Hello#*'World"), "Hello World")
    
    def test_combined(self):
        self.assertEqual(MOAM.clean_json("  Hello\r\n\tWorld#*'  "), "Hello World")

class TestCleanLemmatizerWords(unittest.TestCase):
    def setUp(self):
        self.lemmatizer = WordNetLemmatizer()

    def test_normal_sentence(self):
        self.assertEqual(MOAM.clean_lemmatizer_words("The cats are running", self.lemmatizer), "The cat be run")

    def test_sentence_with_punctuation(self):
        self.assertEqual(MOAM.clean_lemmatizer_words("Hello, world!", self.lemmatizer), "Hello world")

    def test_sentence_with_numbers(self):
        self.assertEqual(MOAM.clean_lemmatizer_words("There are 2 cats", self.lemmatizer), "There be cat")

    def test_mixed_case_sentence(self):
        self.assertEqual(MOAM.clean_lemmatizer_words("The Cats Are Running", self.lemmatizer), "The cat be run")

    def test_empty_string(self):
        self.assertEqual(MOAM.clean_lemmatizer_words("", self.lemmatizer), "")

    def test_single_character_words(self):
        self.assertEqual(MOAM.clean_lemmatizer_words("A b c d e f g", self.lemmatizer), "")

    def test_sentence_with_non_alpha_characters(self):
        self.assertEqual(MOAM.clean_lemmatizer_words("Hello @world #2024", self.lemmatizer), "Hello world")
       

class TestCleanStemWords(unittest.TestCase):
    def setUp(self):
        self.stemmer = PorterStemmer()

    def test_normal_sentence(self):
        self.assertEqual(MOAM.clean_stem_words("The cats are running", self.stemmer), "the cat are run")

    def test_sentence_with_punctuation(self):
        self.assertEqual(MOAM.clean_stem_words("Hello, world!", self.stemmer), "hello world")

    def test_sentence_with_numbers(self):
        self.assertEqual(MOAM.clean_stem_words("There are 2 cats", self.stemmer), "there are cat")

    def test_mixed_case_sentence(self):
        self.assertEqual(MOAM.clean_stem_words("The Cats Are Running", self.stemmer), "the cat are run")

    def test_empty_string(self):
        self.assertEqual(MOAM.clean_stem_words("", self.stemmer), "")

    def test_single_character_words(self):
        self.assertEqual(MOAM.clean_stem_words("A b c d e f g", self.stemmer), "")

    def test_sentence_with_non_alpha_characters(self):
        self.assertEqual(MOAM.clean_stem_words("Hello @world #2024", self.stemmer), "hello world")
        

class TestCleanStopWords(unittest.TestCase):
    
    def setUp(self):
        self.stop_words = set(stopwords.words("english"))

    def test_normal_sentence(self):
        self.assertEqual(MOAM.clean_stop_words("The cats are running",self.stop_words), "cats running")

    def test_sentence_with_punctuation(self):
        self.assertEqual(MOAM.clean_stop_words("Hello, world!",self.stop_words), "Hello world")

    def test_sentence_with_numbers(self):
        self.assertEqual(MOAM.clean_stop_words("There are 2 cats",self.stop_words), "cats")

    def test_mixed_case_sentence(self):
        self.assertEqual(MOAM.clean_stop_words("The Cats Are Running",self.stop_words), "Cats Running")

    def test_empty_string(self):
        self.assertEqual(MOAM.clean_stop_words("",self.stop_words), "")

    def test_single_character_words(self):
        self.assertEqual(MOAM.clean_stop_words("A b c d e f g",self.stop_words), "")

    def test_sentence_with_non_alpha_characters(self):
        self.assertEqual(MOAM.clean_stop_words("Hello @world #2024",self.stop_words), "Hello world")


class TestCleanString(unittest.TestCase):
    
    def test_remove_urls(self):
        self.assertEqual(MOAM.clean_string("Check this link http://example.com"), "Check this link")

    def test_remove_hashtags(self):
        self.assertEqual(MOAM.clean_string("This is a #hashtag"), "This is a")

    def test_remove_mentions(self):
        self.assertEqual(MOAM.clean_string("Mentioning @user"), "Mentioning")

    def test_remove_newlines_and_carriage_returns(self):
        self.assertEqual(MOAM.clean_string("Line1\nLine2\rLine3"), "Line1 Line2 Line3")

    def test_remove_tabs(self):
        self.assertEqual(MOAM.clean_string("This\tis\ta\ttest"), "This is a test")

    def test_remove_extra_whitespace(self):
        self.assertEqual(MOAM.clean_string("This  is   a    test"), "This is a test")

    def test_remove_punctuations(self):
        self.assertEqual(MOAM.clean_string("Hello, world!"), "Hello world")

    def test_remove_non_ascii_characters(self):
        self.assertEqual(MOAM.clean_string("Hello world 😊"), "Hello world")

    def test_combined_cases(self):
        self.assertEqual(MOAM.clean_string("Check this link http://example.com #hashtag @user\nNew line\tTab! 😊"), "Check this link New line Tab")


class TestCleanseString(unittest.TestCase):
    
    def setUp(self):
        self.stop_words = set(stopwords.words("english"))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    
    def test_normal_sentence(self):
        self.assertEqual(MOAM.cleanse_string("The cats are running", self.stop_words, self.stemmer, self.lemmatizer), ['Cat', 'run'])

    def test_sentence_with_punctuation(self):
        self.assertEqual(MOAM.cleanse_string("Hello, world!",self.stop_words,self.stemmer,self.lemmatizer), ['Hello', 'world'])

    def test_sentence_with_numbers(self):
        self.assertEqual(MOAM.cleanse_string("There are 2 cats",self.stop_words,self.stemmer,self.lemmatizer), ['Cat'])

    def test_mixed_case_sentence(self):
        self.assertEqual(MOAM.cleanse_string("The Cats Are Running", self.stop_words, self.stemmer, self.lemmatizer), ['Cat', 'run'])

    def test_empty_string(self):
        self.assertEqual(MOAM.cleanse_string("",self.stop_words,self.stemmer,self.lemmatizer), [])

    def test_single_character_words(self):
        self.assertEqual(MOAM.cleanse_string("A b c d e f g",self.stop_words,self.stemmer,self.lemmatizer), [])


class TestCleanseText(unittest.TestCase):

    def test_remove_punctuation(self):
        self.assertEqual(MOAM.cleanse_text("Hello, world!"), "Hello world")

    def test_empty_string(self):
        self.assertEqual(MOAM.cleanse_text(""), "")

    def test_string_with_only_punctuation(self):
        self.assertEqual(MOAM.cleanse_text("!@#$%^&*()"), "")


    def test_string_with_mixed_content(self):
        self.assertEqual(MOAM.cleanse_text("b'Hello, world!\\r\\n"), "Hello world")


class TestDataCleansing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stop_words = set(stopwords.words('english'))
        cls.lemmatizer = WordNetLemmatizer()
        cls.stemmer = PorterStemmer()

    def test_all_false(self):
        self.assertEqual(MOAM.data_cleansing("The cats are running", False, False, False, False, False), "The cats are running")

    def test_run_pii(self):
        self.assertEqual(MOAM.data_cleansing("My email is example@example.com", True, False, False, False, False), "My email is EMAIL")

    def test_run_cleanse(self):
        self.assertEqual(MOAM.data_cleansing("Hello, world!", False, True, False, False, False), "Hello world")

    def test_run_stop(self):
        self.assertEqual(MOAM.data_cleansing("The cats are running", False, False, False, True, False, stop_words=self.stop_words), "cats running")

    def test_run_lemm(self):
        lemmatizer = WordNetLemmatizer()
        self.assertEqual(MOAM.data_cleansing("The cats are running", False, False, True, False, False, lemmatizer=lemmatizer), "The cat be run")

    def test_run_stem(self):
        self.assertEqual(MOAM.data_cleansing("The cats are running", False, False, False, False, True, stemmer=self.stemmer), "the cat are run")

    def test_combined(self):
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        stemmer = PorterStemmer()
        self.assertEqual(MOAM.data_cleansing("My email is example@example.com. The cats are running!", True, True, True, True, True, stop_words=stop_words, lemmatizer=lemmatizer, stemmer=stemmer), "email email cat run")

class TestDataVaracityCheck(unittest.TestCase):

    def test_remove_insufficient_length_rows(self):
        df = pd.DataFrame({'text': ['short', 'this is long enough', 'tiny', 'adequate length']})
        result = MOAM.data_varacity_check(df, 'text', 5)
        expected = pd.DataFrame({'text': ['this is long enough', 'adequate length']})
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

    def test_convert_to_lowercase(self):
        df = pd.DataFrame({'text': ['SHORT', 'This Is Long Enough', 'TINY', 'Adequate Length']})
        result = MOAM.data_varacity_check(df, 'text', 5)
        expected = pd.DataFrame({'text': ['this is long enough', 'adequate length']})
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

    def test_empty_dataframe(self):
        df = pd.DataFrame({'text': []})
        result = MOAM.data_varacity_check(df, 'text', 5)
        expected = pd.DataFrame({'text': []}, dtype=object)
        pd.testing.assert_frame_equal(result, expected)

    def test_all_rows_removed(self):
        df = pd.DataFrame({'text': ['short', 'tiny']})
        result = MOAM.data_varacity_check(df, 'text', 5)
        expected = pd.DataFrame({'text': []}, dtype=object)
        pd.testing.assert_frame_equal(result, expected)

class TestDecodeNetout(unittest.TestCase):

    def test_decode_netout(self):
        netout = np.random.rand(13, 13, 3, 25)
        anchors = [116, 90, 156, 198, 373, 326]
        obj_thresh = 0.5
        net_h, net_w = 416, 416
        result = MOAM.decode_netout(netout, anchors, obj_thresh, net_h, net_w)
        self.assertIsInstance(result, list)

class TestMarkdownEscaper(unittest.TestCase):

    def test_escape_json(self):
        self.assertEqual(MOAM.markdown_escaper('```json{"key": "value"}```', 'json'), '{"key": "value"}')

    def test_escape_python(self):
        self.assertEqual(MOAM.markdown_escaper('```pythonprint("Hello, world!")```', 'python'), 'print("Hello, world!")')

    def test_no_escape(self):
        self.assertEqual(MOAM.markdown_escaper('This is a test', 'json'), 'This is a test')

    def test_partial_escape(self):
        self.assertEqual(MOAM.markdown_escaper('```json{"key": "value"}```', 'python'), '```json{"key": "value"}```')

    def test_empty_string(self):
        self.assertEqual(MOAM.markdown_escaper('', 'json'), '')

class TestMarkdownToJson(unittest.TestCase):

    def test_valid_json(self):
        self.assertEqual(MOAM.markdown_to_json('```json{"key": "value"}```'), {"key": "value"})

    def test_invalid_json(self):
        with self.assertRaises(json.JSONDecodeError):
            MOAM.markdown_to_json('```json{"key": "value"```')

    def test_no_escape(self):
        with self.assertRaises(json.JSONDecodeError):
            MOAM.markdown_to_json('This is a test')

    def test_empty_string(self):
        with self.assertRaises(json.JSONDecodeError):
            MOAM.markdown_to_json('')

#################################################################
#Test Utility
#################################################################

class TestGetFullVersion(unittest.TestCase):

    def test_standard_version(self):
        self.assertEqual(MOAM.get_full_version("Product", 1, 0, 0), "Product v1.0.0")

    def test_minor_update(self):
        self.assertEqual(MOAM.get_full_version("Product", 1, 1, 0), "Product v1.1.0")

    def test_patch_update(self):
        self.assertEqual(MOAM.get_full_version("Product", 1, 0, 1), "Product v1.0.1")

    def test_major_update(self):
        self.assertEqual(MOAM.get_full_version("Product", 2, 0, 0), "Product v2.0.0")

    def test_non_standard_version_name(self):
        self.assertEqual(MOAM.get_full_version("MyApp", 3, 2, 1), "MyApp v3.2.1")

    def test_zero_version(self):
        self.assertEqual(MOAM.get_full_version("Product", 0, 0, 0), "Product v0.0.0")

class TestGetVersion(unittest.TestCase):

    def test_standard_version(self):
        self.assertEqual(MOAM.get_version(1, 0, 0), "1.0.0")

    def test_minor_update(self):
        self.assertEqual(MOAM.get_version(1, 1, 0), "1.1.0")

    def test_patch_update(self):
        self.assertEqual(MOAM.get_version(1, 0, 1), "1.0.1")

    def test_major_update(self):
        self.assertEqual(MOAM.get_version(2, 0, 0), "2.0.0")

    def test_zero_version(self):
        self.assertEqual(MOAM.get_version(0, 0, 0), "0.0.0")

    def test_non_standard_version(self):
        self.assertEqual(MOAM.get_version(3, 2, 1), "3.2.1")



class TestPrintUsage(unittest.TestCase):

    @patch('MOAM.printversion')
    def test_printusage(self, mock_printversion):
        with patch('builtins.print') as mock_print:
            MOAM.printusage()
            expected_calls = [
                unittest.mock.call(""),
                unittest.mock.call("  -v, --version    prints the version of this software package."),
                unittest.mock.call(""),
                unittest.mock.call("  * - indicates required argument.")
            ]
            mock_print.assert_has_calls(expected_calls, any_order=False)
            mock_printversion.assert_called_once()


class TestSetLibraryConfiguration(unittest.TestCase):

    @patch('MOAM.pd.set_option')
    @patch('MOAM.pd.options', create=True)
    @patch('MOAM.np.set_printoptions')
    @patch('MOAM.debug.msg_info')
    def test_set_library_configuration(self, mock_msg_info, mock_set_printoptions, mock_pd_options, mock_set_option):
        MOAM.set_library_configuration()
        
        mock_msg_info.assert_called_once_with("Setting Pandas and Numpy library options.")
        mock_set_option.assert_called_once_with('display.max_colwidth', 10)
        mock_pd_options.display.float_format = '{:,.4f}'.format
        mock_set_printoptions.assert_called_once_with(precision=4)

        

class TestSplitText(unittest.TestCase):

    def test_split_text_basic(self):
        text = "This is a test. This is only a test."
        chunk_size = 10
        expected_output = ["This is a", "test. This", "is only a", "test."]
        self.assertEqual(MOAM.split_text(text, chunk_size), expected_output)

    def test_split_text_large_sentence(self):
        text = "This is a very long sentence that exceeds the chunk size."
        chunk_size = 10
        expected_output = [
            "This is a",
            "very long",
            "sentence",
            "that",
            "exceeds",
            "the chunk",
            "size."
        ]
        self.assertEqual(MOAM.split_text(text, chunk_size), expected_output)

    def test_split_text_exact_chunk_size(self):
        text = "1234567890"
        chunk_size = 10
        expected_output = ['', "1234567890"]
        self.assertEqual(MOAM.split_text(text, chunk_size), expected_output)

    def test_split_text_empty_string(self):
        text = ""
        chunk_size = 10
        expected_output = []
        self.assertEqual(MOAM.split_text(text, chunk_size), expected_output)

    def test_split_text_chunk_size_greater_than_text(self):
        text = "Short text."
        chunk_size = 50
        expected_output = ["Short text."]
        self.assertEqual(MOAM.split_text(text, chunk_size), expected_output)

       



##############################################
# Test Security
# ############################################
        

class TestPromptInjectionSplitString(unittest.TestCase):

    def test_prompt_injection_split_string_basic(self):
        your_string = "This is a test string."
        n = 5
        expected_output = ["This ", "is a ", "test ", "strin", "g."]
        self.assertEqual(MOAM.prompt_injection_split_string(your_string, n), expected_output)

    def test_prompt_injection_split_string_exact_chunk_size(self):
        your_string = "12345"
        n = 5
        expected_output = ["12345"]
        self.assertEqual(MOAM.prompt_injection_split_string(your_string, n), expected_output)

    def test_prompt_injection_split_string_empty_string(self):
        your_string = ""
        n = 5
        expected_output = []
        self.assertEqual(MOAM.prompt_injection_split_string(your_string, n), expected_output)

    def test_prompt_injection_split_string_chunk_size_greater_than_string(self):
        your_string = "Short"
        n = 10
        expected_output = ["Short"]
        self.assertEqual(MOAM.prompt_injection_split_string(your_string, n), expected_output)

    def test_prompt_injection_split_string_chunk_size_one(self):
        your_string = "ABCDE"
        n = 1
        expected_output = ["A", "B", "C", "D", "E"]
        self.assertEqual(MOAM.prompt_injection_split_string(your_string, n), expected_output)

        

class TestPromptInjectionPredict(unittest.TestCase):

    def test_prompt_injection_predict_basic(self):
        mock_pipe = MagicMock()
        mock_pipe.return_value = [{'label': 0, 'score': 0.9}, {'label': 1, 'score': 0.1}]
        inc_prompt = "Test prompt"
        id2label = {0: 'Label A', 1: 'Label B'}

        with patch.dict('MOAM.__dict__', {'id2label': id2label}):
            result = MOAM.prompt_injection_predict(mock_pipe, inc_prompt)
        
        expected_output = {'Label A': 0.9, 'Label B': 0.1}
        self.assertEqual(result, expected_output)
        mock_pipe.assert_called_once_with(inc_prompt)

    def test_prompt_injection_predict_empty_result(self):
        mock_pipe = MagicMock()
        mock_pipe.return_value = []
        inc_prompt = "Test prompt"
        id2label = {0: 'Label A', 1: 'Label B'}

        with patch.dict('MOAM.__dict__', {'id2label': id2label}):
            result = MOAM.prompt_injection_predict(mock_pipe, inc_prompt)
        
        expected_output = {}
        self.assertEqual(result, expected_output)
        mock_pipe.assert_called_once_with(inc_prompt)

    def test_prompt_injection_predict_unmapped_label(self):
        mock_pipe = MagicMock()
        mock_pipe.return_value = [{'label': 2, 'score': 0.5}]
        inc_prompt = "Test prompt"
        id2label = {0: 'Label A', 1: 'Label B'}

        with patch.dict('MOAM.__dict__', {'id2label': id2label}):
            result = MOAM.prompt_injection_predict(mock_pipe, inc_prompt)
        
        expected_output = {None: 0.5}
        self.assertEqual(result, expected_output)
        mock_pipe.assert_called_once_with(inc_prompt)

        
class TestDetectPromptInjection(unittest.TestCase):

    @patch('MOAM.prompt_injection_split_string')
    @patch('MOAM.prompt_injection_predict')
    @patch('MOAM.process_exception')
    def test_detect_prompt_injection_exception(self, mock_process_exception, mock_predict, mock_split_string):
        mock_split_string.return_value = ["chunk1", "chunk2"]
        mock_predict.side_effect = Exception("API call failed")
        inc_prompt = "This is a test prompt."
        the_models = [MagicMock(), MagicMock()]

        result, offending_content = MOAM.detect_PromptInjection(inc_prompt, the_models)
        
        self.assertFalse(result)
        self.assertEqual(offending_content, [])
        mock_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)
        mock_predict.assert_called_once()
        mock_process_exception.assert_called_once()

##############################################
# Test Replace   
# ############################################


class TestDecodeValue(unittest.TestCase):

    def test_decode_value_bytes(self):
        value = b'Test bytes'
        with unittest.mock.patch('MOAM.decode_text', return_value='Decoded text'):
            result = MOAM.decode_value(value)
        self.assertEqual(result, "Decoded text")

    def test_decode_value_other(self):
        value = 12345
        result = MOAM.decode_value(value)
        self.assertEqual(result, "")

##############################################
# Promt_support
# ############################################

class TestCreateGPT35ResponseTemplate(unittest.TestCase):

    def test_create_gpt35_response_template(self):
        system_content = "System message"
        user_content = "User message"
        assistant_content = "Assistant message"
        expected_output = json.dumps({
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_content}
            ]
        })
        result = MOAM.create_gpt35_response_template(system_content, user_content, assistant_content)
        self.assertEqual(result, expected_output)

    def test_create_gpt35_response_template_empty_strings(self):
        system_content = ""
        user_content = ""
        assistant_content = ""
        expected_output = json.dumps({
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_content}
            ]
        })
        result = MOAM.create_gpt35_response_template(system_content, user_content, assistant_content)
        self.assertEqual(result, expected_output)

    def test_create_gpt35_response_template_special_characters(self):
        system_content = "System!@#"
        user_content = "User$%^"
        assistant_content = "Assistant&*()"
        expected_output = json.dumps({
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_content}
            ]
        })
        result = MOAM.create_gpt35_response_template(system_content, user_content, assistant_content)
        self.assertEqual(result, expected_output)


class TestCreatePCPFResponseTemplate(unittest.TestCase):

    def test_create_pcpf_response_template(self):
        prompt_content = "Prompt message"
        completion_content = "Completion message"
        expected_output = json.dumps({
            "prompt": prompt_content,
            "completion": completion_content,
        })
        result = MOAM.create_pcpf_response_template(prompt_content, completion_content)
        self.assertEqual(result, expected_output)

    def test_create_pcpf_response_template_empty_strings(self):
        prompt_content = ""
        completion_content = ""
        expected_output = json.dumps({
            "prompt": prompt_content,
            "completion": completion_content,
        })
        result = MOAM.create_pcpf_response_template(prompt_content, completion_content)
        self.assertEqual(result, expected_output)

    def test_create_pcpf_response_template_special_characters(self):
        prompt_content = "Prompt!@#"
        completion_content = "Completion$%^"
        expected_output = json.dumps({
            "prompt": prompt_content,
            "completion": completion_content,
        })
        result = MOAM.create_pcpf_response_template(prompt_content, completion_content)
        self.assertEqual(result, expected_output)


class TestGCPGenAIPromptJSON(unittest.TestCase):

    @patch('MOAM.genai.configure')
    @patch('MOAM.genai.GenerativeModel')
    def test_gcpgenai_prompt_json_success(self, mock_generative_model, mock_configure):
        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value.text = '{"result": "success"}'
        mock_generative_model.return_value = mock_model_instance

        inc_system = "System message"
        inc_user = "User message"
        the_model = "test-model"
        model_max_token_response = 100
        model_temperature = 0.7
        model_top_p = 0.9

        result = MOAM.gcpgenai_prompt_json(inc_system, inc_user, the_model, model_max_token_response, model_temperature, model_top_p)
        self.assertEqual(result, '{"result": "success"}')

    @patch('MOAM.genai.configure')
    @patch('MOAM.genai.GenerativeModel')
    def test_gcpgenai_prompt_json_failure_setup(self, mock_generative_model, mock_configure):
        mock_generative_model.side_effect = Exception("Failed to setup generative query")

        inc_system = "System message"
        inc_user = "User message"
        the_model = "test-model"
        model_max_token_response = 100
        model_temperature = 0.7
        model_top_p = 0.9

        result = MOAM.gcpgenai_prompt_json(inc_system, inc_user, the_model, model_max_token_response, model_temperature, model_top_p)
        self.assertEqual(result, json.dumps({"error": "Failed to execute generative query"}))

    @patch('MOAM.genai.configure')
    @patch('MOAM.genai.GenerativeModel')
    def test_gcpgenai_prompt_json_failure_execution(self, mock_generative_model, mock_configure):
        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.side_effect = Exception("Failed to execute generative query")
        mock_generative_model.return_value = mock_model_instance

        inc_system = "System message"
        inc_user = "User message"
        the_model = "test-model"
        model_max_token_response = 100
        model_temperature = 0.7
        model_top_p = 0.9

        result = MOAM.gcpgenai_prompt_json(inc_system, inc_user, the_model, model_max_token_response, model_temperature, model_top_p)
        self.assertEqual(result, json.dumps({"error": "Failed to execute generative query"}))


##############################################
# Test plot
##############################################


class TestPlotHistory(unittest.TestCase):

    @patch('MOAM.plt.show')
    @patch('MOAM.plt.close')
    def test_plot_history(self, mock_close, mock_show):
        history_mock = MagicMock()
        history_mock.history = {
            'accuracy': [0.8, 0.85, 0.9],
            'val_accuracy': [0.75, 0.8, 0.85],
            'loss': [0.5, 0.4, 0.3],
            'val_loss': [0.55, 0.45, 0.35]
        }

        MOAM.plot_history(history_mock)

        self.assertEqual(mock_show.call_count, 2)
        self.assertEqual(mock_close.call_count, 3)




class TestSummarizeDiagnosticsSeaborn(unittest.TestCase):

    @patch('MOAM.plt.show')
    @patch('MOAM.plt.figure')
    @patch('MOAM.sns.lineplot')
    @patch('MOAM.pd.DataFrame')
    def test_summarize_diagnostics_seaborn(self, mock_dataframe, mock_lineplot, mock_figure, mock_show):
        history_mock = MagicMock()
        history_mock.history = {
            'accuracy': [0.8, 0.85, 0.9],
            'val_accuracy': [0.75, 0.8, 0.85]
        }
        mock_df_instance = MagicMock()
        mock_dataframe.return_value = mock_df_instance

        title = "Test Title"
        MOAM.summarize_diagnostics_seaborn(history_mock, title)

        mock_dataframe.assert_called_once_with(history_mock.history)
        mock_df_instance.__getitem__.assert_any_call("accuracy")
        mock_df_instance.__getitem__.assert_any_call("val_accuracy")
        mock_lineplot.assert_called_once()
        mock_figure.assert_called_once_with(figsize=[7, 5])
        mock_show.assert_called_once()

        
        
##############################################
#Test nre
##############################################

class TestReplaceEmailSpacy(unittest.TestCase):

    @patch('MOAM.re.sub')
    @patch('MOAM.debug.msg_warning')
    def test_replace_email_spacy(self, mock_msg_warning, mock_re_sub):
        inc_model = MagicMock()
        inc_model.max_length = 10
        inc_model.return_value = MagicMock()
        
        inc_matcher = MagicMock()
        inc_matcher.return_value = [(0, 5)]
        
        inc_text = "test@example.com"
        
        mock_re_sub.side_effect = lambda pattern, repl, string: string.replace("test@example.com", "EMAIL")
        
        result = MOAM.replace_email_spacy(inc_model, inc_matcher, inc_text)
        
        self.assertEqual(result, "EMAIL")
        inc_model.assert_called()
        inc_matcher.assert_called()
        mock_re_sub.assert_called()
        mock_msg_warning.assert_not_called()

    @patch('MOAM.re.sub')
    @patch('MOAM.debug.msg_warning')
    def test_replace_email_spacy_exception(self, mock_msg_warning, mock_re_sub):
        inc_model = MagicMock()
        inc_model.max_length = 10
        inc_model.side_effect = Exception("Model error")
        
        inc_matcher = MagicMock()
        inc_text = "test@example.com"
        
        result = MOAM.replace_email_spacy(inc_model, inc_matcher, inc_text)
        
        self.assertEqual(result, inc_text)
        mock_msg_warning.assert_called_once_with("clean_email_spacy threw an exception: Exception('Model error')")
        mock_re_sub.assert_not_called()

class TestCleanNamedEntityRecognition(unittest.TestCase):

    @patch('MOAM.re.sub')
    @patch('MOAM.debug.msg_warning')
    def test_clean_named_entity_recognition(self, mock_msg_warning, mock_re_sub):
        inc_model = MagicMock()
        inc_model.max_length = 10
        inc_model.return_value = MagicMock(ents=[MagicMock(label_='PERSON', text='John Doe')])
        
        inc_text = "John Doe is a software engineer."
        
        mock_re_sub.side_effect = lambda pattern, repl, string: string.replace("John Doe", "PERSON")
        
        result = MOAM.clean_named_entity_recognition(inc_model, inc_text)
        
        self.assertEqual(result, "PERSON is a software engineer.")
        inc_model.assert_called()
        mock_re_sub.assert_called()
        mock_msg_warning.assert_not_called()

class TestCleanNamedEntityRecognition(unittest.TestCase):

    @patch('MOAM.re.sub')
    @patch('MOAM.debug.msg_warning')
    def test_clean_named_entity_recognition(self, mock_msg_warning, mock_re_sub):
        inc_model = MagicMock()
        inc_model.max_length = 10
        inc_model.return_value = MagicMock(ents=[MagicMock(label_='PERSON', text='John Doe')])
        
        inc_text = "John Doe is a software engineer."
        
        mock_re_sub.side_effect = lambda pattern, repl, string: string.replace("John Doe", "PERSON")
        
        result = MOAM.clean_named_entity_recognition(inc_model, inc_text)
        
        self.assertEqual(result, "PERSON is a software engineer.")
        inc_model.assert_called()
        mock_re_sub.assert_called()
        mock_msg_warning.assert_not_called()

        

class TestDetectAddress():

    @patch('MOAM.usaddress.tag')
    @patch('MOAM.debug.msg_warning')
    @patch('MOAM.re.compile')
    def test_detect_address(self, mock_re_compile, mock_msg_warning, mock_usaddress_tag):
        inc_model = MagicMock()
        inc_text = "123 Main St, Springfield, IL 62704"
        
        # Mocking re.compile to return a mock pattern object
        mock_pattern = mock.Mock()
        mock_pattern.search.return_value = MagicMock(group=lambda: "62704")
        mock_re_compile.return_value = mock_pattern
        
        # Mocking the model's return value
        inc_model.return_value = MagicMock(ents=[
            MagicMock(label_='GPE', text='Springfield'),
            MagicMock(label_='LOC', text='IL')
        ])
        
        # Mocking usaddress.tag
        mock_usaddress_tag.return_value = ({'PlaceName': 'Springfield', 'StateName': 'IL'}, 'Street Address')
        
        result = MOAM.detect_address(inc_text, inc_model)
        
        self.assertEqual(result, "Springfield, IL, 62704")
        mock_pattern.search.assert_called_once_with(inc_text)
        inc_model.assert_called_once_with(inc_text)
        mock_usaddress_tag.assert_called_once_with(inc_text, tag_mapping={'PlaceName': 'city', 'StateName': 'state'})
        mock_msg_warning.assert_not_called()

    @patch('MOAM.usaddress.tag')
    @patch('MOAM.debug.msg_warning')
    @patch('MOAM.re.compile')
    def test_detect_address_no_zipcode(self, mock_re_compile, mock_msg_warning, mock_usaddress_tag):
        inc_model = MagicMock()
        inc_text = "123 Main St, Springfield, IL"
        
        # Mocking re.compile to return a mock pattern object
        mock_pattern = mock.Mock()
        mock_pattern.search.return_value = None
        mock_re_compile.return_value = mock_pattern
        
        # Mocking the model's return value
        inc_model.return_value = MagicMock(ents=[
            MagicMock(label_='GPE', text='Springfield'),
            MagicMock(label_='LOC', text='IL')
        ])
        
        # Mocking usaddress.tag
        mock_usaddress_tag.return_value = ({'PlaceName': 'Springfield', 'StateName': 'IL'}, 'Street Address')
        
        result = MOAM.detect_address(inc_text, inc_model)
        
        self.assertEqual(result, "Springfield, IL, ")
        mock_pattern.search.assert_called_once_with(inc_text)
        inc_model.assert_called_once_with(inc_text)
        mock_usaddress_tag.assert_called_once_with(inc_text, tag_mapping={'PlaceName': 'city', 'StateName': 'state'})
        mock_msg_warning.assert_not_called()

    @patch('MOAM.usaddress.tag')
    @patch('MOAM.debug.msg_warning')
    @patch('MOAM.re.compile')
    def test_detect_address_exception(self, mock_re_compile, mock_msg_warning, mock_usaddress_tag):
        inc_model = MagicMock()
        inc_text = "123 Main St, Springfield, IL"
        
        # Mocking re.compile to return a mock pattern object
        mock_pattern = mock.Mock()
        mock_pattern.search.return_value = None
        mock_re_compile.return_value = mock_pattern
        
        # Mocking the model's return value
        inc_model.return_value = MagicMock(ents=[
            MagicMock(label_='GPE', text='Springfield'),
            MagicMock(label_='LOC', text='IL')
        ])
        
        # Mocking usaddress.tag to raise an exception
        mock_usaddress_tag.side_effect = Exception("usaddress error")
        
        result = MOAM.detect_address(inc_text, inc_model)
        
        self.assertEqual(result, "Springfield, IL, ")
        mock_pattern.search.assert_called_once_with(inc_text)
        inc_model.assert_called_once_with(inc_text)
        mock_usaddress_tag.assert_called_once_with(inc_text, tag_mapping={'PlaceName': 'city', 'StateName': 'state'})
        mock_msg_warning.assert_called_once_with("ADDRESS processing encountered a problem: usaddress error")



class TestDetectLocations(unittest.TestCase):

    @patch('MOAM.prompt_injection_split_string')
    @patch('MOAM.process_exception')
    def test_detect_locations(self, mock_process_exception, mock_prompt_injection_split_string):
        inc_model = MagicMock()
        inc_prompt = "New York is a city in the United States. Paris is the capital of France."
        
        # Mocking prompt_injection_split_string
        mock_prompt_injection_split_string.return_value = [inc_prompt]
        
        # Mocking the model's return value
        inc_model.return_value = MagicMock(ents=[
            MagicMock(label_='GPE', text='New York'),
            MagicMock(label_='GPE', text='Paris')
        ])
        
        result = MOAM.detect_locations(inc_prompt, inc_model)
        
        self.assertEqual(result, ['New York', 'Paris'])
        mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)
        inc_model.assert_called_once_with(inc_prompt)
        mock_process_exception.assert_not_called()

    @patch('MOAM.prompt_injection_split_string')
    @patch('MOAM.process_exception')
    def test_detect_locations_multiple_chunks(self, mock_process_exception, mock_prompt_injection_split_string):
        inc_model = MagicMock()
        inc_prompt = "New York is a city in the United States. Paris is the capital of France."
        
        # Mocking prompt_injection_split_string to return multiple chunks
        mock_prompt_injection_split_string.return_value = ["New York is a city in the United States.", "Paris is the capital of France."]
        
        # Mocking the model's return value for each chunk
        inc_model.side_effect = [
            MagicMock(ents=[MagicMock(label_='GPE', text='New York')]),
            MagicMock(ents=[MagicMock(label_='GPE', text='Paris')])
        ]
        
        result = MOAM.detect_locations(inc_prompt, inc_model)
        
        self.assertEqual(result, ['New York', 'Paris'])
        mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)
        self.assertEqual(inc_model.call_count, 2)
        mock_process_exception.assert_not_called()

    @patch('MOAM.prompt_injection_split_string')
    @patch('MOAM.process_exception')
    def test_detect_locations_exception(self, mock_process_exception, mock_prompt_injection_split_string):
        inc_model = MagicMock()
        inc_prompt = "New York is a city in the United States. Paris is the capital of France."
        
        # Mocking prompt_injection_split_string
        mock_prompt_injection_split_string.return_value = [inc_prompt]
        
        # Mocking the model to raise an exception
        inc_model.side_effect = Exception("Model error")
        
        result = MOAM.detect_locations(inc_prompt, inc_model)
        
        self.assertEqual(result, [])
        mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)
        inc_model.assert_called_once_with(inc_prompt)
        mock_process_exception.assert_called_once_with("ERROR finding organizations as follows: Model error")


class TestDetectOrganizations(unittest.TestCase):

    @patch('MOAM.prompt_injection_split_string')
    @patch('MOAM.process_exception')
    def test_detect_organizations(self, mock_process_exception, mock_prompt_injection_split_string):
        inc_model = MagicMock()
        inc_prompt = "Google and Microsoft are leading tech companies."
        
        # Mocking prompt_injection_split_string
        mock_prompt_injection_split_string.return_value = [inc_prompt]
        
        # Mocking the model's return value
        inc_model.return_value = MagicMock(ents=[
            MagicMock(label_='ORG', text='Google'),
            MagicMock(label_='ORG', text='Microsoft')
        ])
        
        result = MOAM.detect_organizations(inc_prompt, inc_model)
        
        self.assertEqual(result, ["Microsoft", "Google"])
        mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)
        inc_model.assert_called_once_with(inc_prompt)
        mock_process_exception.assert_not_called()

    @patch('MOAM.prompt_injection_split_string')
    @patch('MOAM.process_exception')
    def test_detect_organizations_multiple_chunks(self, mock_process_exception, mock_prompt_injection_split_string):
        inc_model = MagicMock()
        inc_prompt = "Google and Microsoft are leading tech companies. Apple is another major player."
        
        # Mocking prompt_injection_split_string to return multiple chunks
        mock_prompt_injection_split_string.return_value = ["Google and Microsoft are leading tech companies.", "Apple is another major player."]
        
        # Mocking the model's return value for each chunk
        inc_model.side_effect = [
            MagicMock(ents=[MagicMock(label_='ORG', text='Google'), MagicMock(label_='ORG', text='Microsoft')]),
            MagicMock(ents=[MagicMock(label_='ORG', text='Apple')])
        ]
        
        result = MOAM.detect_organizations(inc_prompt, inc_model)
        
        self.assertEqual(result, ['Microsoft', 'Apple', 'Google'])
        mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)
        self.assertEqual(inc_model.call_count, 2)
        mock_process_exception.assert_not_called()

    @patch('MOAM.prompt_injection_split_string')
    @patch('MOAM.process_exception')
    def test_detect_organizations_exception(self, mock_process_exception, mock_prompt_injection_split_string):
        inc_model = MagicMock()
        inc_prompt = "Google and Microsoft are leading tech companies."
        
        # Mocking prompt_injection_split_string
        mock_prompt_injection_split_string.return_value = [inc_prompt]
        
        # Mocking the model to raise an exception
        inc_model.side_effect = Exception("Model error")
        
        result = MOAM.detect_organizations(inc_prompt, inc_model)
        
        self.assertEqual(result, [])
        mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)
        inc_model.assert_called_once_with(inc_prompt)
        mock_process_exception.assert_called_once_with("ERROR finding organizations as follows: Model error")
        
        
##############################################
# Test pii
##############################################

class TestCleanPII(unittest.TestCase):

    def test_clean_pii_email(self):
        inc_input = "Contact me at example@example.com"
        expected_output = "Contact me at EMAIL"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_credit_card(self):
        inc_input = "My credit card number is 1234-5678-9012-3456"
        expected_output = "My credit card number is CREDITCARD"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_link(self):
        inc_input = "Visit https://example.com for more info"
        expected_output = "Visit URL for more info"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_ip(self):
        inc_input = "My IP address is 192.168.1.1"
        expected_output = "My IP address is IP"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_ipv6(self):
        inc_input = "My IPv6 address is 2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        expected_output = "My IPv6 address is IPV6"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_phone(self):
        inc_input = "Call me at (123) 456-7890"
        expected_output = "Call me at PHONENUMBER"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_street_address(self):
        inc_input = "I live at 123 Main St."
        expected_output = "I live at STREETADDRESS"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_btc_address(self):
        inc_input = "My BTC address is 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        expected_output = "My BTC address is BTCADDRESS"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_zipcode(self):
        inc_input = "My ZIP code is 12345-6789"
        expected_output = "My ZIP code is PHONENUMBER"
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

    def test_clean_pii_zipcode2(self):
        inc_input = "My ZIP code is .. 12345. "
        expected_output = "My ZIP code is .. ZIPCODE2. "
        self.assertEqual(MOAM.clean_pii(inc_input), expected_output)

##############################################
#Test decode_pdf
##############################################


class TestReadPdPdf(unittest.TestCase):

    @patch('MOAM.os.path.isfile')
    @patch('MOAM.fitz.open')
    @patch('MOAM.debug.msg_info')
    @patch('MOAM.process_exception')
    def test_read_pd_pdf_success(self, mock_process_exception, mock_msg_info, mock_fitz_open, mock_isfile):
        mock_isfile.return_value = True
        mock_doc = MagicMock()
        mock_page = MagicMock()
        mock_page.get_text.return_value = [
            (0, 0, 0, 0, "Sample text", 0, 0, 0)
        ]
        mock_doc.__iter__.return_value = [mock_page]
        mock_fitz_open.return_value = mock_doc

        result = MOAM.read_pd_pdf("dummy.pdf")
        self.assertEqual(result, " Sample text")

        mock_isfile.assert_called_once_with("dummy.pdf")
        mock_fitz_open.assert_called_once_with("dummy.pdf")
        mock_msg_info.assert_any_call(f"Entering {MOAM.__name__} read_pd_pdf")
        mock_msg_info.assert_any_call(f"Exiting {MOAM.__name__} read_pd_pdf")
        mock_process_exception.assert_not_called()

    @patch('MOAM.os.path.isfile')
    @patch('MOAM.process_exception')
    def test_read_pd_pdf_file_not_found(self, mock_process_exception, mock_isfile):
        mock_isfile.return_value = False

        with self.assertRaises(SystemExit):
            MOAM.read_pd_pdf("missing.pdf")

        mock_isfile.assert_called_once_with("missing.pdf")
        mock_process_exception.assert_not_called()

    @patch('MOAM.os.path.isfile')
    @patch('MOAM.fitz.open')
    @patch('MOAM.process_exception')
    def test_read_pd_pdf_exception(self, mock_process_exception, mock_fitz_open, mock_isfile):
        mock_isfile.return_value = True
        mock_fitz_open.side_effect = Exception("Some error")

        result = MOAM.read_pd_pdf("dummy.pdf")
        self.assertEqual(result, "")

        mock_isfile.assert_called_once_with("dummy.pdf")
        mock_fitz_open.assert_called_once_with("dummy.pdf")
        mock_process_exception.assert_called_once_with("ERROR detected trying detect the PDF path as follows: Some error")


class TestReadPdf(unittest.TestCase):

    @patch('MOAM.os.path.isfile')
    @patch('MOAM.fitz.open')
    @patch('MOAM.debug.msg_info')
    @patch('MOAM.debug.msg_error')
    @patch('MOAM.process_exception')
    def test_read_pdf_success(self, mock_process_exception, mock_msg_error, mock_msg_info, mock_fitz_open, mock_isfile):
        mock_isfile.return_value = True
        mock_doc = MagicMock()
        mock_page = MagicMock()
        mock_page.get_text.return_value = [
            (0, 0, 0, 0, "Sample text", 0, 0, 0)
        ]
        mock_doc.__iter__.return_value = [mock_page]
        mock_fitz_open.return_value = mock_doc

        result = MOAM.read_pdf("dummy.pdf")
        self.assertEqual(result, " Sample text")

        mock_isfile.assert_called_once_with("dummy.pdf")
        mock_fitz_open.assert_called_once_with("dummy.pdf")
        mock_msg_info.assert_any_call(f"Entering {MOAM.__name__} read_pdf")
        mock_msg_info.assert_any_call(f"Exiting {MOAM.__name__} read_pdf")
        mock_process_exception.assert_not_called()
        mock_msg_error.assert_not_called()

    @patch('MOAM.os.path.isfile')
    @patch('MOAM.debug.msg_error')
    @patch('MOAM.process_exception')
    def test_read_pdf_file_not_found(self, mock_process_exception, mock_msg_error, mock_isfile):
        mock_isfile.return_value = False

        with self.assertRaises(SystemExit):
            MOAM.read_pdf("missing.pdf")

        mock_isfile.assert_called_once_with("missing.pdf")
        mock_msg_error.assert_any_call("ERROR detected, the input data file for work further in the notebook is missing.  Aborting execution.")
        mock_msg_error.assert_any_call("  Resolve the missing.pdf missing file and repeat.")
        mock_process_exception.assert_not_called()

    @patch('MOAM.os.path.isfile')
    @patch('MOAM.fitz.open')
    @patch('MOAM.process_exception')
    def test_read_pdf_exception(self, mock_process_exception, mock_fitz_open, mock_isfile):
        mock_isfile.return_value = True
        mock_fitz_open.side_effect = Exception("Some error")

        result = MOAM.read_pdf("dummy.pdf")
        self.assertEqual(result, "")

        mock_isfile.assert_called_once_with("dummy.pdf")
        mock_fitz_open.assert_called_once_with("dummy.pdf")
        mock_process_exception.assert_called_once_with("ERROR detected trying detect the PDF path as follows: Some error")

##############################################
#Test metrics
##############################################


class TestCalculateStringSize(unittest.TestCase):

    def test_calculate_string_size_empty_string(self):
        self.assertEqual(MOAM.calculate_string_size(""), 0)

    def test_calculate_string_size_single_word(self):
        self.assertEqual(MOAM.calculate_string_size("Hello"), 1)

    def test_calculate_string_size_multiple_words(self):
        self.assertEqual(MOAM.calculate_string_size("Hello world"), 2)

    def test_calculate_string_size_with_punctuation(self):
        self.assertEqual(MOAM.calculate_string_size("Hello, world!"), 4)

    def test_calculate_string_size_with_numbers(self):
        self.assertEqual(MOAM.calculate_string_size("There are 2 apples"), 4)

    def test_calculate_string_size_with_special_characters(self):
        self.assertEqual(MOAM.calculate_string_size("Hello @world #2023"), 5)


class TestGetMetrics(unittest.TestCase):

    @patch('MOAM.calculate_string_size')
    @patch('MOAM.tqdm')
    @patch('MOAM.debug.msg_debug')
    @patch('MOAM.process_exception')
    def test_get_metrics_success(self, mock_process_exception, mock_msg_debug, mock_tqdm, mock_calculate_string_size):
        mock_calculate_string_size.side_effect = lambda x: len(x.split())
        mock_tqdm.side_effect = lambda x: x

        data = {'col1': ['Hello world', 'Test string', 'Another example']}
        df = pd.DataFrame(data)
        source_columns = ['col1']

        MOAM.get_metrics(df, source_columns)

        mock_calculate_string_size.assert_any_call('Hello world')
        mock_calculate_string_size.assert_any_call('Test string')
        mock_calculate_string_size.assert_any_call('Another example')
        mock_msg_debug.assert_any_call(f"Metrics on tokens for col1.\n")
        mock_msg_debug.assert_any_call(f"..records: {3:>30,}")
        mock_msg_debug.assert_any_call(f"......max: {2:>30,}")
        mock_msg_debug.assert_any_call(f"......avg: {2:>30,}")
        mock_msg_debug.assert_any_call(f"......min: {2:>30,}")
        mock_process_exception.assert_not_called()

if __name__ == '__main__':
    unittest.main()