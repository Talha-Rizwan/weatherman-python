import argparse


class Argument:

    def __init__(self):
        self.command_line_arguments = None    


    # def get_command_line_arguments(self):
    #     arguments = sys.argv

    #     if len(arguments) > 3:
    #         self.command_line_arguments = {
    #             'flag' : arguments[1],
    #             'month_and_year' : arguments[2],
    #             'file_path' : arguments[3]
    #         }
    #     else:
    #         print("Incorrect number of arguments")

    
    def get_command_line_arguments(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('-e', action='store_true', help='Optional flag')
        parser.add_argument('-a', action='store_true', help='Optional flag')
        parser.add_argument('-c', action='store_true', help='Optional flag')
        parser.add_argument('-d', action='store_true', help='Optional flag')

        parser.add_argument('date', help='First argument')
        parser.add_argument('file_path', help='Second argument')

        self.command_line_arguments = parser.parse_args()
