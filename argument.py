import sys


class Argument:

    def __init__(self):
        self.command_line_arguments = None    


    def get_command_line_arguments(self):
        arguments = sys.argv

        if len(arguments) > 3:
            self.command_line_arguments = {
                'flag' : arguments[1],
                'month_and_year' : arguments[2],
                'file_path' : arguments[3]
            }
        else:
            print("Incorrect number of arguments")
