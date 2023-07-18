from argument_class import Argument
from file_parser_class import Parser
from calculator_class import Calculator
from display_output_class import Display


def main():
    arg = Argument()
    arg.get_command_line_arguments()
    check_flag_argument( arg.command_line_arguments)

def check_flag_argument(arguments):
    parse = Parser()
    calculate = Calculator()
    displayer = Display()

    if arguments.e:
        months_weather_data = parse.read_file_for_yearly_weather(arguments)
        yearly_temperature = calculate.get_yearly_weather_results(months_weather_data)
        displayer.display_yearly_results(yearly_temperature)

    elif arguments.a or arguments.c or arguments.d:
        parse.get_file_path(arguments)

        for file in parse.path:
            if arguments.a:
                daily_temperatures = parse.read_file(file)
                mean_temperature = calculate.get_sum_values(daily_temperatures)
                displayer.display_average_results(mean_temperature)
            else :
                this_month_temperature = parse.read_file_for_bar_chart(file)
                if arguments.c:
                    displayer.generate_bar_chart_for_individual_temperature(this_month_temperature, arguments)
                else:
                    displayer.generate_bar_chart_for_combined_temperature(this_month_temperature, arguments)                    
    else:
        print('Incorrect Flag!')

if __name__ == '__main__':
    main()
