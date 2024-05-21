import unittest
import pandas as pd
from datetime import datetime, timedelta
import pytz
from clean_panda.date_time_handler import DateTimeHandler

class TestDateTimeHandler(unittest.TestCase):
    
    def setUp(self):
        '''Set up the test data and the DateTimeHandler instance.'''
        self.handler = DateTimeHandler()
        self.data = {
            'date': [
                datetime(2023, 1, 1, 12, 0, 0),
                datetime(2023, 1, 2, 13, 30, 0),
                datetime(2023, 1, 3, 15, 45, 0),
                pd.NaT
            ]
        }
        self.df = pd.DataFrame(self.data)
    
    def test_convert_date_to_strings(self):
        df_result = self.handler.convert_date_to_strings(self.df.copy(), column=0)
        expected_result = pd.DataFrame({
            'date': [
                '2023-01-01 12:00:00',
                '2023-01-02 13:30:00',
                '2023-01-03 15:45:00',
                pd.NaT
            ]
        })
        pd.testing.assert_frame_equal(df_result, expected_result)
    
    def test_extract_components(self):
        df_result = self.handler.extract_components(self.df.copy(), column=0)
        expected_result = pd.DataFrame({
            'date': self.data['date'],
            'year': [2024, 2023, 2023, None],
            'month': [1, 1, 1, None],
            'day': [1, 2, 3, None],
            'hour': [12, 13, 15, None],
            'minute': [0, 30, 45, None],
            'second': [0, 0, 0, None]
        })
        pd.testing.assert_frame_equal(df_result, expected_result)
    
    def test_reformat_date(self):
        df_result = self.handler.reformat_date(self.df.copy(), column=0)
        expected_result = pd.DataFrame({
            'date': [
                '01-01-2023 12:00:00',
                '02-01-2023 13:30:00',
                '03-01-2023 15:45:00',
                pd.NaT
            ]
        })
        pd.testing.assert_frame_equal(df_result, expected_result)
    
    def test_calculate_datetime_differences(self):
        df_result = self.handler.calculate_datetime_differences(self.df.copy(), column=0)
        expected_result = pd.DataFrame({
            'date': self.data['date'],
            'time_diff': [None, 90000.0, 81300.0, None]  # Differences in seconds
        })
        pd.testing.assert_frame_equal(df_result, expected_result)
    
    def test_convert_datetime_to_different_timezones(self):
        df_result = self.handler.convert_datetime_to_different_timezones(self.df.copy(), column=0, from_tz='UTC', to_tz='America/New_York')
        expected_result = pd.DataFrame({
            'date': [
                pytz.utc.localize(datetime(2023, 1, 1, 12, 0, 0)).astimezone(pytz.timezone('America/New_York')),
                pytz.utc.localize(datetime(2023, 1, 2, 13, 30, 0)).astimezone(pytz.timezone('America/New_York')),
                pytz.utc.localize(datetime(2023, 1, 3, 15, 45, 0)).astimezone(pytz.timezone('America/New_York')),
                pd.NaT
            ]
        })
        pd.testing.assert_frame_equal(df_result, expected_result)
    
    def test_shift_time(self):
        df_result = self.handler.shift_time(self.df.copy(), column=0, shift_value=1, unit='days')
        expected_result = pd.DataFrame({
            'date': [
                datetime(2023, 1, 2, 12, 0, 0),
                datetime(2023, 1, 3, 13, 30, 0),
                datetime(2023, 1, 4, 15, 45, 0),
                pd.NaT
            ]
        })
        pd.testing.assert_frame_equal(df_result, expected_result)
    
    def test_handle_irregular_time_intervals(self):
        df_result = self.handler.handle_irregular_time_intervals(self.df.copy(), column=0)
        expected_result = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', end='2023-01-04', freq='D'),
            'data': [self.data['date'][0], self.data['date'][1], self.data['date'][2], self.data['date'][2]]  # Forward filled
        }).rename(columns={'data': 'date'})
        pd.testing.assert_frame_equal(df_result, expected_result)

if __name__ == '__main__':
    unittest.main()