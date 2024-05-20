from typing import Union
import pandas as pd

class OutlierHandler:
    def __init__(self) -> None:
        pass
    
    def identify_outliers_iqr(self, dataframe: pd.DataFrame, column: str, threshold: float = 1.5) -> pd.DataFrame:
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        
        outliers = dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)]
        return outliers
    
    def handle_outliers_iqr(self, dataframe: pd.DataFrame, column: str, threshold: float = 1.5, replacement: Union[None, float, int, str] = None) -> pd.DataFrame:
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        
        if replacement is None:
            dataframe = dataframe[(dataframe[column] >= lower_bound) & (dataframe[column] <= upper_bound)]
        else:
            dataframe.loc[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound), column] = replacement
        
        return dataframe
