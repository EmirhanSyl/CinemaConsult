import unittest
import pandas as pd
from clean_panda.categorical_encoder import label_encoding, one_hot_encoding, ordinal_encoding, binary_encoding, target_encoding

class TestEncodingMethods(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame for testing
        self.data = pd.DataFrame({
            'color': ['red', 'blue', 'green', 'blue', 'red'],
            'size': ['S', 'M', 'L', 'M', 'S'],
            'price': [10, 20, 30, 20, 10]
        })

    def test_label_encoding(self):
        df = self.data.copy()
        result = label_encoding(df, 'color')
        expected = pd.DataFrame({
            'color': [2, 0, 1, 0, 2],  # Assuming 'blue': 0, 'green': 1, 'red': 2
            'size': ['S', 'M', 'L', 'M', 'S'],
            'price': [10, 20, 30, 20, 10]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_one_hot_encoding(self):
        df = self.data.copy()
        result = one_hot_encoding(df, 'color')
        expected = pd.DataFrame({
            'size': ['S', 'M', 'L', 'M', 'S'],
            'price': [10, 20, 30, 20, 10],
            'color_blue': [0, 1, 0, 1, 0],
            'color_green': [0, 0, 1, 0, 0],
            'color_red': [1, 0, 0, 0, 1]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_ordinal_encoding(self):
        df = self.data.copy()
        result = ordinal_encoding(df, 'size')
        expected = pd.DataFrame({
            'color': ['red', 'blue', 'green', 'blue', 'red'],
            'size': [0, 1, 2, 1, 0],  # Assuming 'S': 0, 'M': 1, 'L': 2
            'price': [10, 20, 30, 20, 10]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_binary_encoding(self):
        df = self.data.copy()
        result = binary_encoding(df, 'color')
        expected = pd.DataFrame({
            'size': ['S', 'M', 'L', 'M', 'S'],
            'price': [10, 20, 30, 20, 10],
            'color_0': [0, 1, 0, 1, 0],
            'color_1': [1, 0, 1, 0, 1]
        })  # The exact expected result may vary based on the library's encoding
        pd.testing.assert_frame_equal(result, expected)

    def test_target_encoding(self):
        df = self.data.copy()
        result = target_encoding(df, 'color', 'price')
        # Manually compute the expected target encoded values based on the mean price for each color
        # 'blue': (20+20)/2 = 20, 'green': 30, 'red': (10+10)/2 = 10
        expected = pd.DataFrame({
            'color': [10, 20, 30, 20, 10],
            'size': ['S', 'M', 'L', 'M', 'S'],
            'price': [10, 20, 30, 20, 10]
        })
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()