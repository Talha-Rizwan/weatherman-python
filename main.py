"""Main program module"""

from argument_class import Argument
from file_parser_class import Parser
from calculator_class import Calculator
from display_output_class import Display


def main():
    """Main driver for weatherman"""

    arg = Argument()
    arg.get_command_line_arguments()

    parse = Parser()
    calculate = Calculator()
    displayer = Display()

    if arg.command_line_arguments.e:
        months_weather_data = parse.read_file_for_yearly_weather(arg.command_line_arguments)
        yearly_temperature = calculate.get_yearly_weather_results(months_weather_data)
        displayer.display_yearly_results(yearly_temperature)

    else:
        parse.get_file_path(arg.command_line_arguments)

        for file in parse.path:
            if arg.command_line_arguments.a:
                daily_temperatures = parse.read_file(file)
                mean_temperature = calculate.get_mean_values(daily_temperatures)
                displayer.display_average_results(mean_temperature)
            else :
                this_month_temperature = parse.read_file_for_bar_chart(file)
                if arg.command_line_arguments.c:
                    displayer.generate_bar_chart_for_individual_temperature(
                        this_month_temperature,
                        arg.command_line_arguments
                    )
                else:
                    displayer.generate_bar_chart_for_combined_temperature(
                        this_month_temperature,
                        arg.command_line_arguments
                    )


if __name__ == '__main__':
    main()
