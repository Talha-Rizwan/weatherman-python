"""calculations are performed here"""
import math
from constants import HIGHEST_TEMPERATURE, LOWEST_TEMPERATURE, MAXIMUM_HUMIDITY
from constants import HIGHEST_TEMPERATURE_MEAN, LOWEST_TEMPERATURE_MEAN, MAXIMUM_HUMIDITY_MEAN
from constants import SUM, COUNT, VALUE, DATE


class Calculator :
    """Performs all the calculation related tasks"""
    def get_mean_values(self, daily_temperatures):
        """Calculates the average monthly result from daily temperatures"""
        temperature_sum = {
            HIGHEST_TEMPERATURE: {SUM: 0, COUNT: 0 },
            LOWEST_TEMPERATURE: {SUM: 0, COUNT: 0 },
            MAXIMUM_HUMIDITY: {SUM: 0, COUNT: 0 }
        }

        for daily_temperature in daily_temperatures:
            self.compute_sum_of_rows(temperature_sum, daily_temperature)

        return self.calculate_mean_temperatures(temperature_sum)

    def compute_sum_of_rows(self, temperature_sum, daily_temperature):
        """Calculates the sum of single row in the dataset"""
        self.compute_sum_of_single_attribute(
            daily_temperature,
            temperature_sum,
            HIGHEST_TEMPERATURE
            )
        self.compute_sum_of_single_attribute(
            daily_temperature,
            temperature_sum,
            LOWEST_TEMPERATURE
            )
        self.compute_sum_of_single_attribute(
            daily_temperature,
            temperature_sum,
            MAXIMUM_HUMIDITY
            )

    def compute_sum_of_single_attribute(
            self,
            daily_temperature,
            temperature_sum,
            key_attribute
            ):
        """Add the value of a single attribute in the total sum value"""
        if daily_temperature[key_attribute]:
            temperature_sum[key_attribute][SUM] += int(daily_temperature[key_attribute])
            temperature_sum[key_attribute][COUNT] += 1

    def calculate_mean_temperatures(self, temperature_sum):
        """Calculates the resultant mean temperature from the sum values """
        mean_temperature = {
                HIGHEST_TEMPERATURE_MEAN: 0,
                LOWEST_TEMPERATURE_MEAN:0,
                MAXIMUM_HUMIDITY_MEAN: 0
            }

        mean_temperature[HIGHEST_TEMPERATURE_MEAN] = self.calculate_mean(
            temperature_sum[HIGHEST_TEMPERATURE][SUM],
            temperature_sum[HIGHEST_TEMPERATURE][COUNT]
            )
        mean_temperature[LOWEST_TEMPERATURE_MEAN] = self.calculate_mean(
            temperature_sum[LOWEST_TEMPERATURE][SUM],
            temperature_sum[LOWEST_TEMPERATURE][COUNT]
            )
        mean_temperature[MAXIMUM_HUMIDITY_MEAN] = self.calculate_mean(
            temperature_sum[MAXIMUM_HUMIDITY][SUM],
            temperature_sum[MAXIMUM_HUMIDITY][COUNT]
            )
        return mean_temperature

    def calculate_mean(self, total_sum, count):
        """Calculates te mean from the sum value and total count value."""
        if count > 0:
            return int(total_sum / count)
        print("no data available")
        return None

    def get_yearly_weather_results(self, monthly_temperatures):
        """
            Computes the yearly maximum highest temperature,
            lowest temperature and most humid temperature
        """
        yearly_temperature = {
            HIGHEST_TEMPERATURE: {VALUE: -math.inf, DATE: None },
            LOWEST_TEMPERATURE: {VALUE: math.inf, DATE: None },
            MAXIMUM_HUMIDITY: {VALUE: -math.inf, DATE: None }
        }
        for month_weather in monthly_temperatures:
            self.compare_monthly_with_yearly_weather(
                month_weather,
                yearly_temperature
                )

        return yearly_temperature

    def compare_monthly_with_yearly_weather(self, monthly_temperature,
                                               yearly_temperature ):
        """Compares monthly temperature values with yearly temperature values"""
        self.compare_temperature_for_single_attribute_of_monthly_to_yearly \
            (monthly_temperature, yearly_temperature, HIGHEST_TEMPERATURE)
        self.compare_temperature_for_single_attribute_of_monthly_to_yearly \
            (monthly_temperature, yearly_temperature, LOWEST_TEMPERATURE)
        self.compare_temperature_for_single_attribute_of_monthly_to_yearly \
            (monthly_temperature, yearly_temperature, MAXIMUM_HUMIDITY)
        return yearly_temperature

    def compare_temperature_for_single_attribute_of_monthly_to_yearly(
            self,
            monthly_temperature,
            yearly_temperature,
            key_attribute
            ):
        """Compares monthly single temperature attribite with yearly temperature"""
        if key_attribute == LOWEST_TEMPERATURE:
            if monthly_temperature[key_attribute][VALUE] \
                    < yearly_temperature[key_attribute][VALUE]:
                yearly_temperature[key_attribute][VALUE] \
                        = monthly_temperature[key_attribute][VALUE]
                yearly_temperature[key_attribute][DATE] \
                        = monthly_temperature[key_attribute][DATE]
        else:
            if monthly_temperature[key_attribute][VALUE] \
                    > yearly_temperature[key_attribute][VALUE]:
                yearly_temperature[key_attribute][VALUE] \
                        = monthly_temperature[key_attribute][VALUE]
                yearly_temperature[key_attribute][DATE] \
                        = monthly_temperature[key_attribute][DATE]
                