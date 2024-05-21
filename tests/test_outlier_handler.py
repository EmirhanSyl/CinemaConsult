import unittest
import pandas as pd
import numpy as np
from clean_panda.outlier_handler import OutlierHandler, identify_outliers_zscore, handle_outliers_zscore, winsorize_data

class TestOutlierHandler(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5, 100],  # Outlier at 100
            'B': [10, 20, 30, 40, 50, 60],
            'C': [100, 200, 300, 400, 500, 600]
        })
        self.handler = OutlierHandler()

    def test_identify_outliers_iqr(self):
        result = self.handler.identify_outliers_iqr(self.data, 'A')
        expected = pd.DataFrame({'A': [100], 'B': [60], 'C': [600]}, index=[5])
        pd.testing.assert_frame_equal(result, expected)

    def test_handle_outliers_iqr_remove(self):
        result = self.handler.handle_outliers_iqr(self.data, 'A')
        expected = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500]
        })
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

    def test_handle_outliers_iqr_replace(self):
        result = self.handler.handle_outliers_iqr(self.data, 'A', replacement='median')
        expected = pd.DataFrame({
            'A': [1, 2, 3, 4, 5, 3],
            'B': [10, 20, 30, 40, 50, 60],
            'C': [100, 200, 300, 400, 500, 600]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_identify_outliers_zscore(self):
        result = identify_outliers_zscore(self.data['A'])
        expected = np.array([False, False, False, False, False, True])
        np.testing.assert_array_equal(result, expected)

    def test_handle_outliers_zscore_remove(self):
        result = handle_outliers_zscore(self.data['A'])
        expected = pd.Series([1, 2, 3, 4, 5])
        pd.testing.assert_series_equal(result.reset_index(drop=True), expected)

    def test_handle_outliers_zscore_replace(self):
        result = handle_outliers_zscore(self.data['A'], replacement='median')
        expected = pd.Series([1, 2, 3, 4, 5, 3])
        pd.testing.assert_series_equal(result, expected)

    def test_winsorize_data(self):
        result = winsorize_data(self.data['A'])
        expected = pd.Series([1, 2, 3, 4, 5, 5])  # Assuming limits are (0.05, 0.05) and the 100 is changed to the next highest value in the limit
        pd.testing.assert_series_equal(result, expected)

if __name__ == '__main__':
    unittest.main()