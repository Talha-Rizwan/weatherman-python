import sys
import os
import math

class TemperatureYearlyResults:
    def __init__(self, highest_temperature_of_the_year, lowest_temperature_of_the_year, maximum_humidity_of_the_year,
                 highest_temperature_of_the_year_date, lowest_temperature_of_the_year_date,
                 maximum_humidity_of_the_year_date):
        self.highest_temperature_of_the_year = highest_temperature_of_the_year
        self.lowest_temperature_of_the_year = lowest_temperature_of_the_year
        self.maximum_humidity_of_the_year = maximum_humidity_of_the_year
        self.highest_temperature_of_the_year_date = highest_temperature_of_the_year_date
        self.lowest_temperature_of_the_year_date = lowest_temperature_of_the_year_date
        self.maximum_humidity_of_the_year_date = maximum_humidity_of_the_year_date

class TemperatureMonthlyRecords:
    def __init__(self, highest_temperature_of_the_month, lowest_temperature_of_the_month, maximum_humidity_of_the_month,
                 date_of_highest_temperature_of_the_month, date_of_lowest_temperature_of_the_month,
                 date_of_maximum_humidity_of_the_month):
        self.highest_temperature_of_the_month = highest_temperature_of_the_month
        self.lowest_temperature_of_the_month = lowest_temperature_of_the_month
        self.maximum_humidity_of_the_month = maximum_humidity_of_the_month
        self.date_of_highest_temperature_of_the_month = date_of_highest_temperature_of_the_month
        self.date_of_lowest_temperature_of_the_month = date_of_lowest_temperature_of_the_month
        self.date_of_maximum_humidity_of_the_month = date_of_maximum_humidity_of_the_month

class TemperatureDailyRecords:
    def __init__(self, highest_temperature_of_the_day, lowest_temperature_of_the_day, maximum_humidity_of_the_day,
                 date_of_the_day):
        self.highest_temperature_of_the_day = float(highest_temperature_of_the_day)
        self.lowest_temperature_of_the_day = float(lowest_temperature_of_the_day)
        self.maximum_humidity_of_the_day = float(maximum_humidity_of_the_day)
        self.date_of_the_current_day = date_of_the_day


def get_yearly_temperature_stats():
    year = get_command_line_arguments()
    yearly_temperature_values = initialize_the_temperature_result_variables()
    read_file(yearly_temperature_values, year)


def get_command_line_arguments():
    arguments = sys.argv
    if len(arguments) > 2:
        year = arguments[2]
        file_path = arguments[3]
        return year


def initialize_the_temperature_result_variables():
    return TemperatureYearlyResults(-math.inf, math.inf, -math.inf, 0, 0, 0)

def read_file(yearly_temperature_values, year):
    for i in range(1, 13):
        month = find_month_name(i)
        file_path = generate_file_path(year, month)

        if os.path.exists(file_path):

            with open(file_path, 'r') as file:
                next(file)
                
                monthly_temperature_values = initialize_the_monthly_temperature_variables()
                read_file_line_by_line(file, monthly_temperature_values)
                compare_monthly_with_yearly_weather_values(monthly_temperature_values, yearly_temperature_values)
              
    show_the_output(yearly_temperature_values)

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


def generate_file_path(year, month):
    path = 'weatherfiles/Murree_weather_'+year+month+'.txt'
    return path

def read_file_line_by_line(file, monthly_temperature_values):
    for line in file:
        daily_temperature_values = extract_the_required_dataset_features_from_row(line)
        compare_daily_with_monthly_weather_values(daily_temperature_values, monthly_temperature_values)
 
def extract_the_required_dataset_features_from_row(line):
    all_feature_of_the_dataset = line.split(',')
    daily_temperature_values = initialize_the_day_temperature_variables(all_feature_of_the_dataset[1].strip(), all_feature_of_the_dataset[3].strip(), all_feature_of_the_dataset[8].strip(), all_feature_of_the_dataset[0].strip() )
    return daily_temperature_values

def initialize_the_monthly_temperature_variables():
    return TemperatureMonthlyRecords(-math.inf, math.inf, -math.inf, 0, 0, 0)

def initialize_the_day_temperature_variables(highest_temperature, lowest_temperature, maximum_humidity, date ):
    return TemperatureDailyRecords(highest_temperature, lowest_temperature, maximum_humidity, date)

def compare_daily_with_monthly_weather_values(daily_temperature_values, monthly_temperature_values):
    if daily_temperature_values.highest_temperature_of_the_day and monthly_temperature_values.highest_temperature_of_the_month < daily_temperature_values.highest_temperature_of_the_day:
        monthly_temperature_values.highest_temperature_of_the_month = daily_temperature_values.highest_temperature_of_the_day
        monthly_temperature_values.date_of_highest_temperature_of_the_month = daily_temperature_values.date_of_the_current_day

    if daily_temperature_values.lowest_temperature_of_the_day and monthly_temperature_values.lowest_temperature_of_the_month > daily_temperature_values.lowest_temperature_of_the_day:
        monthly_temperature_values.lowest_temperature_of_the_month = daily_temperature_values.lowest_temperature_of_the_day
        monthly_temperature_values.date_of_lowest_temperature_of_the_month = daily_temperature_values.date_of_the_current_day
    
    if daily_temperature_values.maximum_humidity_of_the_day and monthly_temperature_values.maximum_humidity_of_the_month < daily_temperature_values.maximum_humidity_of_the_day:
        monthly_temperature_values.maximum_humidity_of_the_month = daily_temperature_values.maximum_humidity_of_the_day
        monthly_temperature_values.date_of_maximum_humidity_of_the_month = daily_temperature_values.date_of_the_current_day
               
def compare_monthly_with_yearly_weather_values(monthly_temperature_values, yearly_temperature_values ):
    if monthly_temperature_values.highest_temperature_of_the_month > yearly_temperature_values.highest_temperature_of_the_year:
        yearly_temperature_values.highest_temperature_of_the_year = monthly_temperature_values.highest_temperature_of_the_month
        yearly_temperature_values.highest_temperature_of_the_year_date = monthly_temperature_values.date_of_highest_temperature_of_the_month

    if monthly_temperature_values.lowest_temperature_of_the_month < yearly_temperature_values.lowest_temperature_of_the_year:
        yearly_temperature_values.lowest_temperature_of_the_year = monthly_temperature_values.lowest_temperature_of_the_month
        yearly_temperature_values.lowest_temperature_of_the_year_date = monthly_temperature_values.date_of_lowest_temperature_of_the_month

    if monthly_temperature_values.maximum_humidity_of_the_month > yearly_temperature_values.maximum_humidity_of_the_year:
        yearly_temperature_values.maximum_humidity_of_the_year = monthly_temperature_values.maximum_humidity_of_the_month
        yearly_temperature_values.maximum_humidity_of_the_year_date = monthly_temperature_values.date_of_maximum_humidity_of_the_month

def show_the_output(yearly_temperature_values):
    if yearly_temperature_values.highest_temperature_of_the_year_date != 0 and yearly_temperature_values.lowest_temperature_of_the_year_date != 0 and yearly_temperature_values.maximum_humidity_of_the_year_date:
        print(f'Highest:{yearly_temperature_values.highest_temperature_of_the_year}C on {yearly_temperature_values.highest_temperature_of_the_year_date} ')
        print(f'Lowest:{yearly_temperature_values.lowest_temperature_of_the_year}C on {yearly_temperature_values.lowest_temperature_of_the_year_date} ')
        print(f'Humid:{yearly_temperature_values.maximum_humidity_of_the_year}C on {yearly_temperature_values.maximum_humidity_of_the_year_date} ')
    else:
        print(f'no data to display')

