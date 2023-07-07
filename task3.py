import sys
import os

RED = "\033[0;31m"
BLUE = '\033[34m'
RESET = '\033[0m'

def main():
    read_arguments()
    
def read_arguments():
    arguments = sys.argv

    if len(arguments) > 2:
        month_and_year = arguments[1]
        file_path = arguments[2]
        List_split=split_month_and_year(month_and_year)
        month=find_month_name(int(List_split[1]))
        year=List_split[0]

        path=generate_file_path(year, month)
        print("the file path is : ", path)

        if month != 0 and os.path.exists(path):
            read_file(path)
        else:
            print("invalid arguments format")

def find_month_name(month_number):
    if month_number < 1 or month_number > 12 :
        print("invalid input format entered")
        return 0
    elif month_number==1:
        return "_Jan"
    elif month_number==2:
        return "_Feb"
    elif month_number==3:
        return "_Mar"
    elif month_number==4:
        return "_Apr"
    elif month_number==5:
        return "_May"
    elif month_number==6:
        return "_Jun"
    elif month_number==7:
        return "_Jul"
    elif month_number==8:
        return "_Aug"
    elif month_number==9:
        return "_Sep"
    elif month_number==10:
        return "_Oct"
    elif month_number==11:
        return "_Nov"
    elif month_number==12:
        return "_Dec"
    
def split_month_and_year(month_and_year):
    return month_and_year.split('/')

def generate_file_path(year, month):
    path = 'weatherfiles/Murree_weather_'+year+month+'.txt'
    return path

def read_file(path):

    file_path = path

    with open(file_path,'r') as file:
        next(file)
        
        day_number=1

        for line in file:
            all_columns=line.split(',')

            if all_columns[1] != '':
                current_highest_temperature = int(all_columns[1].strip())
            else:
                current_highest_temperature = None

            if all_columns[3] != '':
                current_lowest_temperature = int(all_columns[3].strip())
            else:
                current_lowest_temperature = None

            if current_highest_temperature is not None:
                horizontal_bar_chart(day_number,current_highest_temperature, RED)
            else:
                print(f"{day_number}: ")

            if current_lowest_temperature is not None:
                horizontal_bar_chart(day_number,current_lowest_temperature, BLUE)
            else:
                print(f"{day_number}: ")

            day_number+=1


def horizontal_bar_chart(day_number,value, color):
    print(f"{day_number}: ", end="")
    for i in range(value):
        print(color+"#"+RESET, end="")
    print(f" {value}C")

if __name__ == "__main__":
    main()