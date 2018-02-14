import requests
import bs4
import re

st13 = 'GB500000003275444'
# st13 = 'GB500000003275316'
st13 = 'GB500000003275100'

urlstring = f'https://www.tmdn.org/tmview/get-detail?st13={st13}'

cookies = {
	'TSPD_101': '0827db1318ab2800b0ed77c820f6ae25c11eb502c842d4e406cf0effc2a0b3c4f01cbadd8beec6c64322abc1b32bde6008f78e4f20051000b0c10f052ef44cff3a0aef4ac3e40c32'
}

headers = {
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-GB,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6,ja;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
	'Content-Type': 'application/json; charset=utf-8',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	# 'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'close'
}

a = requests.get(urlstring, headers=headers, cookies=cookies)

r = re.compile('\(\d{3}\)')

def mm(s):
	return re.match(r, s)

def pp(s):
	print(s.prettify())

s = bs4.BeautifulSoup(a.text, 'html.parser')

bods = s.find_all('tbody', class_='bodySection')

for b in bods:
	pp(b)
	print('')


# print(bods[1].prettify())



# list of goods and services

des = bods[1].find_all('tbody')[1]

for x in des.stripped_strings:
	if mm(x):
		print('')
	else:
		print(x)


print('')
print('')
print('')
print('')

inf = bods[0]


for x in inf.stripped_strings:
	if mm(x):
		print('')
	else:
		print(x)


print('')
print('')
print('')
print('')




ads = bods[2].find_all('table', class_="marginTopLeftBottom")


for a in ads:
	for r in a.find_all('td'):
		for i in r.stripped_strings:
			print(i)

	print('')
	print('')





rep = bods[3]
for i in rep.stripped_strings:
	print(i)



prio = bods[7]
for i in prio.stripped_strings:
	print(i)


# print(bods[1].get_text())

# print(len(bods))

# print(a.text)

# soup = bs4.BeautifulSoup(html.text, 'html.parser')
# rows_s = soup.find_all('tr', event_attr_id=True, event_timestamp=True)
