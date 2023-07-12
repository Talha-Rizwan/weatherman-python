import sys
import os
import math
import csv


def get_yearly_temperature_stats():
    year = get_year_from_arguments()
    yearly_temperature_values = initialize_temperature_values()    
    read_file(yearly_temperature_values, year)


def get_year_from_arguments():
    arguments = sys.argv

    if len(arguments) > 2:
        return arguments[2]


def initialize_temperature_values():
    return {
            'highest_temperature' : {'value' : -math.inf, 'date' : None }, 
            'lowest_temperature' : {'value' : math.inf, 'date' : None }, 
            'maximum_humidity' : {'value' : -math.inf, 'date' : None }
            }


def read_file(yearly_temperature_values, year):
    for month_number in range(1, 13):
        month = find_month_name(month_number)
        file_path = generate_file_path(year, month)
        

        if os.path.exists(file_path):
            with open(file_path) as file:
                all_data_rows = csv.DictReader(file)
                
                monthly_temperature_values = initialize_temperature_values()

                read_file_line_by_line(all_data_rows, monthly_temperature_values)
                compare_monthly_with_yearly_weather_values(monthly_temperature_values, yearly_temperature_values)
              
    display_results(yearly_temperature_values)


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
    

def read_file_line_by_line(all_data_rows, monthly_temperature_values):
    for weather_data_of_single_row in all_data_rows:
        daily_temperature_values = extract_required_weatherdata_from_dataset \
                                                            (weather_data_of_single_row)
        compare_daily_with_monthly_weather_values(daily_temperature_values, 
                                                  monthly_temperature_values)


def extract_required_weatherdata_from_dataset(weather_data_of_single_row):
    return  {
                'highest_temperature' : int(weather_data_of_single_row['Max TemperatureC']), 
                'lowest_temperature' : int(weather_data_of_single_row['Min TemperatureC']), 
                'maximum_humidity' : int(weather_data_of_single_row[' Mean Humidity']),
                'date_of_the_day' : weather_data_of_single_row['PKT']
            }


def compare_temperature_for_single_attribute_of_daily_to_monthly(daily_temperature_values,
                                                                 monthly_temperature_values,
                                                                 key_attribute):
    
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


def compare_daily_with_monthly_weather_values(daily_temperature_values, monthly_temperature_values):
    compare_temperature_for_single_attribute_of_daily_to_monthly(daily_temperature_values,
                                                                monthly_temperature_values,
                                                                'highest_temperature')
    compare_temperature_for_single_attribute_of_daily_to_monthly(daily_temperature_values, 
                                                                 monthly_temperature_values, 
                                                                 'lowest_temperature')
    compare_temperature_for_single_attribute_of_daily_to_monthly(daily_temperature_values, 
                                                                 monthly_temperature_values, 
                                                                 'maximum_humidity')


def compare_temperature_for_single_attribute_of_monthly_to_yearly(monthly_temperature_values, 
                                                                  yearly_temperature_values, 
                                                                  key_attribute):

    if key_attribute == 'lowest_temperature':
        if monthly_temperature_values[key_attribute]['value'] \
                < yearly_temperature_values[key_attribute]['value']:
            yearly_temperature_values[key_attribute]['value'] \
                    = monthly_temperature_values[key_attribute]['value']
            yearly_temperature_values[key_attribute]['date'] \
                    = monthly_temperature_values[key_attribute]['date']
    else:
        if monthly_temperature_values[key_attribute]['value'] \
                > yearly_temperature_values[key_attribute]['value']:
            yearly_temperature_values[key_attribute]['value'] \
                    = monthly_temperature_values[key_attribute]['value']
            yearly_temperature_values[key_attribute]['date'] \
                    = monthly_temperature_values[key_attribute]['date']

     
def compare_monthly_with_yearly_weather_values(monthly_temperature_values,
                                               yearly_temperature_values ):    
    compare_temperature_for_single_attribute_of_monthly_to_yearly \
        (monthly_temperature_values, yearly_temperature_values, 'highest_temperature')
    compare_temperature_for_single_attribute_of_monthly_to_yearly \
        (monthly_temperature_values, yearly_temperature_values, 'lowest_temperature')
    compare_temperature_for_single_attribute_of_monthly_to_yearly \
        (monthly_temperature_values, yearly_temperature_values, 'maximum_humidity')


def set_date_to_correct_format(date):
    date_components = date.split('-')
    return f'{find_month_name(int(date_components[1])).replace("_", "")} {date_components[2]}'
    
    
def display_results(yearly_temperature_values):
    
    if yearly_temperature_values['highest_temperature']['date'] is not None \
            and yearly_temperature_values['lowest_temperature']['date'] is not None \
                and yearly_temperature_values['maximum_humidity']['date'] is not None:
        print(f'Highest: {yearly_temperature_values["highest_temperature"]["value"]}C on {set_date_to_correct_format(yearly_temperature_values["highest_temperature"]["date"]) } ')
        print(f'Lowest: {yearly_temperature_values["lowest_temperature"]["value"]}C on {set_date_to_correct_format(yearly_temperature_values["lowest_temperature"]["date"])} ')
        print(f'Humid: {yearly_temperature_values["maximum_humidity"]["value"]}C on {set_date_to_correct_format(yearly_temperature_values["maximum_humidity"]["date"])} ')
    else:
        print('no data to display')