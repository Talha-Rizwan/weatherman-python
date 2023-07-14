import csv
import glob
import math
import os

class Parser:
    def __init__(self):
        self.path = None

    def read_file_for_bar_chart(self, file_path):
        with open(file_path) as file:
            all_data_rows = csv.DictReader(file)
            all_month_temperature_values = []

            for weather_data_of_single_row in all_data_rows:
                daily_temperature_values = self.extract_temperatures_from_the_dataset_row(weather_data_of_single_row)
                all_month_temperature_values.append(daily_temperature_values)
            return all_month_temperature_values

    def extract_temperatures_from_the_dataset_row(self, weather_data_of_single_row):
        daily_temperature_values = {
                    'highest_temperature' : 0, 
                    'lowest_temperature' : 0, 
                }

        if weather_data_of_single_row['Max TemperatureC'] != '':
            daily_temperature_values['highest_temperature'] = int(weather_data_of_single_row['Max TemperatureC'])
        else:
            daily_temperature_values['highest_temperature'] = None

        if weather_data_of_single_row['Min TemperatureC'] != '':
            daily_temperature_values['lowest_temperature'] = int(weather_data_of_single_row['Min TemperatureC'])
        else:
            daily_temperature_values['lowest_temperature'] = None
        
        return daily_temperature_values

    def generate_file_path(self, arguments):
        List_split = arguments.date.split('/')
        month = self.find_month_name(int(List_split[1]))
        year = List_split[0]

        if int(year) > 0:
            self.path = f'{arguments.file_path}weatherfiles/Murree_weather_{year}{month}.txt'
        else :
            print('invalid year entered')

    def isPathExist(self):
        return os.path.exists(self.path)

    def find_month_name(self, month_number):
        MONTH_NAMES = {
            1: '_Jan',
            2: '_Feb',
            3: '_Mar',
            4: '_Apr',
            5: '_May',
            6: '_Jun',
            7: '_Jul',
            8: '_Aug',
            9: '_Sep',
            10: '_Oct',
            11: '_Nov',
            12: '_Dec'
        }

        if month_number < 1 or month_number > 12:
            print('Invalid input format entered')
            return 0

        return MONTH_NAMES[month_number]

    def read_file(self, file_path):
        all_daily_temperature_values = []
        with open(file_path) as file:
            all_data_rows = csv.DictReader(file)
            
            for weather_data_of_single_row in all_data_rows:
                daily_temperature_values = self.extract_required_weatherdata_from_dataset(weather_data_of_single_row)
                all_daily_temperature_values.append(daily_temperature_values)
            return all_daily_temperature_values

    def extract_required_weatherdata_from_dataset(self, weather_data_of_single_row):    
        return {
        'highest_temperature' : weather_data_of_single_row['Max TemperatureC'], 
        'lowest_temperature' : weather_data_of_single_row['Min TemperatureC'], 
        'maximum_humidity' : weather_data_of_single_row[' Mean Humidity'],
        }

    def read_file_for_yearly_weather(self, command_line_arguments):
        file_paths = self.get_files(command_line_arguments)
        all_months_weather_values = []
        for file in file_paths:
            with open(file) as file:
                all_data_rows = csv.DictReader(file)
                
                monthly_temperature_values = self.initialize_temperature_values()

                this_month_weather_values = self.read_file_line_by_line(all_data_rows, monthly_temperature_values)
                all_months_weather_values.append(this_month_weather_values)
        return all_months_weather_values
    
    def get_files(self, command_line_arguments):
        return glob.glob(f'{command_line_arguments.file_path}weatherfiles/Murree_weather_{command_line_arguments.date}_???.txt')

    def initialize_temperature_values(self):
        return {
        'highest_temperature' : {'value' : -math.inf, 'date' : None }, 
        'lowest_temperature' : {'value' : math.inf, 'date' : None }, 
        'maximum_humidity' : {'value' : -math.inf, 'date' : None }
        }
    
    def read_file_line_by_line(self, all_data_rows, monthly_temperature_values):
        for weather_data_of_single_row in all_data_rows:
            daily_temperature_values = self.extract_required_weatherdata_from_dataset_of_yearly \
                                                                (weather_data_of_single_row)
            self.compare_daily_with_monthly_weather_values(daily_temperature_values, 
                                                    monthly_temperature_values)
        return monthly_temperature_values

    def extract_required_weatherdata_from_dataset_of_yearly(self, weather_data_of_single_row):
        return  {
                'highest_temperature' : int(weather_data_of_single_row['Max TemperatureC']), 
                'lowest_temperature' : int(weather_data_of_single_row['Min TemperatureC']), 
                'maximum_humidity' : int(weather_data_of_single_row[' Mean Humidity']),
                'date_of_the_day' : weather_data_of_single_row['PKT']
            }
    
    def compare_daily_with_monthly_weather_values(self, daily_temperature_values, monthly_temperature_values):
        self.compare_temperature_for_single_attribute_of_daily_to_monthly(
            daily_temperature_values,
            monthly_temperature_values,
            'highest_temperature'
        )
        self.compare_temperature_for_single_attribute_of_daily_to_monthly(daily_temperature_values, 
                                                                    monthly_temperature_values, 
                                                                    'lowest_temperature')
        self.compare_temperature_for_single_attribute_of_daily_to_monthly(daily_temperature_values, 
                                                                    monthly_temperature_values, 
                                                                    'maximum_humidity')

    def compare_temperature_for_single_attribute_of_daily_to_monthly(
            self, daily_temperature_values,
            monthly_temperature_values,
            key_attribute
            ):
        
        if key_attribute == 'lowest_temperature':
            if daily_temperature_values[key_attribute] \
                        and monthly_temperature_values[key_attribute]['value'] \
                                > daily_temperature_values[key_attribute]:
                monthly_temperature_values[key_attribute]['value'] = daily_temperature_values[key_attribute]
                monthly_temperature_values[key_attribute]['date'] = daily_temperature_values['date_of_the_day']
        else:
            if daily_temperature_values[key_attribute] \
                        and monthly_temperature_values[key_attribute]['value'] \
                                < daily_temperature_values[key_attribute]:
                monthly_temperature_values[key_attribute]['value'] = daily_temperature_values[key_attribute]
                monthly_temperature_values[key_attribute]['date'] = daily_temperature_values['date_of_the_day']