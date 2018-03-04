"""Scrap weather data from http://weather.yahoo.co.jp

Julian Wittmann
2017-03-31
Python 3.5
"""

import bs4

from weather_common import *


class MonthlyWeather():
    """docstring for MonthlyWeather"""
    def __init__(self, location=None, year=None,
                 month=None, daily_weather=None):
        self.location = location
        self.year = year
        self.month = month
        # list of weather_entry
        self.daily_weather = [] if daily_weather is None else daily_weather


def find_days_in_month(month_soup):
    # find by links in the table
    def is_day(tag):
        return tag.name == 'a' and tag.parent.name == 'td'
    links = month_soup.find_all(is_day)
    days = [x.parent for x in links]
    return days


def get_day_data(day_soup):
    fields = list(day_soup.strings)
    assert len(fields) == 4

    calendar_day = int(fields[0])
    temp_max = int(fields[1])
    temp_min = int(fields[3])

    weather = day_soup.img['alt']

    # print('day: {} max: {} min: {} weather: {}'.format(
    #     calendar_day,
    #     temp_max,
    #     temp_min,
    #     weather)
    # )

    day_entry = weather_entry(calendar_day, temp_max, temp_min, weather)
    return day_entry


def find_month_tables(html_soup):
    weather_tables = html_soup.find_all(class_='yjw_table')
    return weather_tables

##############TODO#################
year_name = '201'
location_name = 'chibaraja'

def find_year(html_soup):
    global year_name
    year_name += 'X'
    return year_name

def find_location(html_soup):
    global location_name
    location_name += 'Y'
    return location_name
##############TODO#################


def scrap_html(html):
    # make soup
    html_soup = bs4.BeautifulSoup(html, 'html.parser')

    # check for valid content
    # TODO
    year = find_year(html_soup)  # TODO
    location = find_location(html_soup)  # TODO

    # find tables
    # 1 table represents 1 month
    months_soup = find_month_tables(html_soup)

    monthly_weather_list = []  # Holds MonthlyWeather instances

    # get days
    for month in months_soup:
        calendar_name = month['id']     # TODO get month name
        print(calendar_name)            # TODO get month name
        location = find_location(html)

        monthly_weather = MonthlyWeather(
            location, year, calendar_name,
        )

        days_soup = find_days_in_month(month)
        monthly_weather_data_list = [get_day_data(day) for day in days_soup]
        monthly_weather.daily_weather = monthly_weather_data_list

        monthly_weather_list.append(monthly_weather)

    return monthly_weather_list
