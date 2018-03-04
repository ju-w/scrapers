"""Scrap weather data from http://weather.yahoo.co.jp

Julian Wittmann
2017-03-31
Python 3.5
"""

import os
import sys

import requests

from weather_common import *
from weather_csv import *
from weather_scrap import *


def download_html(url):
    print('Downloading html')
    req_obj = requests.get(url)
    print(req_obj.encoding)
    html = req_obj.text
    return html


def save_html(html):
    with open('my.html', 'x', encoding='utf-8') as fd:
        print('saving')
        fd.write(html)
        fd.close()


def get_html(url, from_local_buffer=True):
    print("get_html")
    if from_local_buffer is True:
        if not os.path.isfile('my.html'):
            print("no file")
            html_raw = download_html(url)
            save_html(html_raw)

        with open('my.html', encoding='utf-8') as fd:
            html = fd.read()
            fd.close()
    else:
        html = download_html(url)

    # check if it worked properly

    return html


def main(url):
    print(url)

    # get html
    site_html = get_html(url, from_local_buffer=False)

    # pull out information
    scrapped_data = scrap_html(site_html)

    # save information
    for monthly_weather in scrapped_data:
        write_weather_to_csv(monthly_weather)


if __name__ == '__main__':
    # url = sys.argv[1]
    url = 'http://weather.yahoo.co.jp/weather/jp/past/12/4510.html?c=2017&m=1'
    main(url)

