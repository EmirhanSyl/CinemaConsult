import pandas as pd
from nltk.stem import WordNetLemmatizer

class Scaler:
    def __init__(self) -> None:
        '''Will be implemented soon...'''
        pass
    
    def standardize_data(self, dataframe:pd.DataFrame):
        ...
    
    def normalize_data(self, dataframe:pd.DataFrame):
        ...
    
    def robust_scale_data(self, dataframe:pd.DataFrame):
        ...
    
    def normalize_vectors(self, dataframe:pd.DataFrame):
        ...
        
    def log_transform_data(self, dataframe:pd.DataFrame):
        ...
        
    