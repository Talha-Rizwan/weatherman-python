import csv
import glob
import math
import calendar

from constants import HIGHEST_TEMPERATURE, LOWEST_TEMPERATURE, MAXIMUM_HUMIDITY, DATE, VALUE, MAX_TEMPERATURE, MIN_TEMPERATURE, MEAN_HUMIDITY, DATE_OF_THE_DAY


class Parser:
    def __init__(self):
        self.path = None

    def read_file_for_bar_chart(self, file_path):
        with open(file_path) as file:
            all_rows_data = csv.DictReader(file)
            monthly_temperatures = []

            for weather_data_of_single_row in all_rows_data:
                daily_temperature = self.extract_temperature_from_row(weather_data_of_single_row)
                monthly_temperatures.append(daily_temperature)
            return monthly_temperatures

    def extract_temperature_from_row(self, weather_data_of_single_row):
        daily_temperature = {
                    HIGHEST_TEMPERATURE: 0,
                    LOWEST_TEMPERATURE: 0,
                }

        if weather_data_of_single_row[MAX_TEMPERATURE] != '':
            daily_temperature[HIGHEST_TEMPERATURE] = int(weather_data_of_single_row[MAX_TEMPERATURE])
        else:
            daily_temperature[HIGHEST_TEMPERATURE] = None

        if weather_data_of_single_row[MIN_TEMPERATURE] != '':
            daily_temperature[LOWEST_TEMPERATURE] = int(weather_data_of_single_row[MIN_TEMPERATURE])
        else:
            daily_temperature[LOWEST_TEMPERATURE] = None

        return daily_temperature

    def read_file(self, file_path):
        all_daily_temperature = []
        with open(file_path) as file:
            all_rows_data = csv.DictReader(file)

            for weather_data_of_single_row in all_rows_data:
                daily_temperature = self.extract_required_weatherdata_from_dataset(weather_data_of_single_row)
                all_daily_temperature.append(daily_temperature)
            return all_daily_temperature

    def extract_required_weatherdata_from_dataset(self, weather_data_of_single_row):
        return {
            HIGHEST_TEMPERATURE: weather_data_of_single_row[MAX_TEMPERATURE],
            LOWEST_TEMPERATURE: weather_data_of_single_row[MIN_TEMPERATURE],
            MAXIMUM_HUMIDITY: weather_data_of_single_row[MEAN_HUMIDITY],
        }

    def read_file_for_yearly_weather(self, command_line_arguments):
        file_paths = self.get_files(command_line_arguments)
        all_months_weather_values = []
        for file in file_paths:
            with open(file) as file:
                all_rows_data = csv.DictReader(file)
                monthly_temperature = self.initialize_temperature_values()
                this_month_weather_values = self.read_file_line_by_line(all_rows_data, monthly_temperature)
                all_months_weather_values.append(this_month_weather_values)
        return all_months_weather_values

    def get_files(self, command_line_arguments):
        return glob.glob(f'{command_line_arguments.file_path}weatherfiles/Murree_weather_{command_line_arguments.date}_???.txt')

    def get_file_path(self, arguments):
        List_split = arguments.date.split('/')
        month = calendar.month_name[int(List_split[1])]
        year = List_split[0]

        if int(year) > 0:
            self.path = glob.glob(f'{arguments.file_path}weatherfiles/Murree_weather_{year}_{month[:3]}.txt')
        else :
            print('invalid year entered')

    def initialize_temperature_values(self):
        return {
            HIGHEST_TEMPERATURE: {VALUE: -math.inf, DATE: None },
            LOWEST_TEMPERATURE: {VALUE: math.inf, DATE: None },
            MAXIMUM_HUMIDITY: {VALUE: -math.inf, DATE: None }
        }

    def read_file_line_by_line(self, all_rows_data, monthly_temperature):
        for weather_data_of_single_row in all_rows_data:
            daily_temperature = self.extract_required_weatherdata_from_dataset_of_yearly(
                weather_data_of_single_row
                )
            self.get_monthly_weather_data(
                daily_temperature,
                monthly_temperature
                )
            
        return monthly_temperature

    def extract_required_weatherdata_from_dataset_of_yearly(self, weather_data_of_single_row):
        
        if weather_data_of_single_row[MAX_TEMPERATURE] == '' or weather_data_of_single_row[MIN_TEMPERATURE] == '' or weather_data_of_single_row[MEAN_HUMIDITY] == '':
            return None

        if 'PKT' in weather_data_of_single_row.keys():
          return  {
                HIGHEST_TEMPERATURE: int(weather_data_of_single_row[MAX_TEMPERATURE]),
                LOWEST_TEMPERATURE: int(weather_data_of_single_row[MIN_TEMPERATURE]),
                MAXIMUM_HUMIDITY: int(weather_data_of_single_row[MEAN_HUMIDITY]),
                DATE_OF_THE_DAY: weather_data_of_single_row['PKT']
            }              
        else :
            return  {
                HIGHEST_TEMPERATURE: int(weather_data_of_single_row[MAX_TEMPERATURE]),
                LOWEST_TEMPERATURE: int(weather_data_of_single_row[MIN_TEMPERATURE]),
                MAXIMUM_HUMIDITY: int(weather_data_of_single_row[MEAN_HUMIDITY]),
                DATE_OF_THE_DAY: weather_data_of_single_row['PKST']
            }


    def get_monthly_weather_data(self, daily_temperature, monthly_temperature):
        if daily_temperature is not None:
            self.compare_single_attribute_temperature(
                daily_temperature,
                monthly_temperature,
                HIGHEST_TEMPERATURE
            )
            self.compare_single_attribute_temperature(
                daily_temperature,
                monthly_temperature,
                LOWEST_TEMPERATURE
                )
            self.compare_single_attribute_temperature(
                daily_temperature,
                monthly_temperature,
                MAXIMUM_HUMIDITY
                )

    def compare_single_attribute_temperature(
            self, daily_temperature,
            monthly_temperature,
            key_attribute
            ):

        if key_attribute == LOWEST_TEMPERATURE:
            if daily_temperature[key_attribute] \
                        and monthly_temperature[key_attribute][VALUE] \
                                > daily_temperature[key_attribute]:
                monthly_temperature[key_attribute][VALUE] = daily_temperature[key_attribute]
                monthly_temperature[key_attribute][DATE] = daily_temperature[DATE_OF_THE_DAY]
        else:
            if daily_temperature[key_attribute] \
                        and monthly_temperature[key_attribute][VALUE] \
                                < daily_temperature[key_attribute]:
                monthly_temperature[key_attribute][VALUE] = daily_temperature[key_attribute]
                monthly_temperature[key_attribute][DATE] = daily_temperature[DATE_OF_THE_DAY]
