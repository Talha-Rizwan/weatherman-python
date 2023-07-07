import sys
import os

def main():
    read_arguments()

def read_arguments():
    highest_year_temperature='-10000'
    lowest_year_temperature='10000'
    max_year_humidity='-10000'
    max_highest_year_temperature_date=0
    max_lowest_year_temperature_date=0
    max_year_humidity_date = 0

    arguments = sys.argv

    if len(arguments) > 2:
        year = arguments[1]
        file_path = arguments[2]
        
        for i in range(1,13):
            month=find_month_name(i)
            path=generate_file_path(year, month)
            print("the path is : ", path)

            if os.path.exists(path):
                file_path = path

                with open(file_path,'r') as file:
                    next(file)
                    
                    monthly_max_highest_temperature='-10000'
                    monthly_max_lowest_temperature='10000'
                    monthly_max_humidity='-10000'
                    monthly_max_highest_temperature_date=0
                    monthly_max_lowest_temperature_date=0
                    monthly_max_humidity_date = 0
                    
                    for line in file:
                        all_columns=line.split(',')

                        current_date = all_columns[0].strip()
                        current_highest_temperature = all_columns[1].strip()
                        current_lowest_temperature = all_columns[3].strip()
                        current_humidity=all_columns[8].strip()
                        
                        if current_highest_temperature:
                            if monthly_max_highest_temperature < current_highest_temperature:
                                monthly_max_highest_temperature=current_highest_temperature
                                monthly_max_highest_temperature_date=current_date

                        if current_lowest_temperature:
                            if monthly_max_lowest_temperature > current_lowest_temperature:
                                monthly_max_lowest_temperature=current_lowest_temperature
                                monthly_max_lowest_temperature_date=current_date
                        
                        if current_humidity:
                            if monthly_max_humidity < current_humidity:
                                monthly_max_humidity=current_humidity
                                monthly_max_humidity_date=current_date

                    if monthly_max_highest_temperature > highest_year_temperature:
                        highest_year_temperature=monthly_max_highest_temperature
                        max_highest_year_temperature_date=monthly_max_highest_temperature_date

                    if monthly_max_lowest_temperature < lowest_year_temperature:
                        lowest_year_temperature=monthly_max_lowest_temperature
                        max_lowest_year_temperature_date=monthly_max_lowest_temperature_date

                    if monthly_max_humidity > max_year_humidity:
                        max_year_humidity=monthly_max_humidity
                        max_year_humidity_date=monthly_max_humidity_date

    print(f"Highest:{highest_year_temperature}C on {max_highest_year_temperature_date} ")
    print(f"Lowest:{lowest_year_temperature}C on {max_lowest_year_temperature_date} ")
    print(f"Humid:{max_year_humidity}C on {max_year_humidity_date} ")

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

def generate_file_path(year, month):
    path = 'weatherfiles/Murree_weather_'+year+month+'.txt'
    return path

if __name__ == "__main__":
    main()