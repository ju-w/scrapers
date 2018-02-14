import requests
import json


urlstring = f'https://www.tmdn.org/tmview/search-tmv?_search=false&nd=1518359249400&rows=40&page=1&sidx=score&sord=asc&q=oc%3AGB+AND+ad%3A2017-12-01..2018-02-07&fq=%5B%5D&pageSize=40&facetQueryType=0&selectedRowRefNumber=null&providerList=null&expandedOffices=null'

cookies = {
	'TSPD_101': '0827db1318ab2800b0ed77c820f6ae25c11eb502c842d4e406cf0effc2a0b3c4f01cbadd8beec6c64322abc1b32bde6008f78e4f20051000b0c10f052ef44cff3a0aef4ac3e40c32'
}

headers = {
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-GB,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6,ja;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
	'Content-Type': 'application/json; charset=utf-8',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'close'
}


a = requests.get(urlstring, headers=headers, cookies=cookies)

a.raise_for_status()
print(a.status_code)

print(a.text)

j = json.loads(a.text)

print(json.dumps(j, sort_keys=True, indent=4, ensure_ascii=False))

# print(j['rows'])


for row in j['rows']:

	print(row['ApplicantName'])
	print(row['ST13'])
	print(row['an'])
	try:
		print(row['MarkVerbalElementText'])
	except KeyError as e:
		print(e)

	print('')




# print(a.text)
