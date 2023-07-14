from argument import Argument
from parser_file import Parser
from calculate_class import Calculator
from display_output import Display

def main():
    arg = Argument()

    arg.get_command_line_arguments()
    
    check_flag_argument(arg.command_line_arguments)


def check_flag_argument(command_line_arguments):
    flag = command_line_arguments['flag']
    parse = Parser()
    calculate = Calculator()
    displayer = Display()

    if flag == '-e':
        
        all_months_weather_values = parse.read_file_for_yearly_weather(command_line_arguments)
        yearly_temperature_values = calculate.get_yearly_weather_results(all_months_weather_values)
        displayer.display_yearly_results(yearly_temperature_values)

    elif flag == '-a':
        parse.generate_file_path(command_line_arguments)

        if parse.isPathExist():        
            all_daily_temperature_values = parse.read_file(parse.path)
            mean_result_values = calculate.get_the_sum_values(all_daily_temperature_values)
            displayer.display_average_results(mean_result_values)
        else:
            print('invalid arguments format')


    elif flag == '-c':
        parse.generate_file_path(command_line_arguments)
        
        if parse.isPathExist():            
            all_month_temperature_values = parse.read_file_for_bar_chart(parse.path)
            displayer.generate_temperature_graph_for_individual_bars(all_month_temperature_values)
        else:
            print('invalid arguments format')

    elif flag == '-d':
        parse.generate_file_path(command_line_arguments)

        if parse.isPathExist():            
            all_month_temperature_values = parse.read_file_for_bar_chart(parse.path)
            displayer.generate_temperature_graph_for_combined_bars(all_month_temperature_values)
        else:
            print('invalid arguments format')

    else:
        invalid_flag()


def invalid_flag():
    print('The flag entered is incorrect!')
    

if __name__ == '__main__':
    main()