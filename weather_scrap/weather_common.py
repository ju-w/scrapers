"""Commons

Julian Wittmann
2017-03-31
Python 3.5
"""

from collections import namedtuple

weather_entry = namedtuple('weather_entry', 'day, max, min, weather')
csv_entry = namedtuple('csv_entry', 'day high_low weather weather_icon')

weather_symbols = {
    '晴れ': '☀',
    '雨': '☂',
    '曇り': '☁',
    '雪': '❄',
}
