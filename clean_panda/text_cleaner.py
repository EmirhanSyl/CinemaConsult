import pandas as pd

class TextCleaner:
    def __init__(self) -> None:
        '''TODO: Implement'''
        pass
    
    def remove_common_words(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def convert_to_lowercase(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def remove_punctuation(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def lemmatization(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def expand_contractions(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def remove_special_characters(self, dataframe:pd.DataFrame, column=0, remove=["a"]) -> pd.DataFrame:
        ...
        
    def remove_numerical(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def filter_words(self, dataframe:pd.DataFrame, column=0, remove=["damn!"]) -> pd.DataFrame:
        ...