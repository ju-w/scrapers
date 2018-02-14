from __future__ import print_function

import json
import re
import datetime

import bs4
import requests


def scrape_url(url):

	print('scraping: ', url)

	headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
	html = requests.get(url, headers=headers)
	soup = bs4.BeautifulSoup(html.text, 'html.parser')
	rows_s = soup.find_all('tr', event_attr_id=True, event_timestamp=True)

	table_data = []

	for r in rows_s:
		try:
			row_data = extract_data(r)
			table_data.append(row_data)
		except Exception as e:
			print(e)

	# print(table_data)
	table_data_json = json.dumps(table_data)
	# print(table_data_json)
	return table_data_json


def extract_data(row_s):

	def stripped_text(soup):
		return ''.join(soup.stripped_strings)

	def number_from_s(soup):
		text = stripped_text(soup)
		# print(text)
		m = re.search('[+-]?[0-9,.]+', text)
		if not m:
			# return 0 if we cant make number
			return 0
		n_s = m.group().replace(',', '')

		# try making int first, if it fails make float
		try:
			int_n = int(n_s)
			return int_n

		except ValueError:
			try:
				float_n = float(n_s)
				return float_n

			# this should not happen
			except ValueError:
				return 0


	row_data = {}

	i_s = row_s.attrs['id']
	row_data['event_id'] = int(i_s.lstrip('eventRowId_'))

	d_s = row_s.attrs['event_timestamp']
	# row_data['event_date'] = datetime.datetime.strptime(d_s, '%Y-%m-%d %H:%M:%S')
	row_data['event_date'] = d_s

	c_s = row_s.find('td', class_='flagCur')
	row_data['cur'] = stripped_text(c_s)

	b_s = row_s.find_all(class_="grayFullBullishIcon")
	row_data['imp'] = len(b_s)

	e_s = row_s.find('td', class_="event")
	row_data['event'] = stripped_text(e_s)

	a_s = row_s.find('td', class_='act')
	row_data['actual_text'] = a_s['title']
	row_data['actual'] = number_from_s(a_s)

	f_s = row_s.find('td', class_='fore')
	row_data['forecast'] = number_from_s(f_s)

	p_s = row_s.find('td', class_='prev')
	row_data['previous'] = number_from_s(p_s)

	print(row_data)
	return row_data
