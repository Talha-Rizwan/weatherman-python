import math


class Calculator :
    def get_the_sum_values(self, all_daily_temperature_values):
        temperature_sum_values = self.initialize_temperature_sum_values()

        for daily_temperature_value in all_daily_temperature_values:
            self.compute_the_sum_of_all_rows(temperature_sum_values, daily_temperature_value)
        
        return self.calculate_mean_temperature(temperature_sum_values)

    def initialize_temperature_sum_values(self):
        return {
        'highest_temperature' : {'sum' : 0, 'count' : 0 }, 
        'lowest_temperature' : {'sum' : 0, 'count' : 0 }, 
        'maximum_humidity' : {'sum' : 0, 'count' : 0 }
        }
    
    def compute_the_sum_of_all_rows(self, temperature_sum_values, daily_temperature_values):
        self.compute_sum_of_single_attribute(
            daily_temperature_values, 
            temperature_sum_values, 
            'highest_temperature'
            )
        self.compute_sum_of_single_attribute(
            daily_temperature_values,
            temperature_sum_values, 
            'lowest_temperature'
            )
        self.compute_sum_of_single_attribute(
            daily_temperature_values,
            temperature_sum_values,
            'maximum_humidity'
            )
    
    def compute_sum_of_single_attribute(
            self, 
            daily_temperature_values, 
            temperature_sum_values, 
            key_attribute 
            ):

        if daily_temperature_values[key_attribute]:
            temperature_sum_values[key_attribute]['sum'] += int(daily_temperature_values[key_attribute])
            temperature_sum_values[key_attribute]['count'] += 1

    def calculate_mean_temperature(self, temperature_sum_values):
        mean_result_values = self.initialize_temperature_mean_values()
        mean_result_values['highest_temperature_mean'] = self.Calculate_mean( 
            temperature_sum_values['highest_temperature']['sum'], 
            temperature_sum_values['highest_temperature']['count'] 
            )
        mean_result_values['lowest_temperature_mean'] = self.Calculate_mean(
            temperature_sum_values['lowest_temperature']['sum'],
            temperature_sum_values['lowest_temperature']['count'] 
            ) 
        mean_result_values['maximum_humidity_mean'] = self.Calculate_mean(
            temperature_sum_values['maximum_humidity']['sum'], 
            temperature_sum_values['maximum_humidity']['count']
            )
        return mean_result_values
    
    def initialize_temperature_mean_values(self):
        return {
            'highest_temperature_mean' : 0, 
            'lowest_temperature_mean' :0, 
            'maximum_humidity_mean' : 0
            }

    def Calculate_mean(self, sum, count):
        if count > 0:
            return int(sum / count)
        
    def get_yearly_weather_results(self, all_months_weather_values):
        yearly_temperature_values = self.initialize_temperature_values()    
        
        for month_weather_values in all_months_weather_values:
            self.compare_monthly_with_yearly_weather_values(month_weather_values, yearly_temperature_values)
        
        return yearly_temperature_values    

    def initialize_temperature_values(self):
        return {
        'highest_temperature' : {'value' : -math.inf, 'date' : None }, 
        'lowest_temperature' : {'value' : math.inf, 'date' : None }, 
        'maximum_humidity' : {'value' : -math.inf, 'date' : None }
        }    

    def compare_monthly_with_yearly_weather_values(self, monthly_temperature_values,
                                               yearly_temperature_values ):    
        self.compare_temperature_for_single_attribute_of_monthly_to_yearly \
            (monthly_temperature_values, yearly_temperature_values, 'highest_temperature')
        self.compare_temperature_for_single_attribute_of_monthly_to_yearly \
            (monthly_temperature_values, yearly_temperature_values, 'lowest_temperature')
        self.compare_temperature_for_single_attribute_of_monthly_to_yearly \
            (monthly_temperature_values, yearly_temperature_values, 'maximum_humidity')
        return yearly_temperature_values

    def compare_temperature_for_single_attribute_of_monthly_to_yearly(
            self,
            monthly_temperature_values, 
            yearly_temperature_values, 
            key_attribute):

        if key_attribute == 'lowest_temperature':
            if monthly_temperature_values[key_attribute]['value'] \
                    < yearly_temperature_values[key_attribute]['value']:
                yearly_temperature_values[key_attribute]['value'] \
                        = monthly_temperature_values[key_attribute]['value']
                yearly_temperature_values[key_attribute]['date'] \
                        = monthly_temperature_values[key_attribute]['date']
        else:
            if monthly_temperature_values[key_attribute]['value'] \
                    > yearly_temperature_values[key_attribute]['value']:
                yearly_temperature_values[key_attribute]['value'] \
                        = monthly_temperature_values[key_attribute]['value']
                yearly_temperature_values[key_attribute]['date'] \
                        = monthly_temperature_values[key_attribute]['date']