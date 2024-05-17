import pandas as pd
import date

class DateTimeHandler:
    def __init__(self) -> None:
        '''TODO: Implementation'''
        pass
    
    def convert_date_to_strings(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def extract_components(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def reformat_date(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def calculate_datetime_differences(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def convert_datetime_to_different_timezones(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def shift_time(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...
        
    def handle_irregular_time_intervals(self, dataframe:pd.DataFrame, column=0) -> pd.DataFrame:
        ...