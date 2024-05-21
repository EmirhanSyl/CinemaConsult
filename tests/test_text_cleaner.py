import unittest
import pandas as pd

# Assuming the functions are in a module named text_preprocessing
from clean_panda.text_cleaner import (
    remove_common_words,
    convert_to_lowercase,
    remove_punctuation,
    lemmatization,
    expand_contractions,
    remove_special_characters,
    remove_numerical,
    filter_words,
    remove_stopwords,
    stem_words,
    remove_html_tags,
    replace_urls
)

class TestTextPreprocessing(unittest.TestCase):

    def setUp(self):
        # Create a sample dataframe for testing
        self.data = pd.DataFrame({
            'text': [
                "This is a sample text with a URL http://example.com",
                "Here's another text with a number 1234 and an HTML tag <br>",
                "Expanding contractions like don't and won't",
                "Removing punctuation, numbers 567, and special characters $#@!",
                "Some explicit content like fuck that needs filtering"
            ]
        })
    
    def test_remove_common_words(self):
        df = self.data.copy()
        result = remove_common_words(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "sample text URL http://example.com",
                "Here's another text number 1234 HTML tag <br>",
                "Expanding contractions like don't won't",
                "Removing punctuation, numbers 567, special characters $#@!",
                "Some explicit content like fuck needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

    def test_convert_to_lowercase(self):
        df = self.data.copy()
        result = convert_to_lowercase(df, 'text')
        expected = self.data.copy()
        expected['text'] = expected['text'].str.lower()
        self.assertTrue(result.equals(expected))

    def test_remove_punctuation(self):
        df = self.data.copy()
        result = remove_punctuation(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "This is a sample text with a URL httpexamplecom",
                "Heres another text with a number 1234 and an HTML tag br",
                "Expanding contractions like dont and wont",
                "Removing punctuation numbers 567 and special characters ",
                "Some explicit content like fuck that needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

    def test_lemmatization(self):
        df = self.data.copy()
        result = lemmatization(df, 'text')
        # This test assumes that lemmatization will return the same text in this case
        # Replace this with expected lemmatized results if known
        expected = df
        self.assertTrue(result.equals(expected))

    def test_expand_contractions(self):
        df = self.data.copy()
        result = expand_contractions(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "This is a sample text with a URL http://example.com",
                "Here is another text with a number 1234 and an HTML tag <br>",
                "Expanding contractions like do not and will not",
                "Removing punctuation, numbers 567, and special characters $#@!",
                "Some explicit content like fuck that needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

    def test_remove_special_characters(self):
        df = self.data.copy()
        result = remove_special_characters(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "This is a sample text with a URL http://example.com",
                "Here's another text with a number 1234 and an HTML tag <br>",
                "Expanding contractions like don't and won't",
                "Removing punctuation numbers 567 and special characters ",
                "Some explicit content like fuck that needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

    def test_remove_numerical(self):
        df = self.data.copy()
        result = remove_numerical(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "This is a sample text with a URL http://example.com",
                "Here's another text with a number  and an HTML tag <br>",
                "Expanding contractions like don't and won't",
                "Removing punctuation, numbers , and special characters $#@!",
                "Some explicit content like fuck that needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

    def test_filter_words(self):
        df = self.data.copy()
        result = filter_words(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "This is a sample text with a URL http://example.com",
                "Here's another text with a number 1234 and an HTML tag <br>",
                "Expanding contractions like don't and won't",
                "Removing punctuation, numbers 567, and special characters $#@!",
                "Some explicit content like that needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

    def test_remove_stopwords(self):
        df = self.data.copy()
        result = remove_stopwords(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "sample text URL http://example.com",
                "Here's another text number 1234 HTML tag <br>",
                "Expanding contractions like don't won't",
                "Removing punctuation, numbers 567, special characters $#@!",
                "Some explicit content like fuck needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

    def test_stem_words(self):
        df = self.data.copy()
        result = stem_words(df, 'text')
        # This test assumes that stemming will return the same text in this case
        # Replace this with expected stemmed results if known
        expected = df
        self.assertTrue(result.equals(expected))

    def test_remove_html_tags(self):
        df = self.data.copy()
        result = remove_html_tags(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "This is a sample text with a URL http://example.com",
                "Here's another text with a number 1234 and an HTML tag ",
                "Expanding contractions like don't and won't",
                "Removing punctuation, numbers 567, and special characters $#@!",
                "Some explicit content like fuck that needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

    def test_replace_urls(self):
        df = self.data.copy()
        result = replace_urls(df, 'text')
        expected = pd.DataFrame({
            'text': [
                "This is a sample text with a URL [URL]",
                "Here's another text with a number 1234 and an HTML tag <br>",
                "Expanding contractions like don't and won't",
                "Removing punctuation, numbers 567, and special characters $#@!",
                "Some explicit content like fuck that needs filtering"
            ]
        })
        self.assertTrue(result.equals(expected))

if __name__ == '__main__':
    unittest.main()