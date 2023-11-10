# Weatherman-assignment


# Weather Man

## Overview

The Weather Man Python application is designed to analyze and generate reports based on historical weather data. The provided weather data files contain information on temperatures and humidity for past years. The application offers various functionalities to extract meaningful insights from the data.

## Installation

To use the Weather Man application, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the Weather Man repository.

2. Navigate to the project directory:
   ```bash
   cd weather-man
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The Weather Man application provides different commands to generate specific reports. Here are examples of usage for each report:

1. **Report for a Given Year:**
   ```bash
   python weatherman.py -e 2002 /path/to/files
   ```
   Output:
   ```
   Highest: 45C on June 23
   Lowest: 01C on December 22
   Humid: 95% on August 14
   ```

2. **Report for a Given Month (Average):**
   ```bash
   python weatherman.py -a 2005/6 /path/to/files
   ```
   Output:
   ```
   Highest Average: 39C
   Lowest Average: 18C
   Average Humidity: 71%
   ```

3. **Draw Horizontal Bar Charts (Highest and Lowest Temperature):**
   ```bash
   python weatherman.py -c 2011/03 /path/to/files
   ```
   Output:
   ```
   March 2011
   01 ++++++++++++++++++++++++ 25C
   01 +++++++++++ 11C
   02 +++++++++++++++++++++ 22C
   02 ++++++++ 08C
   ```

4. **Draw Combined Horizontal Bar Chart (Highest and Lowest Temperature):**
   ```bash
   python weatherman.py -d 2011/3 /path/to/files
   ```
   Output:
   ```
   March 2011
   01 +++++++++++++++++++++++++++++++++++ 11C - 25C
   02 +++++++++++++++++++++++++++++ 08C - 22C
   ```

## Notes

- Ensure that the provided path to weather data files is correct.
- The application uses a red color for the highest temperature and blue for the lowest temperature in the bar charts.

Feel free to explore and analyze the weather data with the Weather Man application! If you encounter any issues or have suggestions, please let us know by opening an issue in the repository.
