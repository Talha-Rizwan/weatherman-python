import sys
import os

class TemperatureDailyRecords:
    def __init__(self, highest_temperature_of_the_day, lowest_temperature_of_the_day):
        self.highest_temperature_of_the_day = highest_temperature_of_the_day
        self.lowest_temperature_of_the_day = lowest_temperature_of_the_day


RED = '\033[0;31m'
BLUE = '\033[34m'
RESET = '\033[0m'

def combined_bar_chart_for_highest_and_lowest_temperature_of_month():
    month_and_year = read_arguments()
    List_split = split_month_and_year(month_and_year)
    month = find_month_name(int(List_split[1]))
    year = List_split[0]
    path = generate_file_path(year, month)
    if month != 0 and os.path.exists(path):
        read_file(path)
    else:
        print(f'invalid arguments format')
        

def read_arguments():
    arguments = sys.argv

    if len(arguments) > 2:
        month_and_year = arguments[2]
        file_path = arguments[3]
        return month_and_year
    

def initialize_the_day_temperature_variables(highest_temperature, lowest_temperature ):
    return TemperatureDailyRecords(highest_temperature, lowest_temperature)

    
def find_month_name(month_number):
    month_dict = {
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
        print(f'Invalid input format entered')
        return 0

    return month_dict[month_number]


def split_month_and_year(month_and_year):
    return month_and_year.split('/')


def generate_file_path(year, month):
    path = 'weatherfiles/Murree_weather_' + year + month + '.txt'
    return path


def extract_temperatures_from_the_dataset_row(line):
    daily_temperature_values = initialize_the_day_temperature_variables(0, 0)
    all_columns = line.split(',')

    if all_columns[1] != '':
        daily_temperature_values.highest_temperature_of_the_day = int(all_columns[1].strip())
    else:
        daily_temperature_values.highest_temperature_of_the_day = None

    if all_columns[3] != '':
        daily_temperature_values.lowest_temperature_of_the_day = int(all_columns[3].strip())
    else:
        daily_temperature_values.lowest_temperature_of_the_day = None
    
    return daily_temperature_values


def generate_bar_chart_for_each_value(day_number,highest_temperature, lowest_temperature):
    if highest_temperature is not None and lowest_temperature is not None :
        display_horizontal_bar_chart(day_number, highest_temperature, lowest_temperature)
    else:
        print(f'{day_number}: ')


def read_file(file_path):
    with open(file_path,'r') as file:
        next(file)
        
        day_number = 1
        for line in file:
            daily_temperature_values = extract_temperatures_from_the_dataset_row(line)
            
            generate_bar_chart_for_each_value(day_number, daily_temperature_values.highest_temperature_of_the_day, daily_temperature_values.lowest_temperature_of_the_day)
            day_number += 1


def display_horizontal_bar_chart(day_number,highest_temperature, lowest_temperature):
    print(f'{day_number}: ', end='')
    for idx in range(lowest_temperature):
        print(f'{BLUE}+{RESET}', end='')
    for idx in range(highest_temperature):
        print(f'{RED}+{RESET}', end='')
    print(f' {lowest_temperature}C-{highest_temperature}C')

