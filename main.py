import sys

from yearly_temperature import get_yearly_temperature_stats
from monthly_temperature import get_monthly_average_temperature_stats
from individual_temp_bar_charts import individual_bar_charts_for_highest_and_lowest_temperature_of_month
from combined_temp_bar_chart import combined_bar_chart_for_highest_and_lowest_temperature_of_month


def main():
    check_flag_argument()


def check_flag_argument():
    arguments = sys.argv
    flag = arguments[1]

    flag_dict = {
            '-e': get_yearly_temperature_stats,
            '-a': get_monthly_average_temperature_stats,
            '-c': individual_bar_charts_for_highest_and_lowest_temperature_of_month,
            '-d': combined_bar_chart_for_highest_and_lowest_temperature_of_month
        }

    flag_dict.get(flag, invalid_flag)()


def invalid_flag():
    print('The flag entered is incorrect!')
    

if __name__ == '__main__':
    main()