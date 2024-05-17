import pytest
import pandas as pd
from clean_panda.missing_value_handler import MissingValueHandler

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'A': [1, 2, None, 4],
        'B': [None, 2, 3, 4],
        'C': [1, 2, 3, None]
    })

def test_replace_missing_values():
    ...