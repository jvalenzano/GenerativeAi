# Introduction
This document provides an overview of the test cases included in the `test.py` file for the funcitons in the `MOAM`. These tests are designed to ensure the correct functionality of the functions in the `MOAM` module.

## Test Cases

# Test Documentation for `TestCleanDate` in `test.py`

### Test Case 1: `test_remove_urls`
- **Description**: This test verifies that the `clean_date` function correctly removes URLs from the input string.
- **Input**: `"Check this link http://example.com"`
- **Expected Output**: `"Check this link"`

### Test Case 2: `test_remove_hashtags`
- **Description**: This test checks that the `clean_date` function removes hashtags from the input string.
- **Input**: `"This is a #hashtag"`
- **Expected Output**: `"This is a"`

### Test Case 3: `test_remove_mentions`
- **Description**: This test ensures that the `clean_date` function removes mentions from the input string.
- **Input**: `"Mentioning @user"`
- **Expected Output**: `"Mentioning"`

### Test Case 4: `test_remove_newlines_and_carriage_returns`
- **Description**: This test verifies that the `clean_date` function removes newlines and carriage returns from the input string.
- **Input**: `"Line1\nLine2\rLine3"`
- **Expected Output**: `"Line1Line2Line3"`

### Test Case 5: `test_remove_tabs`
- **Description**: This test checks that the `clean_date` function removes tab characters from the input string.
- **Input**: `"This\tis\ta\ttest"`
- **Expected Output**: `"This is a test"`

### Test Case 6: `test_remove_extra_whitespace`
- **Description**: This test ensures that the `clean_date` function removes extra whitespace from the input string.
- **Input**: `"This  is   a    test"`
- **Expected Output**: `"This is a test"`

### Test Case 7: `test_remove_punctuations`
- **Description**: This test verifies that the `clean_date` function removes punctuation from the input string.
- **Input**: `"Hello, world!"`
- **Expected Output**: `"Hello world"`

### Test Case 8: `test_combined_cases`
- **Description**: This test checks that the `clean_date` function handles a combination of URLs, hashtags, mentions, newlines, tabs, and punctuation in the input string.
- **Input**: `"Check this link http://example.com #hashtag @user\nNew line\tTab!"`
- **Expected Output**: `"Check this link New line Tab"`

# Test Documentation for `TestCleanJson` in `test.py`

### Test Case 1: `test_remove_carriage_returns`
- **Description**: This test verifies that the `clean_json` function removes carriage return characters from the input string.
- **Input**: `"Hello\rWorld"`
- **Expected Output**: `"HelloWorld"`

### Test Case 2: `test_remove_newlines`
- **Description**: This test checks that the `clean_json` function removes newline characters from the input string.
- **Input**: `"Hello\nWorld"`
- **Expected Output**: `"HelloWorld"`

### Test Case 3: `test_remove_extra_whitespace`
- **Description**: This test ensures that the `clean_json` function removes extra whitespace from the input string.
- **Input**: `"Hello    World"`
- **Expected Output**: `"Hello World"`

### Test Case 4: `test_remove_tabs`
- **Description**: This test verifies that the `clean_json` function removes tab characters from the input string.
- **Input**: `"Hello\tWorld"`
- **Expected Output**: `"Hello World"`

### Test Case 5: `test_strip_leading_trailing_whitespace`
- **Description**: This test checks that the `clean_json` function strips leading and trailing whitespace from the input string.
- **Input**: `"  Hello World  "`
- **Expected Output**: `"Hello World"`

### Test Case 6: `test_remove_punctuations`
- **Description**: This test ensures that the `clean_json` function removes punctuation from the input string.
- **Input**: `"Hello#*'World"`
- **Expected Output**: `"Hello World"`

### Test Case 7: `test_combined`
- **Description**: This test verifies that the `clean_json` function handles a combination of carriage returns, newlines, tabs, punctuation, and leading/trailing whitespace in the input string.
- **Input**: `"  Hello\r\n\tWorld#*'  "`
- **Expected Output**: `"Hello World"`

# Test Documentation for `TestCleanLemmatizerWords` in `test.py`

### Test Case 1: `test_normal_sentence`
- **Description**: This test verifies that the `clean_lemmatizer_words` function correctly lemmatizes a normal sentence.
- **Input**: `"The cats are running"`
- **Expected Output**: `"The cat be run"`

### Test Case 2: `test_sentence_with_punctuation`
- **Description**: This test checks that the `clean_lemmatizer_words` function removes punctuation and lemmatizes the sentence.
- **Input**: `"Hello, world!"`
- **Expected Output**: `"Hello world"`

### Test Case 3: `test_sentence_with_numbers`
- **Description**: This test ensures that the `clean_lemmatizer_words` function removes numbers and lemmatizes the sentence.
- **Input**: `"There are 2 cats"`
- **Expected Output**: `"There be cat"`

### Test Case 4: `test_mixed_case_sentence`
- **Description**: This test verifies that the `clean_lemmatizer_words` function handles mixed case sentences and lemmatizes them correctly.
- **Input**: `"The Cats Are Running"`
- **Expected Output**: `"The cat be run"`

### Test Case 5: `test_empty_string`
- **Description**: This test checks that the `clean_lemmatizer_words` function handles an empty string correctly.
- **Input**: `""`
- **Expected Output**: `""`

### Test Case 6: `test_single_character_words`
- **Description**: This test ensures that the `clean_lemmatizer_words` function handles single character words correctly.
- **Input**: `"A b c d e f g"`
- **Expected Output**: `""`

### Test Case 7: `test_sentence_with_non_alpha_characters`
- **Description**: This test verifies that the `clean_lemmatizer_words` function removes non-alphabetic characters and lemmatizes the sentence.
- **Input**: `"Hello @world #2024"`
- **Expected Output**: `"Hello world"`

# Test Documentation for `TestCleanStemWords` in `test.py`

### Test Case 1: `test_normal_sentence`
- **Description**: This test verifies that the `clean_stem_words` function correctly stems a normal sentence.
- **Input**: `"The cats are running"`
- **Expected Output**: `"the cat are run"`

### Test Case 2: `test_sentence_with_punctuation`
- **Description**: This test checks that the `clean_stem_words` function removes punctuation and stems the sentence.
- **Input**: `"Hello, world!"`
- **Expected Output**: `"hello world"`

### Test Case 3: `test_sentence_with_numbers`
- **Description**: This test ensures that the `clean_stem_words` function removes numbers and stems the sentence.
- **Input**: `"There are 2 cats"`
- **Expected Output**: `"there are cat"`

### Test Case 4: `test_mixed_case_sentence`
- **Description**: This test verifies that the `clean_stem_words` function handles mixed case sentences and stems them correctly.
- **Input**: `"The Cats Are Running"`
- **Expected Output**: `"the cat are run"`

### Test Case 5: `test_empty_string`
- **Description**: This test checks that the `clean_stem_words` function handles an empty string correctly.
- **Input**: `""`
- **Expected Output**: `""`

### Test Case 6: `test_single_character_words`
- **Description**: This test ensures that the `clean_stem_words` function handles single character words correctly.
- **Input**: `"A b c d e f g"`
- **Expected Output**: `""`

### Test Case 7: `test_sentence_with_non_alpha_characters`
- **Description**: This test verifies that the `clean_stem_words` function removes non-alphabetic characters and stems the sentence.
- **Input**: `"Hello @world #2024"`
- **Expected Output**: `"hello world"`

# Test Documentation for `TestCleanStopWords` in `test.py`

### Test Case 1: `test_normal_sentence`
- **Description**: This test verifies that the `clean_stop_words` function correctly removes stop words from a normal sentence.
- **Input**: `"The cats are running"`
- **Expected Output**: `"cats running"`

### Test Case 2: `test_sentence_with_punctuation`
- **Description**: This test checks that the `clean_stop_words` function removes stop words and punctuation from the sentence.
- **Input**: `"Hello, world!"`
- **Expected Output**: `"Hello world"`

### Test Case 3: `test_sentence_with_numbers`
- **Description**: This test ensures that the `clean_stop_words` function removes stop words and numbers from the sentence.
- **Input**: `"There are 2 cats"`
- **Expected Output**: `"cats"`

### Test Case 4: `test_mixed_case_sentence`
- **Description**: This test verifies that the `clean_stop_words` function handles mixed case sentences and removes stop words correctly.
- **Input**: `"The Cats Are Running"`
- **Expected Output**: `"Cats Running"`

### Test Case 5: `test_empty_string`
- **Description**: This test checks that the `clean_stop_words` function handles an empty string correctly.
- **Input**: `""`
- **Expected Output**: `""`

### Test Case 6: `test_single_character_words`
- **Description**: This test ensures that the `clean_stop_words` function handles single character words correctly.
- **Input**: `"A b c d e f g"`
- **Expected Output**: `""`

### Test Case 7: `test_sentence_with_non_alpha_characters`
- **Description**: This test verifies that the `clean_stop_words` function removes stop words and non-alphabetic characters from the sentence.
- **Input**: `"Hello @world #2024"`
- **Expected Output**: `"Hello world"`

# Test Documentation for `TestCleanString` in `test.py`

### Test Case 1: `test_remove_urls`
- **Description**: This test verifies that the `clean_string` function correctly removes URLs from the input string.
- **Input**: `"Check this link http://example.com"`
- **Expected Output**: `"Check this link"`

### Test Case 2: `test_remove_hashtags`
- **Description**: This test checks that the `clean_string` function removes hashtags from the input string.
- **Input**: `"This is a #hashtag"`
- **Expected Output**: `"This is a"`

### Test Case 3: `test_remove_mentions`
- **Description**: This test ensures that the `clean_string` function removes mentions from the input string.
- **Input**: `"Mentioning @user"`
- **Expected Output**: `"Mentioning"`

### Test Case 4: `test_remove_newlines_and_carriage_returns`
- **Description**: This test verifies that the `clean_string` function removes newlines and carriage returns from the input string.
- **Input**: `"Line1\nLine2\rLine3"`
- **Expected Output**: `"Line1 Line2 Line3"`

### Test Case 5: `test_remove_tabs`
- **Description**: This test checks that the `clean_string` function removes tab characters from the input string.
- **Input**: `"This\tis\ta\ttest"`
- **Expected Output**: `"This is a test"`

### Test Case 6: `test_remove_extra_whitespace`
- **Description**: This test ensures that the `clean_string` function removes extra whitespace from the input string.
- **Input**: `"This  is   a    test"`
- **Expected Output**: `"This is a test"`

### Test Case 7: `test_remove_punctuations`
- **Description**: This test verifies that the `clean_string` function removes punctuation from the input string.
- **Input**: `"Hello, world!"`
- **Expected Output**: `"Hello world"`

### Test Case 8: `test_remove_non_ascii_characters`
- **Description**: This test checks that the `clean_string` function removes non-ASCII characters from the input string.
- **Input**: `"Hello world 😊"`
- **Expected Output**: `"Hello world"`

### Test Case 9: `test_combined_cases`
- **Description**: This test ensures that the `clean_string` function handles a combination of URLs, hashtags, mentions, newlines, tabs, punctuation, and non-ASCII characters in the input string.
- **Input**: `"Check this link http://example.com #hashtag @user\nNew line\tTab! 😊"`
- **Expected Output**: `"Check this link New line Tab"`

# Test Documentation for `TestCleanseString` in `test.py`

### Test Case 1: `test_normal_sentence`
- **Description**: This test verifies that the `cleanse_string` function correctly processes a normal sentence by removing stop words, stemming, and lemmatizing.
- **Input**: `"The cats are running"`
- **Expected Output**: `['Cat', 'run']`

### Test Case 2: `test_sentence_with_punctuation`
- **Description**: This test checks that the `cleanse_string` function removes punctuation and processes the sentence correctly.
- **Input**: `"Hello, world!"`
- **Expected Output**: `['Hello', 'world']`

### Test Case 3: `test_sentence_with_numbers`
- **Description**: This test ensures that the `cleanse_string` function removes numbers and processes the sentence correctly.
- **Input**: `"There are 2 cats"`
- **Expected Output**: `['Cat']`

### Test Case 4: `test_mixed_case_sentence`
- **Description**: This test verifies that the `cleanse_string` function handles mixed case sentences and processes them correctly.
- **Input**: `"The Cats Are Running"`
- **Expected Output**: `['Cat', 'run']`

### Test Case 5: `test_empty_string`
- **Description**: This test checks that the `cleanse_string` function handles an empty string correctly.
- **Input**: `""`
- **Expected Output**: `[]`

### Test Case 6: `test_single_character_words`
- **Description**: This test ensures that the `cleanse_string` function handles single character words correctly.
- **Input**: `"A b c d e f g"`
- **Expected Output**: `[]`

# Test Documentation for `TestCleanseText` in `test.py`

### Test Case 1: `test_remove_punctuation`
- **Description**: This test verifies that the `cleanse_text` function correctly removes punctuation from the input string.
- **Input**: `"Hello, world!"`
- **Expected Output**: `"Hello world"`

### Test Case 2: `test_empty_string`
- **Description**: This test checks that the `cleanse_text` function handles an empty string correctly.
- **Input**: `""`
- **Expected Output**: `""`

### Test Case 3: `test_string_with_only_punctuation`
- **Description**: This test ensures that the `cleanse_text` function removes all punctuation from a string that contains only punctuation characters.
- **Input**: `"!@#$%^&*()"`
- **Expected Output**: `""`

### Test Case 4: `test_string_with_mixed_content`
- **Description**: This test verifies that the `cleanse_text` function correctly processes a string with mixed content, including punctuation and escape characters.
- **Input**: `"b'Hello, world!\\r\\n"`
- **Expected Output**: `"Hello world"`

# Test Documentation for `TestDataCleansing` in `test.py`

### Test Case 1: `test_all_false`
- **Description**: This test verifies that the `data_cleansing` function returns the input string unchanged when all processing flags are set to `False`.
- **Input**: `"The cats are running"`
- **Flags**: `False, False, False, False, False`
- **Expected Output**: `"The cats are running"`

### Test Case 2: `test_run_pii`
- **Description**: This test checks that the `data_cleansing` function replaces PII (email) when the PII flag is set to `True`.
- **Input**: `"My email is example@example.com"`
- **Flags**: `True, False, False, False, False`
- **Expected Output**: `"My email is EMAIL"`

### Test Case 3: `test_run_cleanse`
- **Description**: This test ensures that the `data_cleansing` function removes punctuation when the cleanse flag is set to `True`.
- **Input**: `"Hello, world!"`
- **Flags**: `False, True, False, False, False`
- **Expected Output**: `"Hello world"`

### Test Case 4: `test_run_stop`
- **Description**: This test verifies that the `data_cleansing` function removes stop words when the stop words flag is set to `True`.
- **Input**: `"The cats are running"`
- **Flags**: `False, False, False, True, False`
- **Expected Output**: `"cats running"`
- **Additional Input**: `stop_words`

### Test Case 5: `test_run_lemm`
- **Description**: This test checks that the `data_cleansing` function lemmatizes words when the lemmatize flag is set to `True`.
- **Input**: `"The cats are running"`
- **Flags**: `False, False, True, False, False`
- **Expected Output**: `"The cat be run"`
- **Additional Input**: `lemmatizer`

### Test Case 6: `test_run_stem`
- **Description**: This test ensures that the `data_cleansing` function stems words when the stem flag is set to `True`.
- **Input**: `"The cats are running"`
- **Flags**: `False, False, False, False, True`
- **Expected Output**: `"the cat are run"`
- **Additional Input**: `stemmer`

### Test Case 7: `test_combined`
- **Description**: This test verifies that the `data_cleansing` function correctly processes the input string with all flags set to `True`.
- **Input**: `"My email is example@example.com. The cats are running!"`
- **Flags**: `True, True, True, True, True`
- **Expected Output**: `"email email cat run"`
- **Additional Input**: `stop_words, lemmatizer, stemmer`

# Test Documentation for `TestDataVaracityCheck` in `test.py`

### Test Case 1: `test_remove_insufficient_length_rows`
- **Description**: This test verifies that the `data_varacity_check` function removes rows where the text length is less than the specified minimum length.
- **Input**: 
  - DataFrame: `{'text': ['short', 'this is long enough', 'tiny', 'adequate length']}`
  - Column: `'text'`
  - Minimum Length: `5`
- **Expected Output**: 
  - DataFrame: `{'text': ['this is long enough', 'adequate length']}`

### Test Case 2: `test_convert_to_lowercase`
- **Description**: This test checks that the `data_varacity_check` function converts all text to lowercase and removes rows where the text length is less than the specified minimum length.
- **Input**: 
  - DataFrame: `{'text': ['SHORT', 'This Is Long Enough', 'TINY', 'Adequate Length']}`
  - Column: `'text'`
  - Minimum Length: `5`
- **Expected Output**: 
  - DataFrame: `{'text': ['this is long enough', 'adequate length']}`

### Test Case 3: `test_empty_dataframe`
- **Description**: This test ensures that the `data_varacity_check` function handles an empty DataFrame correctly.
- **Input**: 
  - DataFrame: `{'text': []}`
  - Column: `'text'`
  - Minimum Length: `5`
- **Expected Output**: 
  - DataFrame: `{'text': []}` (with dtype=object)

### Test Case 4: `test_all_rows_removed`
- **Description**: This test verifies that the `data_varacity_check` function removes all rows when all text lengths are less than the specified minimum length.
- **Input**: 
  - DataFrame: `{'text': ['short', 'tiny']}`
  - Column: `'text'`
  - Minimum Length: `5`
- **Expected Output**: 
  - DataFrame: `{'text': []}` (with dtype=object)

# Test Documentation for `TestDecodeNetout` in `test.py`

### Test Case: `test_decode_netout`
- **Description**: This test verifies that the `decode_netout` function correctly processes the network output and returns a list of detected objects.
- **Input**:
  - `netout`: A randomly generated numpy array of shape `(13, 13, 3, 25)`
  - `anchors`: A list of anchor box dimensions `[116, 90, 156, 198, 373, 326]`
  - `obj_thresh`: Object confidence threshold `0.5`
  - `net_h`: Network input height `416`
  - `net_w`: Network input width `416`
- **Expected Output**: The result should be an instance of `list`.
- **Assertions**:
  - `self.assertIsInstance(result, list)`: Ensures the result is a list.

  # Test Documentation for `TestMarkdownEscaper` in `test.py`

### Test Case 1: `test_escape_json`
- **Description**: This test verifies that the `markdown_escaper` function correctly escapes JSON code blocks.
- **Input**: 
  - String: `'```json{"key": "value"}```'`
  - Language: `'json'`
- **Expected Output**: `'{"key": "value"}'`

### Test Case 2: `test_escape_python`
- **Description**: This test checks that the `markdown_escaper` function correctly escapes Python code blocks.
- **Input**: 
  - String: `'```pythonprint("Hello, world!")```'`
  - Language: `'python'`
- **Expected Output**: `'print("Hello, world!")'`

### Test Case 3: `test_no_escape`
- **Description**: This test ensures that the `markdown_escaper` function returns the input string unchanged when there is no code block to escape.
- **Input**: 
  - String: `'This is a test'`
  - Language: `'json'`
- **Expected Output**: `'This is a test'`

### Test Case 4: `test_partial_escape`
- **Description**: This test verifies that the `markdown_escaper` function does not escape code blocks when the specified language does not match the code block language.
- **Input**: 
  - String: `'```json{"key": "value"}```'`
  - Language: `'python'`
- **Expected Output**: `'```json{"key": "value"}```'`

### Test Case 5: `test_empty_string`
- **Description**: This test checks that the `markdown_escaper` function handles an empty string correctly.
- **Input**: 
  - String: `''`
  - Language: `'json'`
- **Expected Output**: `''`

# Test Documentation for `TestMarkdownToJson` in `test.py`

### Test Case 1: `test_valid_json`
- **Description**: This test verifies that the `markdown_to_json` function correctly converts a valid JSON code block to a JSON object.
- **Input**: `'```json{"key": "value"}```'`
- **Expected Output**: `{"key": "value"}`

### Test Case 2: `test_invalid_json`
- **Description**: This test checks that the `markdown_to_json` function raises a `json.JSONDecodeError` when given an invalid JSON code block.
- **Input**: `'```json{"key": "value"```'`
- **Expected Output**: Raises `json.JSONDecodeError`

### Test Case 3: `test_no_escape`
- **Description**: This test ensures that the `markdown_to_json` function raises a `json.JSONDecodeError` when the input string does not contain a JSON code block.
- **Input**: `'This is a test'`
- **Expected Output**: Raises `json.JSONDecodeError`

### Test Case 4: `test_empty_string`
- **Description**: This test checks that the `markdown_to_json` function raises a `json.JSONDecodeError` when given an empty string.
- **Input**: `''`
- **Expected Output**: Raises `json.JSONDecodeError`

# Test Documentation for `TestGetFullVersion` in `test.py`

### Test Case 1: `test_standard_version`
- **Description**: This test verifies that the `get_full_version` function correctly formats a standard version number.
- **Input**: 
  - Product Name: `"Product"`
  - Major Version: `1`
  - Minor Version: `0`
  - Patch Version: `0`
- **Expected Output**: `"Product v1.0.0"`

### Test Case 2: `test_minor_update`
- **Description**: This test checks that the `get_full_version` function correctly formats a version number with a minor update.
- **Input**: 
  - Product Name: `"Product"`
  - Major Version: `1`
  - Minor Version: `1`
  - Patch Version: `0`
- **Expected Output**: `"Product v1.1.0"`

### Test Case 3: `test_patch_update`
- **Description**: This test ensures that the `get_full_version` function correctly formats a version number with a patch update.
- **Input**: 
  - Product Name: `"Product"`
  - Major Version: `1`
  - Minor Version: `0`
  - Patch Version: `1`
- **Expected Output**: `"Product v1.0.1"`

### Test Case 4: `test_major_update`
- **Description**: This test verifies that the `get_full_version` function correctly formats a version number with a major update.
- **Input**: 
  - Product Name: `"Product"`
  - Major Version: `2`
  - Minor Version: `0`
  - Patch Version: `0`
- **Expected Output**: `"Product v2.0.0"`

### Test Case 5: `test_non_standard_version_name`
- **Description**: This test checks that the `get_full_version` function correctly formats a version number for a product with a non-standard name.
- **Input**: 
  - Product Name: `"MyApp"`
  - Major Version: `3`
  - Minor Version: `2`
  - Patch Version: `1`
- **Expected Output**: `"MyApp v3.2.1"`

### Test Case 6: `test_zero_version`
- **Description**: This test ensures that the `get_full_version` function correctly formats a version number with all zero values.
- **Input**: 
  - Product Name: `"Product"`
  - Major Version: `0`
  - Minor Version: `0`
  - Patch Version: `0`
- **Expected Output**: `"Product v0.0.0"`

# Test Documentation for `TestGetVersion` in `test.py`

### Test Case 1: `test_standard_version`
- **Description**: This test verifies that the `get_version` function correctly formats a standard version number.
- **Input**: 
  - Major Version: `1`
  - Minor Version: `0`
  - Patch Version: `0`
- **Expected Output**: `"1.0.0"`

### Test Case 2: `test_minor_update`
- **Description**: This test checks that the `get_version` function correctly formats a version number with a minor update.
- **Input**: 
  - Major Version: `1`
  - Minor Version: `1`
  - Patch Version: `0`
- **Expected Output**: `"1.1.0"`

### Test Case 3: `test_patch_update`
- **Description**: This test ensures that the `get_version` function correctly formats a version number with a patch update.
- **Input**: 
  - Major Version: `1`
  - Minor Version: `0`
  - Patch Version: `1`
- **Expected Output**: `"1.0.1"`

### Test Case 4: `test_major_update`
- **Description**: This test verifies that the `get_version` function correctly formats a version number with a major update.
- **Input**: 
  - Major Version: `2`
  - Minor Version: `0`
  - Patch Version: `0`
- **Expected Output**: `"2.0.0"`

### Test Case 5: `test_zero_version`
- **Description**: This test ensures that the `get_version` function correctly formats a version number with all zero values.
- **Input**: 
  - Major Version: `0`
  - Minor Version: `0`
  - Patch Version: `0`
- **Expected Output**: `"0.0.0"`

### Test Case 6: `test_non_standard_version`
- **Description**: This test checks that the `get_version` function correctly formats a version number with non-standard values.
- **Input**: 
  - Major Version: `3`
  - Minor Version: `2`
  - Patch Version: `1`
- **Expected Output**: `"3.2.1"`

# Test Documentation for `TestPrintUsage` in `test.py`

### Test Case: `test_printusage`
- **Description**: This test verifies that the `printusage` function correctly prints the usage information and calls the `printversion` function.
- **Mocks**:
  - `MOAM.printversion`: Mocked to ensure it is called once.
  - `builtins.print`: Mocked to capture print statements.
- **Steps**:
  1. Patch `MOAM.printversion`.
  2. Patch `builtins.print`.
  3. Call `MOAM.printusage()`.
  4. Verify that `print` was called with the expected usage information.
  5. Verify that `MOAM.printversion` was called once.
- **Expected Print Calls**:
  - `unittest.mock.call("")`
  - `unittest.mock.call("  -v, --version    prints the version of this software package.")`
  - `unittest.mock.call("")`
  - `unittest.mock.call("  * - indicates required argument.")`
- **Expected Mock Assertions**:
  - `mock_print.assert_has_calls(expected_calls, any_order=False)`
  - `mock_printversion.assert_called_once()`

  # Test Documentation for `TestSetLibraryConfiguration` in `test.py`

### Test Case: `test_set_library_configuration`
- **Description**: This test verifies that the `set_library_configuration` function correctly sets the configuration options for Pandas and Numpy libraries.
- **Mocks**:
  - `MOAM.pd.set_option`: Mocked to ensure it is called with the correct arguments.
  - `MOAM.pd.options`: Mocked to ensure the display float format is set correctly.
  - `MOAM.np.set_printoptions`: Mocked to ensure it is called with the correct arguments.
  - `MOAM.debug.msg_info`: Mocked to ensure it is called with the correct message.
- **Steps**:
  1. Patch `MOAM.pd.set_option`.
  2. Patch `MOAM.pd.options`.
  3. Patch `MOAM.np.set_printoptions`.
  4. Patch `MOAM.debug.msg_info`.
  5. Call `MOAM.set_library_configuration()`.
  6. Verify that `msg_info` was called once with the message `"Setting Pandas and Numpy library options."`.
  7. Verify that `set_option` was called once with `'display.max_colwidth', 10`.
  8. Verify that `pd.options.display.float_format` was set to `'{:,.4f}'.format`.
  9. Verify that `set_printoptions` was called once with `precision=4`.
- **Expected Mock Assertions**:
  - `mock_msg_info.assert_called_once_with("Setting Pandas and Numpy library options.")`
  - `mock_set_option.assert_called_once_with('display.max_colwidth', 10)`
  - `self.assertEqual(mock_pd_options.display.float_format, '{:,.4f}'.format)`
  - `mock_set_printoptions.assert_called_once_with(precision=4)`

  # Test Documentation for `TestSplitText` in `test.py`

### Test Case 1: `test_split_text_basic`
- **Description**: This test verifies that the `split_text` function correctly splits a basic sentence into chunks of the specified size.
- **Input**: 
  - Text: `"This is a test. This is only a test."`
  - Chunk Size: `10`
- **Expected Output**: `["This is a", "test. This", "is only a", "test."]`

### Test Case 2: `test_split_text_large_sentence`
- **Description**: This test checks that the `split_text` function correctly splits a long sentence that exceeds the chunk size.
- **Input**: 
  - Text: `"This is a very long sentence that exceeds the chunk size."`
  - Chunk Size: `10`
- **Expected Output**: 
  - `["This is a", "very long", "sentence", "that", "exceeds", "the chunk", "size."]`

### Test Case 3: `test_split_text_exact_chunk_size`
- **Description**: This test ensures that the `split_text` function correctly handles a text that is exactly the chunk size.
- **Input**: 
  - Text: `"1234567890"`
  - Chunk Size: `10`
- **Expected Output**: `["1234567890"]`

### Test Case 4: `test_split_text_empty_string`
- **Description**: This test verifies that the `split_text` function correctly handles an empty string.
- **Input**: 
  - Text: `""`
  - Chunk Size: `10`
- **Expected Output**: `[]`

### Test Case 5: `test_split_text_chunk_size_greater_than_text`
- **Description**: This test checks that the `split_text` function correctly handles a chunk size that is greater than the length of the text.
- **Input**: 
  - Text: `"Short text."`
  - Chunk Size: `50`
- **Expected Output**: `["Short text."]`

# Test Documentation for `TestPromptInjectionSplitString` in `test.py`

### Test Case 1: `test_prompt_injection_split_string_basic`
- **Description**: This test verifies that the `prompt_injection_split_string` function correctly splits a basic string into chunks of the specified size.
- **Input**: 
  - String: `"This is a test string."`
  - Chunk Size: `5`
- **Expected Output**: `["This ", "is a ", "test ", "strin", "g."]`

### Test Case 2: `test_prompt_injection_split_string_exact_chunk_size`
- **Description**: This test checks that the `prompt_injection_split_string` function correctly handles a string that is exactly the chunk size.
- **Input**: 
  - String: `"12345"`
  - Chunk Size: `5`
- **Expected Output**: `["12345"]`

### Test Case 3: `test_prompt_injection_split_string_empty_string`
- **Description**: This test ensures that the `prompt_injection_split_string` function correctly handles an empty string.
- **Input**: 
  - String: `""`
  - Chunk Size: `5`
- **Expected Output**: `[]`

### Test Case 4: `test_prompt_injection_split_string_chunk_size_greater_than_string`
- **Description**: This test verifies that the `prompt_injection_split_string` function correctly handles a chunk size that is greater than the length of the string.
- **Input**: 
  - String: `"Short"`
  - Chunk Size: `10`
- **Expected Output**: `["Short"]`

### Test Case 5: `test_prompt_injection_split_string_chunk_size_one`
- **Description**: This test checks that the `prompt_injection_split_string` function correctly handles a chunk size of one.
- **Input**: 
  - String: `"ABCDE"`
  - Chunk Size: `1`
- **Expected Output**: `["A", "B", "C", "D", "E"]`

# Test Documentation for `TestPromptInjectionPredict` in `test.py`

### Test Case 1: `test_prompt_injection_predict_basic`
- **Description**: This test verifies that the `prompt_injection_predict` function correctly maps the prediction labels to their corresponding scores.
- **Mocks**:
  - `mock_pipe`: Mocked to return a list of predictions with labels and scores.
- **Input**:
  - `inc_prompt`: `"Test prompt"`
  - `id2label`: `{0: 'Label A', 1: 'Label B'}`
- **Mock Return Value**:
  - `mock_pipe.return_value`: ` [{'label': 0, 'score': 0.9}, {'label': 1, 'score': 0.1}]`
- **Expected Output**: `{'Label A': 0.9, 'Label B': 0.1}`
- **Assertions**:
  - `self.assertEqual(result, expected_output)`
  - `mock_pipe.assert_called_once_with(inc_prompt)`

### Test Case 2: `test_prompt_injection_predict_empty_result`
- **Description**: This test checks that the `prompt_injection_predict` function correctly handles an empty list of predictions.
- **Mocks**:
  - `mock_pipe`: Mocked to return an empty list.
- **Input**:
  - `inc_prompt`: `"Test prompt"`
  - `id2label`: `{0: 'Label A', 1: 'Label B'}`
- **Mock Return Value**:
  - `mock_pipe.return_value`: `[]`
- **Expected Output**: `{}`
- **Assertions**:
  - `self.assertEqual(result, expected_output)`
  - `mock_pipe.assert_called_once_with(inc_prompt)`

### Test Case 3: `test_prompt_injection_predict_unmapped_label`
- **Description**: This test ensures that the `prompt_injection_predict` function correctly handles a prediction with an unmapped label.
- **Mocks**:
  - `mock_pipe`: Mocked to return a list with an unmapped label.
- **Input**:
  - `inc_prompt`: `"Test prompt"`
  - `id2label`: `{0: 'Label A', 1: 'Label B'}`
- **Mock Return Value**:
  - `mock_pipe.return_value`: ` [{'label': 2, 'score': 0.5}]`
- **Expected Output**: `{None: 0.5}`
- **Assertions**:
  - `self.assertEqual(result, expected_output)`
  - `mock_pipe.assert_called_once_with(inc_prompt)`

  # Test Documentation for `TestDetectPromptInjection` in `test.py`

### Test Case: `test_detect_prompt_injection_exception`
- **Description**: This test verifies that the `detect_PromptInjection` function correctly handles an exception during the prediction process.
- **Mocks**:
  - `MOAM.prompt_injection_split_string`: Mocked to return a list of string chunks.
  - `MOAM.prompt_injection_predict`: Mocked to raise an exception.
  - `MOAM.process_exception`: Mocked to ensure it is called when an exception occurs.
- **Input**:
  - `inc_prompt`: `"This is a test prompt."`
  - `the_models`: `[MagicMock(), MagicMock()]`
- **Mock Return Values**:
  - `mock_split_string.return_value`: `["chunk1", "chunk2"]`
  - `mock_predict.side_effect`: `Exception("API call failed")`
- **Expected Output**:
  - `result`: `False`
  - `offending_content`: `[]`
- **Assertions**:
  - `self.assertFalse(result)`
  - `self.assertEqual(offending_content, [])`
  - `mock_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)`
  - `mock_predict.assert_called_once()`
  - `mock_process_exception.assert_called_once()`

# Test Documentation for `TestDecodeValue` in `test.py`

### Test Case 1: `test_decode_value_bytes`
- **Description**: This test verifies that the `decode_value` function correctly decodes a byte string using the `decode_text` function.
- **Input**:
  - `value`: `b'Test bytes'`
- **Mocks**:
  - `MOAM.decode_text`: Mocked to return `'Decoded text'`
- **Steps**:
  1. Patch `MOAM.decode_text` to return `'Decoded text'`.
  2. Call `MOAM.decode_value(value)`.
  3. Verify the result is `'Decoded text'`.
- **Expected Output**: `'Decoded text'`
- **Assertions**:
  - `self.assertEqual(result, "Decoded text")`

### Test Case 2: `test_decode_value_other`
- **Description**: This test checks that the `decode_value` function returns an empty string when the input is not a byte string.
- **Input**:
  - `value`: `12345`
- **Steps**:
  1. Call `MOAM.decode_value(value)`.
  2. Verify the result is an empty string.
- **Expected Output**: `""`
- **Assertions**:
  - `self.assertEqual(result, "")`

# Test Documentation for `TestPlotHistory` in `test.py`

## Test Case: `test_plot_history`
- **Description**: Verifies that the `plot_history` function correctly plots the training history and calls the appropriate matplotlib functions.
- **Input**:
  - `history_mock`: A mock object with the following history data:
    - `accuracy`: `[0.8, 0.85, 0.9]`
    - `val_accuracy`: `[0.75, 0.8, 0.85]`
    - `loss`: `[0.5, 0.4, 0.3]`
    - `val_loss`: `[0.55, 0.45, 0.35]`
- **Mocks**:
  - `mock_show`: Mocked `plt.show` function.
  - `mock_close`: Mocked `plt.close` function.
- **Steps**:
  1. Patch `MOAM.plt.show` and `MOAM.plt.close`.
  2. Create a `history_mock` object with the specified history data.
  3. Call `MOAM.plot_history(history_mock)`.
  4. Verify that `mock_show` is called twice.
  5. Verify that `mock_close` is called three times.
- **Expected Output**: None (the function does not return a value)
- **Assertions**:
  - `self.assertEqual(mock_show.call_count, 2)`
  - `self.assertEqual(mock_close.call_count, 3)`

# Test Documentation for `TestSummarizeDiagnosticsSeaborn` in `test.py`

## Test Case: `test_summarize_diagnostics_seaborn`
- **Description**: Verifies that the `summarize_diagnostics_seaborn` function correctly processes the training history and calls the appropriate seaborn and matplotlib functions.
- **Input**:
  - `history_mock`: A mock object with the following history data:
    - `accuracy`: `[0.8, 0.85, 0.9]`
    - `val_accuracy`: `[0.75, 0.8, 0.85]`
  - `title`: `"Test Title"`
- **Mocks**:
  - `mock_dataframe`: Mocked `MOAM.pd.DataFrame` function.
  - `mock_lineplot`: Mocked `MOAM.sns.lineplot` function.
  - `mock_figure`: Mocked `MOAM.plt.figure` function.
  - `mock_show`: Mocked `MOAM.plt.show` function.
- **Steps**:
  1. Patch `MOAM.pd.DataFrame`, `MOAM.sns.lineplot`, `MOAM.plt.figure`, and `MOAM.plt.show`.
  2. Create a `history_mock` object with the specified history data.
  3. Call `MOAM.summarize_diagnostics_seaborn(history_mock, title)`.
  4. Verify that `mock_dataframe` is called once with `history_mock.history`.
  5. Verify that `mock_df_instance.__getitem__` is called with `"accuracy"` and `"val_accuracy"`.
  6. Verify that `mock_lineplot` is called once.
  7. Verify that `mock_figure` is called once with `figsize=[7, 5]`.
  8. Verify that `mock_show` is called once.
- **Expected Output**: None (the function does not return a value)
- **Assertions**:
  - `mock_dataframe.assert_called_once_with(history_mock.history)`
  - `mock_df_instance.__getitem__.assert_any_call("accuracy")`
  - `mock_df_instance.__getitem__.assert_any_call("val_accuracy")`
  - `mock_lineplot.assert_called_once()`
  - `mock_figure.assert_called_once_with(figsize=[7, 5])`
  - `mock_show.assert_called_once()`

# Test Documentation for `TestReplaceEmailSpacy` in `test.py`

## Test Case 1: `test_replace_email_spacy`
- **Description**: Verifies that the `replace_email_spacy` function correctly replaces an email address in the text using the provided model and matcher.
- **Input**:
  - `inc_model`: A mock model with `max_length` set to 10.
  - `inc_matcher`: A mock matcher that returns a match at positions (0, 5).
  - `inc_text`: `"test@example.com"`
- **Mocks**:
  - `mock_re_sub`: Mocked `MOAM.re.sub` function.
  - `mock_msg_warning`: Mocked `MOAM.debug.msg_warning` function.
- **Steps**:
  1. Patch `MOAM.re.sub` and `MOAM.debug.msg_warning`.
  2. Create `inc_model` and `inc_matcher` mock objects.
  3. Set `mock_re_sub.side_effect` to replace `"test@example.com"` with `"EMAIL"`.
  4. Call `MOAM.replace_email_spacy(inc_model, inc_matcher, inc_text)`.
  5. Verify that the result is `"EMAIL"`.
  6. Verify that `inc_model`, `inc_matcher`, and `mock_re_sub` are called.
  7. Verify that `mock_msg_warning` is not called.
- **Expected Output**: `"EMAIL"`
- **Assertions**:
  - `self.assertEqual(result, "EMAIL")`
  - `inc_model.assert_called()`
  - `inc_matcher.assert_called()`
  - `mock_re_sub.assert_called()`
  - `mock_msg_warning.assert_not_called()`

## Test Case 2: `test_replace_email_spacy_exception`
- **Description**: Ensures that the `replace_email_spacy` function handles exceptions correctly and returns the original text.
- **Input**:
  - `inc_model`: A mock model that raises an exception.
  - `inc_matcher`: A mock matcher.
  - `inc_text`: `"test@example.com"`
- **Mocks**:
  - `mock_re_sub`: Mocked `MOAM.re.sub` function.
  - `mock_msg_warning`: Mocked `MOAM.debug.msg_warning` function.
- **Steps**:
  1. Patch `MOAM.re.sub` and `MOAM.debug.msg_warning`.
  2. Create `inc_model` mock object that raises an exception.
  3. Create `inc_matcher` mock object.
  4. Call `MOAM.replace_email_spacy(inc_model, inc_matcher, inc_text)`.
  5. Verify that the result is the original text `"test@example.com"`.
  6. Verify that `mock_msg_warning` is called with the appropriate warning message.
  7. Verify that `mock_re_sub` is not called.
- **Expected Output**: `"test@example.com"`
- **Assertions**:
  - `self.assertEqual(result, inc_text)`
  - `mock_msg_warning.assert_called_once_with("clean_email_spacy threw an exception: Exception('Model error')")`
  - `mock_re_sub.assert_not_called()`

  # Test Documentation for `TestCleanNamedEntityRecognition` in `test.py`

## Test Case: `test_clean_named_entity_recognition`
- **Description**: Verifies that the `clean_named_entity_recognition` function correctly replaces named entities in the text using the provided model.
- **Input**:
  - `inc_model`: A mock model with `max_length` set to 10 and returns a mock object with `ents` containing a named entity with label `'PERSON'` and text `'John Doe'`.
  - `inc_text`: `"John Doe is a software engineer."`
- **Mocks**:
  - `mock_re_sub`: Mocked `MOAM.re.sub` function.
  - `mock_msg_warning`: Mocked `MOAM.debug.msg_warning` function.
- **Steps**:
  1. Patch `MOAM.re.sub` and `MOAM.debug.msg_warning`.
  2. Create `inc_model` mock object with `max_length` set to 10 and return value containing named entity `'John Doe'`.
  3. Set `mock_re_sub.side_effect` to replace `"John Doe"` with `"PERSON"`.
  4. Call `MOAM.clean_named_entity_recognition(inc_model, inc_text)`.
  5. Verify that the result is `"PERSON is a software engineer."`.
  6. Verify that `inc_model` is called.
  7. Verify that `mock_re_sub` is called.
  8. Verify that `mock_msg_warning` is not called.
- **Expected Output**: `"PERSON is a software engineer."`
- **Assertions**:
  - `self.assertEqual(result, "PERSON is a software engineer.")`
  - `inc_model.assert_called()`
  - `mock_re_sub.assert_called()`
  - `mock_msg_warning.assert_not_called()`

# Test Documentation for `TestCleanNamedEntityRecognition` in `test.py`

## Test Case: `test_clean_named_entity_recognition`
- **Description**: Verifies that the `clean_named_entity_recognition` function correctly replaces named entities in the text using the provided model.
- **Input**:
  - `inc_model`: A mock model with `max_length` set to 10 and returns a mock object with `ents` containing a named entity with label `'PERSON'` and text `'John Doe'`.
  - `inc_text`: `"John Doe is a software engineer."`
- **Mocks**:
  - `mock_re_sub`: Mocked `MOAM.re.sub` function.
  - `mock_msg_warning`: Mocked `MOAM.debug.msg_warning` function.
- **Steps**:
  1. Patch `MOAM.re.sub` and `MOAM.debug.msg_warning`.
  2. Create `inc_model` mock object with `max_length` set to 10 and return value containing named entity `'John Doe'`.
  3. Set `mock_re_sub.side_effect` to replace `"John Doe"` with `"PERSON"`.
  4. Call `MOAM.clean_named_entity_recognition(inc_model, inc_text)`.
  5. Verify that the result is `"PERSON is a software engineer."`.
  6. Verify that `inc_model` is called.
  7. Verify that `mock_re_sub` is called.
  8. Verify that `mock_msg_warning` is not called.
- **Expected Output**: `"PERSON is a software engineer."`
- **Assertions**:
  - `self.assertEqual(result, "PERSON is a software engineer.")`
  - `inc_model.assert_called()`
  - `mock_re_sub.assert_called()`
  - `mock_msg_warning.assert_not_called()`

# Test Documentation for `TestDetectAddress` in `test.py`

## Test Case: `test_detect_address`
- **Description**: Verifies that the `detect_address` function correctly identifies and formats the address including the ZIP code.
- **Input**:
  - `inc_text`: `"123 Main St, Springfield, IL 62704"`
  - `inc_model`: A mock model that returns named entities for `Springfield` and `IL`.
- **Mocks**:
  - `mock_re_compile`: Mocked `re.compile` function.
  - `mock_msg_warning`: Mocked `MOAM.debug.msg_warning` function.
  - `mock_usaddress_tag`: Mocked `MOAM.usaddress.tag` function.
- **Steps**:
  1. Patch `MOAM.re.compile`, `MOAM.debug.msg_warning`, and `MOAM.usaddress.tag`.
  2. Create `inc_model` mock object with named entities `Springfield` and `IL`.
  3. Mock `re.compile` to return a pattern that matches the ZIP code `62704`.
  4. Mock `usaddress.tag` to return `Springfield` and `IL`.
  5. Call `MOAM.detect_address(inc_text, inc_model)`.
  6. Verify that the result is `"Springfield, IL, 62704"`.
  7. Verify that `mock_pattern.search`, `inc_model`, and `mock_usaddress_tag` are called.
  8. Verify that `mock_msg_warning` is not called.
- **Expected Output**: `"Springfield, IL, 62704"`
- **Assertions**:
  - `self.assertEqual(result, "Springfield, IL, 62704")`
  - `mock_pattern.search.assert_called_once_with(inc_text)`
  - `inc_model.assert_called_once_with(inc_text)`
  - `mock_usaddress_tag.assert_called_once_with(inc_text, tag_mapping={'PlaceName': 'city', 'StateName': 'state'})`
  - `mock_msg_warning.assert_not_called()`

## Test Case: `test_detect_address_no_zipcode`
- **Description**: Verifies that the `detect_address` function correctly identifies and formats the address without a ZIP code.
- **Input**:
  - `inc_text`: `"123 Main St, Springfield, IL"`
  - `inc_model`: A mock model that returns named entities for `Springfield` and `IL`.
- **Mocks**:
  - `mock_re_compile`: Mocked `re.compile` function.
  - `mock_msg_warning`: Mocked `MOAM.debug.msg_warning` function.
  - `mock_usaddress_tag`: Mocked `MOAM.usaddress.tag` function.
- **Steps**:
  1. Patch `MOAM.re.compile`, `MOAM.debug.msg_warning`, and `MOAM.usaddress.tag`.
  2. Create `inc_model` mock object with named entities `Springfield` and `IL`.
  3. Mock `re.compile` to return a pattern that does not match any ZIP code.
  4. Mock `usaddress.tag` to return `Springfield` and `IL`.
  5. Call `MOAM.detect_address(inc_text, inc_model)`.
  6. Verify that the result is `"Springfield, IL, "`.
  7. Verify that `mock_pattern.search`, `inc_model`, and `mock_usaddress_tag` are called.
  8. Verify that `mock_msg_warning` is not called.
- **Expected Output**: `"Springfield, IL, "`
- **Assertions**:
  - `self.assertEqual(result, "Springfield, IL, ")`
  - `mock_pattern.search.assert_called_once_with(inc_text)`
  - `inc_model.assert_called_once_with(inc_text)`
  - `mock_usaddress_tag.assert_called_once_with(inc_text, tag_mapping={'PlaceName': 'city', 'StateName': 'state'})`
  - `mock_msg_warning.assert_not_called()`

## Test Case: `test_detect_address_exception`
- **Description**: Ensures that the `detect_address` function handles exceptions correctly and returns the address without a ZIP code.
- **Input**:
  - `inc_text`: `"123 Main St, Springfield, IL"`
  - `inc_model`: A mock model that returns named entities for `Springfield` and `IL`.
- **Mocks**:
  - `mock_re_compile`: Mocked `re.compile` function.
  - `mock_msg_warning`: Mocked `MOAM.debug.msg_warning` function.
  - `mock_usaddress_tag`: Mocked `MOAM.usaddress.tag` function that raises an exception.
- **Steps**:
  1. Patch `MOAM.re.compile`, `MOAM.debug.msg_warning`, and `MOAM.usaddress.tag`.
  2. Create `inc_model` mock object with named entities `Springfield` and `IL`.
  3. Mock `re.compile` to return a pattern that does not match any ZIP code.
  4. Mock `usaddress.tag` to raise an exception.
  5. Call `MOAM.detect_address(inc_text, inc_model)`.
  6. Verify that the result is `"Springfield, IL, "`.
  7. Verify that `mock_pattern.search`, `inc_model`, and `mock_usaddress_tag` are called.
  8. Verify that `mock_msg_warning` is called with the appropriate warning message.
- **Expected Output**: `"Springfield, IL, "`
- **Assertions**:
  - `self.assertEqual(result, "Springfield, IL, ")`
  - `mock_pattern.search.assert_called_once_with(inc_text)`
  - `inc_model.assert_called_once_with(inc_text)`
  - `mock_usaddress_tag.assert_called_once_with(inc_text, tag_mapping={'PlaceName': 'city', 'StateName': 'state'})`
  - `mock_msg_warning.assert_called_once_with("ADDRESS processing encountered a problem: usaddress error")`

# Test Documentation for `TestDetectLocations` in `test.py`

### Test Case 1: `test_detect_locations`
- **Description**: This test verifies that the `detect_locations` function correctly identifies geographical locations (GPE) from a single chunk of text.
- **Input**:
  - `inc_prompt`: `"New York is a city in the United States. Paris is the capital of France."`
- **Mocks**:
  - `MOAM.prompt_injection_split_string`: Mocked to return `[inc_prompt]`
  - `inc_model`: Mocked to return entities labeled as 'GPE' for "New York" and "Paris"
- **Steps**:
  1. Patch `MOAM.prompt_injection_split_string` to return `[inc_prompt]`.
  2. Patch `inc_model` to return entities labeled as 'GPE' for "New York" and "Paris".
  3. Call `MOAM.detect_locations(inc_prompt, inc_model)`.
  4. Verify the result is `["New York", "Paris"]`.
- **Expected Output**: `["New York", "Paris"]`
- **Assertions**:
  - `self.assertEqual(result, ["New York", "Paris"])`
  - `mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)`
  - `inc_model.assert_called_once_with(inc_prompt)`
  - `mock_process_exception.assert_not_called()`

### Test Case 2: `test_detect_locations_multiple_chunks`
- **Description**: This test verifies that the `detect_locations` function correctly identifies geographical locations (GPE) from multiple chunks of text.
- **Input**:
  - `inc_prompt`: `"New York is a city in the United States. Paris is the capital of France."`
- **Mocks**:
  - `MOAM.prompt_injection_split_string`: Mocked to return `["New York is a city in the United States.", "Paris is the capital of France."]`
  - `inc_model`: Mocked to return entities labeled as 'GPE' for "New York" in the first chunk and "Paris" in the second chunk
- **Steps**:
  1. Patch `MOAM.prompt_injection_split_string` to return `["New York is a city in the United States.", "Paris is the capital of France."]`.
  2. Patch `inc_model` to return entities labeled as 'GPE' for "New York" in the first chunk and "Paris" in the second chunk.
  3. Call `MOAM.detect_locations(inc_prompt, inc_model)`.
  4. Verify the result is `["New York", "Paris"]`.
- **Expected Output**: `["New York", "Paris"]`
- **Assertions**:
  - `self.assertEqual(result, ["New York", "Paris"])`
  - `mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)`
  - `self.assertEqual(inc_model.call_count, 2)`
  - `mock_process_exception.assert_not_called()`

### Test Case 3: `test_detect_locations_exception`
- **Description**: This test verifies that the `detect_locations` function handles exceptions raised by the model and returns an empty list.
- **Input**:
  - `inc_prompt`: `"New York is a city in the United States. Paris is the capital of France."`
- **Mocks**:
  - `MOAM.prompt_injection_split_string`: Mocked to return `[inc_prompt]`
  - `inc_model`: Mocked to raise an exception with the message "Model error"
- **Steps**:
  1. Patch `MOAM.prompt_injection_split_string` to return `[inc_prompt]`.
  2. Patch `inc_model` to raise an exception with the message "Model error".
  3. Call `MOAM.detect_locations(inc_prompt, inc_model)`.
  4. Verify the result is an empty list.
- **Expected Output**: `[]`
- **Assertions**:
  - `self.assertEqual(result, [])`
  - `mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)`
  - `inc_model.assert_called_once_with(inc_prompt)`
  - `mock_process_exception.assert_called_once_with("ERROR finding organizations as follows: Model error")`

# Test Documentation for `TestDetectOrganizations` in `test.py`

### Test Case 1: `test_detect_organizations`
- **Description**: This test verifies that the `detect_organizations` function correctly identifies organizations (ORG) from a single chunk of text.
- **Input**:
  - `inc_prompt`: `"Google and Microsoft are leading tech companies."`
- **Mocks**:
  - `MOAM.prompt_injection_split_string`: Mocked to return `[inc_prompt]`
  - `inc_model`: Mocked to return entities labeled as 'ORG' for "Google" and "Microsoft"
- **Steps**:
  1. Patch `MOAM.prompt_injection_split_string` to return `[inc_prompt]`.
  2. Patch `inc_model` to return entities labeled as 'ORG' for "Google" and "Microsoft".
  3. Call `MOAM.detect_organizations(inc_prompt, inc_model)`.
  4. Verify the result is `["Microsoft", "Google"]`.
- **Expected Output**: `["Microsoft", "Google"]`
- **Assertions**:
  - `self.assertEqual(result, ["Microsoft", "Google"])`
  - `mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)`
  - `inc_model.assert_called_once_with(inc_prompt)`
  - `mock_process_exception.assert_not_called()`

### Test Case 2: `test_detect_organizations_multiple_chunks`
- **Description**: This test verifies that the `detect_organizations` function correctly identifies organizations (ORG) from multiple chunks of text.
- **Input**:
  - `inc_prompt`: `"Google and Microsoft are leading tech companies. Apple is another major player."`
- **Mocks**:
  - `MOAM.prompt_injection_split_string`: Mocked to return `["Google and Microsoft are leading tech companies.", "Apple is another major player."]`
  - `inc_model`: Mocked to return entities labeled as 'ORG' for "Google" and "Microsoft" in the first chunk and "Apple" in the second chunk
- **Steps**:
  1. Patch `MOAM.prompt_injection_split_string` to return `["Google and Microsoft are leading tech companies.", "Apple is another major player."]`.
  2. Patch `inc_model` to return entities labeled as 'ORG' for "Google" and "Microsoft" in the first chunk and "Apple" in the second chunk.
  3. Call `MOAM.detect_organizations(inc_prompt, inc_model)`.
  4. Verify the result is `["Microsoft", "Apple", "Google"]`.
- **Expected Output**: `["Microsoft", "Apple", "Google"]`
- **Assertions**:
  - `self.assertEqual(result, ["Microsoft", "Apple", "Google"])`
  - `mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)`
  - `self.assertEqual(inc_model.call_count, 2)`
  - `mock_process_exception.assert_not_called()`

### Test Case 3: `test_detect_organizations_exception`
- **Description**: This test verifies that the `detect_organizations` function handles exceptions raised by the model and returns an empty list.
- **Input**:
  - `inc_prompt`: `"Google and Microsoft are leading tech companies."`
- **Mocks**:
  - `MOAM.prompt_injection_split_string`: Mocked to return `[inc_prompt]`
  - `inc_model`: Mocked to raise an exception with the message "Model error"
- **Steps**:
  1. Patch `MOAM.prompt_injection_split_string` to return `[inc_prompt]`.
  2. Patch `inc_model` to raise an exception with the message "Model error".
  3. Call `MOAM.detect_organizations(inc_prompt, inc_model)`.
  4. Verify the result is an empty list.
- **Expected Output**: `[]`
- **Assertions**:
  - `self.assertEqual(result, [])`
  - `mock_prompt_injection_split_string.assert_called_once_with(inc_prompt, MOAM.prompt_defense_model_chunk_size)`
  - `inc_model.assert_called_once_with(inc_prompt)`
  - `mock_process_exception.assert_called_once_with("ERROR finding organizations as follows: Model error")`

# Test Documentation for `TestCleanPII` in `test.py`

### Test Case 1: `test_clean_pii_email`
- **Description**: This test verifies that the `clean_pii` function correctly replaces email addresses with the placeholder "EMAIL".
- **Input**:
  - `inc_input`: `"Contact me at example@example.com"`
- **Expected Output**: `"Contact me at EMAIL"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 2: `test_clean_pii_credit_card`
- **Description**: This test verifies that the `clean_pii` function correctly replaces credit card numbers with the placeholder "CREDITCARD".
- **Input**:
  - `inc_input`: `"My credit card number is 1234-5678-9012-3456"`
- **Expected Output**: `"My credit card number is CREDITCARD"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 3: `test_clean_pii_link`
- **Description**: This test verifies that the `clean_pii` function correctly replaces URLs with the placeholder "URL".
- **Input**:
  - `inc_input`: `"Visit https://example.com for more info"`
- **Expected Output**: `"Visit URL for more info"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 4: `test_clean_pii_ip`
- **Description**: This test verifies that the `clean_pii` function correctly replaces IPv4 addresses with the placeholder "IP".
- **Input**:
  - `inc_input`: `"My IP address is 192.168.1.1"`
- **Expected Output**: `"My IP address is IP"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 5: `test_clean_pii_ipv6`
- **Description**: This test verifies that the `clean_pii` function correctly replaces IPv6 addresses with the placeholder "IPV6".
- **Input**:
  - `inc_input`: `"My IPv6 address is 2001:0db8:85a3:0000:0000:8a2e:0370:7334"`
- **Expected Output**: `"My IPv6 address is IPV6"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 6: `test_clean_pii_phone`
- **Description**: This test verifies that the `clean_pii` function correctly replaces phone numbers with the placeholder "PHONENUMBER".
- **Input**:
  - `inc_input`: `"Call me at (123) 456-7890"`
- **Expected Output**: `"Call me at PHONENUMBER"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 7: `test_clean_pii_street_address`
- **Description**: This test verifies that the `clean_pii` function correctly replaces street addresses with the placeholder "STREETADDRESS".
- **Input**:
  - `inc_input`: `"I live at 123 Main St."`
- **Expected Output**: `"I live at STREETADDRESS"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 8: `test_clean_pii_btc_address`
- **Description**: This test verifies that the `clean_pii` function correctly replaces Bitcoin addresses with the placeholder "BTCADDRESS".
- **Input**:
  - `inc_input`: `"My BTC address is 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"`
- **Expected Output**: `"My BTC address is BTCADDRESS"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 9: `test_clean_pii_zipcode`
- **Description**: This test verifies that the `clean_pii` function correctly replaces ZIP codes with the placeholder "PHONENUMBER".
- **Input**:
  - `inc_input`: `"My ZIP code is 12345-6789"`
- **Expected Output**: `"My ZIP code is PHONENUMBER"`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

### Test Case 10: `test_clean_pii_zipcode2`
- **Description**: This test verifies that the `clean_pii` function correctly replaces ZIP codes with the placeholder "ZIPCODE2".
- **Input**:
  - `inc_input`: `"My ZIP code is .. 12345. "`
- **Expected Output**: `"My ZIP code is .. ZIPCODE2. "`
- **Assertions**:
  - `self.assertEqual(MOAM.clean_pii(inc_input), expected_output)`

# Test Documentation for `TestReadPdPdf` in `test.py`

### Test Case 1: `test_read_pd_pdf_success`
- **Description**: This test verifies that the `read_pd_pdf` function successfully reads text from a PDF file.
- **Input**:
  - `file_path`: `"dummy.pdf"`
- **Mocks**:
  - `MOAM.os.path.isfile`: Mocked to return `True`
  - `MOAM.fitz.open`: Mocked to return a document with one page containing the text "Sample text"
  - `MOAM.debug.msg_info`: Mocked to track info messages
  - `MOAM.process_exception`: Mocked to track exceptions
- **Steps**:
  1. Patch `MOAM.os.path.isfile` to return `True`.
  2. Patch `MOAM.fitz.open` to return a mock document with one page containing the text "Sample text".
  3. Call `MOAM.read_pd_pdf("dummy.pdf")`.
  4. Verify the result is `" Sample text"`.
- **Expected Output**: `" Sample text"`
- **Assertions**:
  - `self.assertEqual(result, " Sample text")`
  - `mock_isfile.assert_called_once_with("dummy.pdf")`
  - `mock_fitz_open.assert_called_once_with("dummy.pdf")`
  - `mock_msg_info.assert_any_call(f"Entering {MOAM.__name__} read_pd_pdf")`
  - `mock_msg_info.assert_any_call(f"Exiting {MOAM.__name__} read_pd_pdf")`
  - `mock_process_exception.assert_not_called()`

### Test Case 2: `test_read_pd_pdf_file_not_found`
- **Description**: This test verifies that the `read_pd_pdf` function raises a `SystemExit` exception when the PDF file is not found.
- **Input**:
  - `file_path`: `"missing.pdf"`
- **Mocks**:
  - `MOAM.os.path.isfile`: Mocked to return `False`
  - `MOAM.process_exception`: Mocked to track exceptions
- **Steps**:
  1. Patch `MOAM.os.path.isfile` to return `False`.
  2. Call `MOAM.read_pd_pdf("missing.pdf")` and expect a `SystemExit` exception.
- **Expected Output**: `SystemExit` exception
- **Assertions**:
  - `mock_isfile.assert_called_once_with("missing.pdf")`
  - `mock_process_exception.assert_not_called()`

### Test Case 3: `test_read_pd_pdf_exception`
- **Description**: This test verifies that the `read_pd_pdf` function handles exceptions raised by `fitz.open` and returns an empty string.
- **Input**:
  - `file_path`: `"dummy.pdf"`
- **Mocks**:
  - `MOAM.os.path.isfile`: Mocked to return `True`
  - `MOAM.fitz.open`: Mocked to raise an exception with the message "Some error"
  - `MOAM.process_exception`: Mocked to track exceptions
- **Steps**:
  1. Patch `MOAM.os.path.isfile` to return `True`.
  2. Patch `MOAM.fitz.open` to raise an exception with the message "Some error".
  3. Call `MOAM.read_pd_pdf("dummy.pdf")`.
  4. Verify the result is an empty string.
- **Expected Output**: `""`
- **Assertions**:
  - `self.assertEqual(result, "")`
  - `mock_isfile.assert_called_once_with("dummy.pdf")`
  - `mock_fitz_open.assert_called_once_with("dummy.pdf")`
  - `mock_process_exception.assert_called_once_with("ERROR detected trying detect the PDF path as follows: Some error")`

  # Test Documentation for `TestReadPdf` in `test.py`

### Test Case 1: `test_read_pdf_success`
- **Description**: This test verifies that the `read_pdf` function successfully reads text from a PDF file.
- **Input**:
  - `file_path`: `"dummy.pdf"`
- **Mocks**:
  - `MOAM.os.path.isfile`: Mocked to return `True`
  - `MOAM.fitz.open`: Mocked to return a document with one page containing the text "Sample text"
  - `MOAM.debug.msg_info`: Mocked to track info messages
  - `MOAM.debug.msg_error`: Mocked to track error messages
  - `MOAM.process_exception`: Mocked to track exceptions
- **Steps**:
  1. Patch `MOAM.os.path.isfile` to return `True`.
  2. Patch `MOAM.fitz.open` to return a mock document with one page containing the text "Sample text".
  3. Call `MOAM.read_pdf("dummy.pdf")`.
  4. Verify the result is `" Sample text"`.
- **Expected Output**: `" Sample text"`
- **Assertions**:
  - `self.assertEqual(result, " Sample text")`
  - `mock_isfile.assert_called_once_with("dummy.pdf")`
  - `mock_fitz_open.assert_called_once_with("dummy.pdf")`
  - `mock_msg_info.assert_any_call(f"Entering {MOAM.__name__} read_pdf")`
  - `mock_msg_info.assert_any_call(f"Exiting {MOAM.__name__} read_pdf")`
  - `mock_process_exception.assert_not_called()`
  - `mock_msg_error.assert_not_called()`

### Test Case 2: `test_read_pdf_file_not_found`
- **Description**: This test verifies that the `read_pdf` function raises a `SystemExit` exception when the PDF file is not found.
- **Input**:
  - `file_path`: `"missing.pdf"`
- **Mocks**:
  - `MOAM.os.path.isfile`: Mocked to return `False`
  - `MOAM.debug.msg_error`: Mocked to track error messages
  - `MOAM.process_exception`: Mocked to track exceptions
- **Steps**:
  1. Patch `MOAM.os.path.isfile` to return `False`.
  2. Call `MOAM.read_pdf("missing.pdf")` and expect a `SystemExit` exception.
- **Expected Output**: `SystemExit` exception
- **Assertions**:
  - `mock_isfile.assert_called_once_with("missing.pdf")`
  - `mock_msg_error.assert_any_call("ERROR detected, the input data file for work further in the notebook is missing.  Aborting execution.")`
  - `mock_msg_error.assert_any_call("  Resolve the missing.pdf missing file and repeat.")`
  - `mock_process_exception.assert_not_called()`

### Test Case 3: `test_read_pdf_exception`
- **Description**: This test verifies that the `read_pdf` function handles exceptions raised by `fitz.open` and returns an empty string.
- **Input**:
  - `file_path`: `"dummy.pdf"`
- **Mocks**:
  - `MOAM.os.path.isfile`: Mocked to return `True`
  - `MOAM.fitz.open`: Mocked to raise an exception with the message "Some error"
  - `MOAM.process_exception`: Mocked to track exceptions
- **Steps**:
  1. Patch `MOAM.os.path.isfile` to return `True`.
  2. Patch `MOAM.fitz.open` to raise an exception with the message "Some error".
  3. Call `MOAM.read_pdf("dummy.pdf")`.
  4. Verify the result is an empty string.
- **Expected Output**: `""`
- **Assertions**:
  - `self.assertEqual(result, "")`
  - `mock_isfile.assert_called_once_with("dummy.pdf")`
  - `mock_fitz_open.assert_called_once_with("dummy.pdf")`
  - `mock_process_exception.assert_called_once_with("ERROR detected trying detect the PDF path as follows: Some error")`

# Test Documentation for `TestCalculateStringSize` in `test.py`

### Test Case 1: `test_calculate_string_size_empty_string`
- **Description**: This test verifies that the `calculate_string_size` function returns 0 for an empty string.
- **Input**:
  - `input_string`: `""`
- **Expected Output**: `0`
- **Assertions**:
  - `self.assertEqual(MOAM.calculate_string_size(""), 0)`

### Test Case 2: `test_calculate_string_size_single_word`
- **Description**: This test verifies that the `calculate_string_size` function returns 1 for a single word.
- **Input**:
  - `input_string`: `"Hello"`
- **Expected Output**: `1`
- **Assertions**:
  - `self.assertEqual(MOAM.calculate_string_size("Hello"), 1)`

### Test Case 3: `test_calculate_string_size_multiple_words`
- **Description**: This test verifies that the `calculate_string_size` function returns the correct count for multiple words.
- **Input**:
  - `input_string`: `"Hello world"`
- **Expected Output**: `2`
- **Assertions**:
  - `self.assertEqual(MOAM.calculate_string_size("Hello world"), 2)`

### Test Case 4: `test_calculate_string_size_with_punctuation`
- **Description**: This test verifies that the `calculate_string_size` function correctly counts words separated by punctuation.
- **Input**:
  - `input_string`: `"Hello, world!"`
- **Expected Output**: `4`
- **Assertions**:
  - `self.assertEqual(MOAM.calculate_string_size("Hello, world!"), 4)`

### Test Case 5: `test_calculate_string_size_with_numbers`
- **Description**: This test verifies that the `calculate_string_size` function correctly counts words in a string containing numbers.
- **Input**:
  - `input_string`: `"There are 2 apples"`
- **Expected Output**: `4`
- **Assertions**:
  - `self.assertEqual(MOAM.calculate_string_size("There are 2 apples"), 4)`

### Test Case 6: `test_calculate_string_size_with_special_characters`
- **Description**: This test verifies that the `calculate_string_size` function correctly counts words in a string containing special characters.
- **Input**:
  - `input_string`: `"Hello @world #2023"`
- **Expected Output**: `5`
- **Assertions**:
  - `self.assertEqual(MOAM.calculate_string_size("Hello @world #2023"), 5)`

# Test Documentation for `TestGetMetrics` in `test.py`

### Test Case 1: `test_get_metrics_success`
- **Description**: This test verifies that the `get_metrics` function correctly calculates metrics for the given DataFrame and source columns.
- **Input**:
  - `df`: DataFrame with data `{'col1': ['Hello world', 'Test string', 'Another example']}`
  - `source_columns`: `['col1']`
- **Mocks**:
  - `MOAM.calculate_string_size`: Mocked to return the number of words in a string
  - `MOAM.tqdm`: Mocked to return the input iterable
  - `MOAM.debug.msg_debug`: Mocked to track debug messages
  - `MOAM.process_exception`: Mocked to track exceptions
- **Steps**:
  1. Patch `MOAM.calculate_string_size` to return the number of words in a string.
  2. Patch `MOAM.tqdm` to return the input iterable.
  3. Create a DataFrame with data `{'col1': ['Hello world', 'Test string', 'Another example']}`.
  4. Call `MOAM.get_metrics(df, ['col1'])`.
  5. Verify that `MOAM.calculate_string_size` is called with each string in the DataFrame.
  6. Verify that debug messages are logged correctly.
  7. Verify that no exceptions are processed.
- **Expected Output**: Metrics calculated and debug messages logged
- **Assertions**:
  - `mock_calculate_string_size.assert_any_call('Hello world')`
  - `mock_calculate_string_size.assert_any_call('Test string')`
  - `mock_calculate_string_size.assert_any_call('Another example')`
  - `mock_msg_debug.assert_any_call(f"Metrics on tokens for col1.\n")`
  - `mock_msg_debug.assert_any_call(f"..records: {3:>30,}")`
  - `mock_msg_debug.assert_any_call(f"......max: {2:>30,}")`
  - `mock_msg_debug.assert_any_call(f"......avg: {2:>30,}")`
  - `mock_msg_debug.assert_any_call(f"......min: {2:>30,}")`
  - `mock_process_exception.assert_not_called()` 