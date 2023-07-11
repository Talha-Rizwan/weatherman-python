import sys
import os


class TemperatureSumResults:
    def __init__(self, highest_temperature_sum, lowest_temperature_sum, humidity_sum,
                 highest_temperature_count, lowest_temperature_count,
                 humidity_count):
        self.highest_temperature_sum = highest_temperature_sum
        self.lowest_temperature_sum = lowest_temperature_sum
        self.humidity_sum = humidity_sum
        self.highest_temperature_count = highest_temperature_count
        self.lowest_temperature_count = lowest_temperature_count
        self.humidity_count = humidity_count


class TemperatureMeanResults:
    def __init__(self, highest_temperature_mean, lowest_temperature_mean, maximum_humidity_mean,
                 ):
        self.highest_temperature_mean = highest_temperature_mean
        self.lowest_temperature_mean = lowest_temperature_mean
        self.maximum_humidity_mean = maximum_humidity_mean
        

class TemperatureDailyRecords:
    def __init__(self, highest_temperature_of_the_day, lowest_temperature_of_the_day, maximum_humidity_of_the_day):
        self.highest_temperature_of_the_day = highest_temperature_of_the_day
        self.lowest_temperature_of_the_day = lowest_temperature_of_the_day
        self.maximum_humidity_of_the_day = maximum_humidity_of_the_day


def get_monthly_average_temperature_stats():
    month_and_year = get_command_line_arguments()
    year_and_month_list = seperate_month_and_year_of_the_argument(month_and_year)
    path = generate_file_path(year_and_month_list[1], year_and_month_list[0])
    get_the_average_temperatures(year_and_month_list, path)


def get_command_line_arguments():
    arguments = sys.argv
    if len(arguments) > 2:
        month_and_year = arguments[2]
        file_path = arguments[3]
        return month_and_year
    
def seperate_month_and_year_of_the_argument(month_and_year):
    if month_and_year is not None:
        List_split = split_month_and_year(month_and_year)
        month = find_month_name(int(List_split[1]))
        year = List_split[0]
        return month,year


def generate_file_path(year, month):
    path = 'weatherfiles/Murree_weather_' + year + month + '.txt'
    return path


def get_the_average_temperatures(year_and_month_list, path):
    if year_and_month_list[0] != 0 and os.path.exists(path):
        read_file(path)
    else:
        print(f'invalid arguments format')

    
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


def read_file(file_path):

    with open(file_path,'r') as file:
        next(file)
        temperature_values = initialize_the_temperature_sum_results()

        for line in file:
            daily_temperature_values = extract_the_required_dataset_features_from_row(line)
            compute_the_sum_of_all_rows(temperature_values, daily_temperature_values)

    mean_result_values = calculate_mean_temperature(temperature_values)
    display_the_calculated_results(mean_result_values)
    return mean_result_values.highest_temperature_mean, mean_result_values.lowest_temperature_mean, mean_result_values.maximum_humidity_mean


def initialize_the_temperature_sum_results():
    return TemperatureSumResults(0,0,0,0,0,0)

def initialize_the_temperature_mean_results():
    return TemperatureMeanResults(0,0,0)

def initialize_the_day_temperature_variables(highest_temperature, lowest_temperature, maximum_humidity ):
    return TemperatureDailyRecords(highest_temperature, lowest_temperature, maximum_humidity)

def extract_the_required_dataset_features_from_row(line):
    all_feature_of_the_dataset = line.split(',')
    daily_temperature_values = initialize_the_day_temperature_variables(all_feature_of_the_dataset[1].strip(), all_feature_of_the_dataset[3].strip(), all_feature_of_the_dataset[8].strip() )
    return daily_temperature_values

def compute_the_sum_of_all_rows(temperature_values, daily_temperature_values):
    if daily_temperature_values.highest_temperature_of_the_day:
        temperature_values.highest_temperature_sum += float(daily_temperature_values.highest_temperature_of_the_day)
        temperature_values.highest_temperature_count += 1

    if daily_temperature_values.lowest_temperature_of_the_day:
        temperature_values.lowest_temperature_sum += float(daily_temperature_values.lowest_temperature_of_the_day)
        temperature_values.lowest_temperature_count += 1
    
    if daily_temperature_values.maximum_humidity_of_the_day:
        temperature_values.humidity_sum += float(daily_temperature_values.maximum_humidity_of_the_day)
        temperature_values.humidity_count += 1

def calculate_mean_temperature(temperature_values):
    mean_result_values = initialize_the_temperature_mean_results()
    mean_result_values.highest_temperature_mean = Calculate_mean( temperature_values.highest_temperature_sum , temperature_values.highest_temperature_count)
    mean_result_values.lowest_temperature_mean = Calculate_mean(temperature_values.lowest_temperature_sum ,temperature_values.lowest_temperature_count) 
    mean_result_values.maximum_humidity_mean = Calculate_mean( temperature_values.humidity_sum , temperature_values.humidity_count)
    return mean_result_values

def display_the_calculated_results(mean_result_values):
    print(f'Highest Average: {mean_result_values.highest_temperature_mean} \nLowest Average: {mean_result_values.lowest_temperature_mean} \nAverage Humidty: {mean_result_values.maximum_humidity_mean}')


def Calculate_mean(sum,count):
    if count > 0:
        return sum / count

