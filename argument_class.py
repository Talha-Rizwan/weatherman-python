import argparse


class Argument:

    def __init__(self):
        self.command_line_arguments = None

    def get_command_line_arguments(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('-e', action = 'store_true', help = 'flag for given year highest temperature, lowest temperature, maximum humidity')
        parser.add_argument('-a', action = 'store_true', help = 'flag for given month average highest temperature, lowest temperature, humidity')
        parser.add_argument('-c', action = 'store_true', help = 'flag for given month two horizontal bar charts for the highest and lowest temperature on each day')
        parser.add_argument('-d', action = 'store_true', help = 'flag for given month one horizontal bar chart for the highest and lowest temperature on each day')

        parser.add_argument('date', help = 'Date argument')
        parser.add_argument('file_path', help = 'File path argument')

        self.command_line_arguments = parser.parse_args()
        