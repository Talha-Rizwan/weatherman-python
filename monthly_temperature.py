import sys
import os
import csv


def get_monthly_average_temperature_stats():
    command_line_arguments = get_command_line_arguments()
    path = generate_file_path( command_line_arguments)
    get_the_average_temperatures(path)


def get_command_line_arguments():
    arguments = sys.argv

    if len(arguments) > 3:
        command_line_arguments = {
            'flag' : arguments[1],
            'month_and_year' : arguments[2],
            'file_path' : arguments[3]
        }
        return command_line_arguments


    
def get_month_and_year_from_argument(month_and_year):

    if month_and_year is not None:
        List_split = split_month_and_year(month_and_year)
        month = find_month_name(int(List_split[1]))
        year = List_split[0]
        return month,year


def generate_file_path(command_line_arguments ):
    year_and_month_list = get_month_and_year_from_argument(command_line_arguments['month_and_year'])

    return f'{command_line_arguments["file_path"]}weatherfiles/Murree_weather_{year_and_month_list[1]}{year_and_month_list[0]}.txt'


def get_the_average_temperatures( path):

    if os.path.exists(path):
        read_file(path)
    else:
        print('invalid arguments format')

    
def find_month_name(month_number):
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

    
def split_month_and_year(month_and_year):
    return month_and_year.split('/')


def initialize_temperature_mean_values():
    return {
            'highest_temperature_mean' : 0, 
            'lowest_temperature_mean' :0, 
            'maximum_humidity_mean' : 0
            }


def read_file(file_path):
    with open(file_path) as file:
        temperature_sum_values = initialize_temperature_sum_values()
        all_data_rows = csv.DictReader(file)
        
        for weather_data_of_single_row in all_data_rows:
            daily_temperature_values = extract_required_weatherdata_from_dataset(weather_data_of_single_row)
            compute_the_sum_of_all_rows(temperature_sum_values, daily_temperature_values)

    mean_result_values = calculate_mean_temperature(temperature_sum_values)
    display_results(mean_result_values)
    return mean_result_values['highest_temperature_mean'], \
            mean_result_values['lowest_temperature_mean'], \
            mean_result_values['maximum_humidity_mean']


def initialize_temperature_sum_values():
    return {
            'highest_temperature' : {'sum' : 0, 'count' : 0 }, 
            'lowest_temperature' : {'sum' : 0, 'count' : 0 }, 
            'maximum_humidity' : {'sum' : 0, 'count' : 0 }
            }


def extract_required_weatherdata_from_dataset(weather_data_of_single_row):    
    return {
            'highest_temperature' : weather_data_of_single_row['Max TemperatureC'], 
            'lowest_temperature' : weather_data_of_single_row['Min TemperatureC'], 
            'maximum_humidity' : weather_data_of_single_row[' Mean Humidity'],
            }
    
def compute_sum_of_single_attribute(daily_temperature_values, temperature_sum_values, key_attribute ):

    if daily_temperature_values[key_attribute]:
        temperature_sum_values[key_attribute]['sum'] += int(daily_temperature_values[key_attribute])
        temperature_sum_values[key_attribute]['count'] += 1


def compute_the_sum_of_all_rows(temperature_sum_values, daily_temperature_values):
    compute_sum_of_single_attribute(daily_temperature_values, temperature_sum_values, 'highest_temperature')
    compute_sum_of_single_attribute(daily_temperature_values, temperature_sum_values, 'lowest_temperature')
    compute_sum_of_single_attribute(daily_temperature_values, temperature_sum_values, 'maximum_humidity')
    

def calculate_mean_temperature(temperature_sum_values):
    mean_result_values = initialize_temperature_mean_values()
    mean_result_values['highest_temperature_mean'] = Calculate_mean( temperature_sum_values['highest_temperature']['sum'], 
                                                                        temperature_sum_values['highest_temperature']['count'] )
    mean_result_values['lowest_temperature_mean'] = Calculate_mean(temperature_sum_values['lowest_temperature']['sum'],
                                                                        temperature_sum_values['lowest_temperature']['count'] ) 
    mean_result_values['maximum_humidity_mean'] = Calculate_mean( temperature_sum_values['maximum_humidity']['sum'], 
                                                                        temperature_sum_values['maximum_humidity']['count'])
    return mean_result_values


def display_results(mean_result_values):
    print(f'Highest Average: {mean_result_values["highest_temperature_mean"]}C')
    print(f'Lowest Average: {mean_result_values["lowest_temperature_mean"]}C')
    print(f'Average Humidty: {mean_result_values["maximum_humidity_mean"]}%')
    


def Calculate_mean(sum, count):
    
    if count > 0:
        return int(sum / count)