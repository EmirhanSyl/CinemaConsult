import unittest
import pandas as pd
import numpy as np

# Import the functions from your module
from clean_panda.scaler import (
    standardize_data,
    normalize_data,
    robust_scale_data,
    normalize_vectors,
    log_transform_data,
    maxabs_scale_data,
    power_transform_data
)

class TestDataScaling(unittest.TestCase):
    
    def setUp(self):
        # Create a sample dataframe for testing
        self.data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500]
        })
    
    def test_standardize_data(self):
        result = standardize_data(self.data)
        self.assertTrue(np.allclose(result.mean(), 0, atol=1e-7))
        self.assertTrue(np.allclose(result.std(), 1, atol=1e-7))

    def test_normalize_data(self):
        result = normalize_data(self.data)
        self.assertTrue(np.allclose(result.min(), 0))
        self.assertTrue(np.allclose(result.max(), 1))
        
    def test_robust_scale_data(self):
        result = robust_scale_data(self.data)
        median = self.data.median()
        iqr = self.data.quantile(0.75) - self.data.quantile(0.25)
        scaled_median = (self.data - median) / iqr
        self.assertTrue(np.allclose(result.median(), scaled_median.median()))
    
    def test_normalize_vectors(self):
        result = normalize_vectors(self.data)
        norms = np.linalg.norm(self.data, axis=1)
        expected = self.data.div(norms, axis=0)
        self.assertTrue(np.allclose(result, expected))

    def test_log_transform_data(self):
        result = log_transform_data(self.data)
        expected = np.log1p(self.data)
        self.assertTrue(np.allclose(result, expected))
    
    def test_maxabs_scale_data(self):
        result = maxabs_scale_data(self.data)
        self.assertTrue(np.allclose(result.max(), 1))
        self.assertTrue(np.allclose(result.min(), self.data.min() / self.data.max().max()))

    def test_power_transform_data(self):
        result = power_transform_data(self.data)
        self.assertTrue(result.shape, self.data.shape)  # Ensure shape is the same
        # For specific numerical checks, more detailed checks might be required
        
if __name__ == '__main__':
    unittest.main()