from constants import MONTH_NAMES, HIGHEST_TEMPERATURE, LOWEST_TEMPERATURE, MAXIMUM_HUMIDITY, MAXIMUM_HUMIDITY_MEAN, HIGHEST_TEMPERATURE_MEAN, LOWEST_TEMPERATURE_MEAN, DATE, VALUE


class Display:
    def __init__(self):
        self.RED = '\033[0;31m'
        self.BLUE = '\033[34m'
        self.RESET = '\033[0m'

    def display_yearly_results(self, yearly_temperature_values):
    
        if yearly_temperature_values[HIGHEST_TEMPERATURE][DATE] is not None \
                and yearly_temperature_values[LOWEST_TEMPERATURE][DATE] is not None \
                    and yearly_temperature_values[MAXIMUM_HUMIDITY][DATE] is not None:
            print(f'Highest: {yearly_temperature_values[HIGHEST_TEMPERATURE][VALUE]}C on {self.set_to_correct_date_format(yearly_temperature_values[HIGHEST_TEMPERATURE][DATE]) } ')
            print(f'Lowest: {yearly_temperature_values[LOWEST_TEMPERATURE][VALUE]}C on {self.set_to_correct_date_format(yearly_temperature_values[LOWEST_TEMPERATURE][DATE])} ')
            print(f'Humid: {yearly_temperature_values[MAXIMUM_HUMIDITY][VALUE]}C on {self.set_to_correct_date_format(yearly_temperature_values[MAXIMUM_HUMIDITY][DATE])} ')
        else:
            print('no data to display')
    
    def set_to_correct_date_format(self, date):
        date_components = date.split('-')
        return f'{self.find_month_name(int(date_components[1])).replace("_", "")} {date_components[2]}'
    
    def find_month_name(self, month_number):

        if month_number < 1 or month_number > 12:
            print('Invalid input format entered')
            return 0

        return MONTH_NAMES[month_number]

    def display_average_results(self, mean_temperature):
        print(f'Highest Average: {mean_temperature[HIGHEST_TEMPERATURE_MEAN]}C')
        print(f'Lowest Average: {mean_temperature[LOWEST_TEMPERATURE_MEAN]}C')
        print(f'Average Humidty: {mean_temperature[MAXIMUM_HUMIDITY_MEAN]}%')

    def generate_bar_chart_for_individual_temperature(self, all_month_temperature_values):
        day_number = 1
        for day in all_month_temperature_values:
            self.generate_bar_chart_for_each_temperature(
                day_number, 
                day[HIGHEST_TEMPERATURE], 
                self.RED
                )
            self.generate_bar_chart_for_each_temperature(
                day_number, 
                day[LOWEST_TEMPERATURE], 
                self.BLUE
                )
            day_number += 1
    
    def generate_bar_chart_for_each_temperature(self, day_number,temperature_value, color):

        if temperature_value is not None:
            print(f'{day_number}: {color}{"+" * temperature_value}{self.RESET} {temperature_value}C')
        else:
            print(f'{day_number}: No Data ')

    def generate_bar_chart_for_combined_temperature(self, all_month_temperature_values):
        day_number = 1
        for day in all_month_temperature_values:
            self.generate_bar_chart_for_each_value_of_combined(day_number, day)
            day_number += 1

    def generate_bar_chart_for_each_value_of_combined(self, day_number, daily_temperature_values):
    
        if daily_temperature_values[HIGHEST_TEMPERATURE] is not None \
                and daily_temperature_values[LOWEST_TEMPERATURE] is not None :
            print(f'{day_number}: {self.BLUE}{"+" * daily_temperature_values[LOWEST_TEMPERATURE]}{self.RED}{"+" * daily_temperature_values[HIGHEST_TEMPERATURE]}{self.RESET} {daily_temperature_values[LOWEST_TEMPERATURE]}C-{daily_temperature_values[HIGHEST_TEMPERATURE]}C')
        else:
            print(f'{day_number}: No Data ')
