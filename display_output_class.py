import calendar
from constants import HIGHEST_TEMPERATURE, LOWEST_TEMPERATURE, MAXIMUM_HUMIDITY
from constants import MAXIMUM_HUMIDITY_MEAN, HIGHEST_TEMPERATURE_MEAN, LOWEST_TEMPERATURE_MEAN
from constants import DATE, VALUE


class Display:
    def __init__(self):
        self.high_temperature_color = '\033[0;31m'
        self.low_temperature_color = '\033[34m'
        self.text_color = '\033[0m'

    def display_yearly_results(self, yearly_temperature):

        if yearly_temperature[HIGHEST_TEMPERATURE][DATE] is not None \
                and yearly_temperature[LOWEST_TEMPERATURE][DATE] is not None \
                    and yearly_temperature[MAXIMUM_HUMIDITY][DATE] is not None:
            print(f'Highest: {yearly_temperature[HIGHEST_TEMPERATURE][VALUE]}C on ' +
                  f'{self.to_date_format(yearly_temperature[HIGHEST_TEMPERATURE][DATE])}')
            print(f'Lowest: {yearly_temperature[LOWEST_TEMPERATURE][VALUE]}C on '+
                  f'{self.to_date_format(yearly_temperature[LOWEST_TEMPERATURE][DATE])}')
            print(f'Humid: {yearly_temperature[MAXIMUM_HUMIDITY][VALUE]}C on ' +
                  f'{self.to_date_format(yearly_temperature[MAXIMUM_HUMIDITY][DATE])}')
        else:
            print('no data to display')

    def to_date_format(self, date):
        date_components = date.split('-')
        return f'{calendar.month_name[int(date_components[1])][:3]} {date_components[2]}'

    def display_average_results(self, mean_temperature):
        print(f'Highest Average: {mean_temperature[HIGHEST_TEMPERATURE_MEAN]}C')
        print(f'Lowest Average: {mean_temperature[LOWEST_TEMPERATURE_MEAN]}C')
        print(f'Average Humidty: {mean_temperature[MAXIMUM_HUMIDITY_MEAN]}%')

    def generate_bar_chart_for_individual_temperature(
            self,
            month_temperature,
            arguments
            ):
        try:
            list_split = arguments.date.split('/')
            print(f'{calendar.month_name[int(list_split[1])]} {list_split[0]}')
            day_number = 1
            for day in month_temperature:
                self.generate_bar_chart_for_each_temperature(
                    day_number,
                    day[HIGHEST_TEMPERATURE],
                    self.high_temperature_color
                    )
                self.generate_bar_chart_for_each_temperature(
                    day_number,
                    day[LOWEST_TEMPERATURE],
                    self.low_temperature_color
                    )
                day_number += 1
        except Exception as e:
            print(f'Error occured while processing the date: {e}')


    def generate_bar_chart_for_each_temperature(self, day_number,temperature, color):

        if temperature is not None:
            print(f'{day_number}: {color}{"+" * temperature}' +
                  f'{self.text_color} {temperature}C')

    def generate_bar_chart_for_combined_temperature(self, month_temperature, arguments):
        try:
            list_split = arguments.date.split('/')
            print(f'{calendar.month_name[int(list_split[1])]} {list_split[0]}')
            day_number = 1
            for day in month_temperature:
                self.generate_bar_chart_for_each_value_of_combined(day_number, day)
                day_number += 1
        except Exception as e:
            print(f'Error occured while processing the date: {e}')


    def generate_bar_chart_for_each_value_of_combined(self, day_number, daily_temperature):

        if daily_temperature[HIGHEST_TEMPERATURE] is not None \
                and daily_temperature[LOWEST_TEMPERATURE] is not None :
            print(f'{day_number}: {self.low_temperature_color}' +
                  f'{"+" * daily_temperature[LOWEST_TEMPERATURE]}' +
                  f'{self.high_temperature_color}' +
                  f'{"+" * daily_temperature[HIGHEST_TEMPERATURE]}' +
                  f'{self.text_color} {daily_temperature[LOWEST_TEMPERATURE]}C-' +
                  f'{daily_temperature[HIGHEST_TEMPERATURE]}C')
