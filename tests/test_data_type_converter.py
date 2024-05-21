import unittest
import pandas as pd

class TestDataTypeConverter(unittest.TestCase):

    def setUp(self):
        '''Set up the test data and the DataTypeConverter instance.'''
        self.converter = DataTypeConverter()
        self.data = {
            'numeric_column': ['1', '2', 'three', '4', '5'],
            'categorical_column': ['apple', 'banana', 'apple', 'banana', 'cherry']
        }
        self.df = pd.DataFrame(self.data)
    
    def test_convert_to_numeric(self):
        df_result = self.converter.convert_to_numeric(self.df.copy(), 'numeric_column')
        expected_result = pd.DataFrame({
            'numeric_column': [1.0, 2.0, float('nan'), 4.0, 5.0],
            'categorical_column': ['apple', 'banana', 'apple', 'banana', 'cherry']
        })
        pd.testing.assert_frame_equal(df_result, expected_result)
    
    def test_convert_to_categorical(self):
        df_result = self.converter.convert_to_categorical(self.df.copy(), 'categorical_column')
        expected_result = pd.DataFrame({
            'numeric_column': ['1', '2', 'three', '4', '5'],
            'categorical_column': pd.Categorical(['apple', 'banana', 'apple', 'banana', 'cherry'])
        })
        pd.testing.assert_frame_equal(df_result, expected_result)
        self.assertTrue(pd.api.types.is_categorical_dtype(df_result['categorical_column']))
    