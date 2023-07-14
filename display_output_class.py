
class Display:

    def __init__(self):
        self.RED = '\033[0;31m'
        self.BLUE = '\033[34m'
        self.RESET = '\033[0m'
# Task 1
    def display_yearly_results(self, yearly_temperature_values):
    
        if yearly_temperature_values['highest_temperature']['date'] is not None \
                and yearly_temperature_values['lowest_temperature']['date'] is not None \
                    and yearly_temperature_values['maximum_humidity']['date'] is not None:
            print(f'Highest: {yearly_temperature_values["highest_temperature"]["value"]}C on {self.set_date_to_correct_format(yearly_temperature_values["highest_temperature"]["date"]) } ')
            print(f'Lowest: {yearly_temperature_values["lowest_temperature"]["value"]}C on {self.set_date_to_correct_format(yearly_temperature_values["lowest_temperature"]["date"])} ')
            print(f'Humid: {yearly_temperature_values["maximum_humidity"]["value"]}C on {self.set_date_to_correct_format(yearly_temperature_values["maximum_humidity"]["date"])} ')
        else:
            print('no data to display')
    
    def set_date_to_correct_format(self, date):
        date_components = date.split('-')
        return f'{self.find_month_name(int(date_components[1])).replace("_", "")} {date_components[2]}'
    
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





# Task 2
    def display_average_results(self, mean_result_values):
        print(f'Highest Average: {mean_result_values["highest_temperature_mean"]}C')
        print(f'Lowest Average: {mean_result_values["lowest_temperature_mean"]}C')
        print(f'Average Humidty: {mean_result_values["maximum_humidity_mean"]}%')

# Task 3
    def generate_temperature_graph_for_individual_bars(self, all_month_temperature_values):
        day_number = 1
        for day in all_month_temperature_values:
            self.generate_bar_chart_for_each_value_individual(day_number, 
                                                day['highest_temperature'], 
                                                self.RED)
            self.generate_bar_chart_for_each_value_individual(day_number, 
                                                day['lowest_temperature'], 
                                                self.BLUE)
            day_number+=1
    
    def generate_bar_chart_for_each_value_individual(self, day_number,temperature_value, color):

        if temperature_value is not None:
            print(f'{day_number}: ', end = '')
            for idx in range(temperature_value):
                print(f"{color}+{self.RESET}", end='')
            print(f' {temperature_value}C')
        else:
            print(f'{day_number}: No Data ')


# Task 4
    def generate_temperature_graph_for_combined_bars(self, all_month_temperature_values):
        day_number = 1
        for day in all_month_temperature_values:
            self.generate_bar_chart_for_each_value_combined(day_number, 
                                                day)
            day_number+=1

    def generate_bar_chart_for_each_value_combined(self, day_number, daily_temperature_values):
    
        if daily_temperature_values['highest_temperature'] is not None \
                and daily_temperature_values['lowest_temperature'] is not None :
            print(f'{day_number}: ', end='')
            for idx in range(daily_temperature_values['lowest_temperature']):
                print(f'{self.BLUE}+{self.RESET}', end='')
            for idx in range(daily_temperature_values['highest_temperature']):
                print(f'{self.RED}+{self.RESET}', end='')
            print(f' {daily_temperature_values["lowest_temperature"]}C-{daily_temperature_values["highest_temperature"]}C')
        else:
            print(f'{day_number}: No Data ')
    
    