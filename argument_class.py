"""command line arguments are handled here"""
import argparse


class Argument:
    """This class handles command line arguments"""

    def __init__(self):
        self.command_line_arguments = None

    def get_command_line_arguments(self):
        """command line arguments are parsed using the argparse library"""

        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group()

        group.add_argument(
            '-e',
            action = 'store_true',
            help = 'flag for given year highest temperature, lowest temperature, maximum humidity'
            )
        group.add_argument(
            '-a',
            action = 'store_true',
            help = 'flag for given month average highest temperature, lowest temperature, humidity'
            )
        group.add_argument(
            '-c',
            action = 'store_true',
            help = 'two bar charts for the highest and lowest temperature on each day'
            )
        group.add_argument(
            '-d',
            action = 'store_true',
            help = 'one bar chart for the highest and lowest temperature on each day'
            )

        parser.add_argument('date', help = 'Date argument')
        parser.add_argument('file_path', help = 'File path argument')

        self.command_line_arguments = parser.parse_args()
        