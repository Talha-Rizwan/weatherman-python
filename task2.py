import sys
import os

def main():
    read_arguments_and_find_result()

def read_arguments_and_find_result():
    arguments = sys.argv

    if len(arguments) > 2:
        month_and_year = arguments[1]
        file_path = arguments[2]
        
        List_split=split_month_and_year(month_and_year)

        month=find_month_name(int(List_split[1]))
        year=List_split[0]

        path=generate_file_path(year, month)
        print("the path is : ", path)

        if month != 0 and os.path.exists(path):
            Calculate_mean_temperature(path)
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


def Calculate_mean_temperature(path):

    file_path = path

    with open(file_path,'r') as file:
        next(file)
        
        highest_temperature_sum=0
        lowest_temperature_sum=0
        humidity_sum=0
        highest_temp_count=0
        lowest_temp_count=0
        humidity_count=0

        for line in file:
            all_columns=line.split(',')

            current_highest_temperature = all_columns[1].strip()
            current_lowest_temperature = all_columns[3].strip()
            current_humidity=all_columns[8].strip()

            if current_highest_temperature:
                highest_temperature_sum += float(current_highest_temperature)
                highest_temp_count += 1

            if current_lowest_temperature:
                lowest_temperature_sum += float(current_lowest_temperature)
                lowest_temp_count += 1
            
            if current_humidity:
                humidity_sum += float(current_humidity)
                humidity_count += 1
   
            highest_temperature_mean = Calculate_mean( highest_temperature_sum , highest_temp_count)
            lowest_temperature_mean =Calculate_mean(lowest_temperature_sum ,lowest_temp_count) 
            humidity_mean_average =Calculate_mean( humidity_sum , humidity_count)
    
    print(f"Highest Average: {highest_temperature_mean} \nLowest Average: {lowest_temperature_mean} \nAverage Humidty: {humidity_mean_average}")

    return highest_temperature_mean, lowest_temperature_mean, humidity_mean_average

def Calculate_mean(sum,count):
    if count > 0:
        return sum / count


if __name__ == "__main__":
    main()