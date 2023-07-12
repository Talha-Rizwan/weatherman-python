import sys
import os

RED = '\033[0;31m'
BLUE = '\033[34m'
RESET = '\033[0m'

def individual_bar_charts_for_highest_and_lowest_temperature_of_month():
    month_and_year = read_arguments()
    List_split = month_and_year.split('/')
    month = find_month_name(int(List_split[1]))
    year = List_split[0]
    path = generate_file_path(year, month)

    if month != 0 and os.path.exists(path):
        read_file(path)
    else:
        print('invalid arguments format')
        

def read_arguments():
    arguments = sys.argv

    if len(arguments) > 2:
        return arguments[2]
    
    
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


def generate_file_path(year, month):
    return f'weatherfiles/Murree_weather_{year}{month}.txt'


def extract_temperatures_from_the_dataset_row(weather_data_of_single_row):
    daily_temperature_values = {
                'highest_temperature' : 0, 
                'lowest_temperature' : 0, 
            }
    
    all_feature_of_the_dataset = weather_data_of_single_row.split(',')

    if all_feature_of_the_dataset[1] != '':
        daily_temperature_values['highest_temperature'] = int(all_feature_of_the_dataset[1].strip())
    else:
        daily_temperature_values['highest_temperature'] = None

    if all_feature_of_the_dataset[3] != '':
        daily_temperature_values['lowest_temperature'] = int(all_feature_of_the_dataset[3].strip())
    else:
        daily_temperature_values['lowest_temperature'] = None
    
    return daily_temperature_values


def generate_bar_chart_for_each_value(day_number,temperature_value, color):

    if temperature_value is not None:
        display_horizontal_bar_chart(day_number, temperature_value, color)
    else:
        print(f'{day_number}: No Data ')


def read_file(file_path):
    with open(file_path,'r') as file:
        next(file)
        
        day_number = 1
        for weather_data_of_single_row in file:
            daily_temperature_values = extract_temperatures_from_the_dataset_row(weather_data_of_single_row)
            
            generate_bar_chart_for_each_value(day_number, 
                                              daily_temperature_values['highest_temperature'], 
                                              RED)
            generate_bar_chart_for_each_value(day_number, 
                                              daily_temperature_values['lowest_temperature'], 
                                              BLUE)
            day_number += 1


def display_horizontal_bar_chart(day_number,value, color):
    print(f'{day_number}: ', end = '')
    for idx in range(value):
        print(f"{color}+{RESET}", end='')
    print(f' {value}C')
