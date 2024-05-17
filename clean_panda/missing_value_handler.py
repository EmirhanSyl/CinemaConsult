from enum import Enum 
import pandas as pd
import datetime

class MissingValueHandler:
    def __init__(self):
        self.const_int = 0
        self.const_str = "NA"
        self.const_date = datetime.datetime(day=1, month=1, year=2024)
        
        
    class strategy(Enum):
        MEAN = 1
        MEDIAN = 2
        CONSTANT = 3
        REMOVE_ROW = 4
        REMOVE_COLUMN = 5
        FORWARD_BACKWARD = 6
        
    def replace_missing_values(self, dataframe:pd.DataFrame, strategy=strategy.MEAN, column=0) -> pd.DataFrame:
        ...
        
       
        
    def replace_mean(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def replace_median(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
    
    def replace_constant(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def replace_remove_row(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def replace_remove_column(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def replace_forward_backward(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...