"""Write data gathered by weather_scrap to a csv file.

Julian Wittmann
2017-03-31
Python 3.5
"""

import csv

from weather_common import *


def get_header():
    return csv_entry._fields


def translate_to_csv_format(a_weather_entry):

    def translate_to_weather_symbol(weather):
        try:
            return weather_symbols[weather]
        except KeyError:
            return '?'

    a_csv_entry = csv_entry(
        a_weather_entry.day,
        '{}/{}'.format(a_weather_entry.max, a_weather_entry.min),
        a_weather_entry.weather,
        translate_to_weather_symbol(a_weather_entry.weather)
    )
    return a_csv_entry


def write_weather_to_csv(monthly_weather):
    # get filename
    filename = 'weather_{}_{}_{}.csv'.format(
        monthly_weather.location,
        monthly_weather.year,
        monthly_weather.month
    )

    # create file
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        weather_writer = csv.writer(csv_file)

        # write header
        header = get_header()
        weather_writer.writerow(header)

        # write entires
        for day_entry in monthly_weather.daily_weather:
            csv_row = translate_to_csv_format(day_entry)
            weather_writer.writerow(csv_row)
