import pandas as pd

class OutlierHandler():
    def __init__(self) -> None:
        """TODO: Implement this methods later"""
        pass
    
    def identify_outliers_iqr(self, dataframe:pd.DataFrame, threshold=1.5):
        ...
        
    def handle_outliers_iqr(self, dataframe:pd.DataFrame, threshold=1.5, replacement=None) -> pd.DataFrame:
        ...
        
    