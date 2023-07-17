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
        all_months_weather_values = parse.read_file_for_yearly_weather(arguments)
        yearly_temperature_values = calculate.get_yearly_weather_results(all_months_weather_values)
        displayer.display_yearly_results(yearly_temperature_values)

    elif arguments.a:
        parse.generate_file_path( arguments)

        if parse.isPathExist():        
            daily_temperatures = parse.read_file(parse.path)
            mean_temperature = calculate.get_sum_values(daily_temperatures)
            displayer.display_average_results(mean_temperature)
        else:
            print('invalid arguments format')

    elif arguments.c:
        parse.generate_file_path( arguments)
        
        if parse.isPathExist():            
            all_month_temperature_values = parse.read_file_for_bar_chart(parse.path)
            displayer.generate_bar_chart_for_individual_temperature(all_month_temperature_values)
        else:
            print('invalid arguments format')

    elif arguments.d:
        parse.generate_file_path( arguments)

        if parse.isPathExist():            
            all_month_temperature_values = parse.read_file_for_bar_chart(parse.path)
            displayer.generate_bar_chart_for_combined_temperature(all_month_temperature_values)
        else:
            print('invalid arguments format')

    else:
        invalid_flag()


def invalid_flag():
    print('Flag is incorrect!')
    

if __name__ == '__main__':
    main()
