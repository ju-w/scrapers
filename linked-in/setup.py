import csv
import time
import random

from selenium import webdriver

d = webdriver.Chrome()

def pp(l):
	for x in l:
		print(x)

with open('in.csv', newline='') as f:
	reader = csv.reader(f, dialect='excel-tab')

	la = [row for row in reader]


pp(la)

for x in la:
	x.append(x[3].split(', ')[0])

def ww(s):
      for x in s:
          a.send_keys(x)
          time.sleep(0.001 + random.random()/30)


a = d.find_element_by_xpath("//form[@id='extended-nav-search']//input")


i = 0
l = None

def g():
	global l
	l = la[i]
	print(l)
	a.clear()
	ww(' '.join(l[0:2]))

def m():
	ww(' ' + l[5])

def mm():
	ww(' ' + l[2])


def c():
	d.find_elements_by_xpath("//form[@id='extended-nav-search']//artdeco-typeahead-results-container/ul/li")[0].click()

def cc():
	d.find_elements_by_xpath(
		"//form[@id='extended-nav-search']//artdeco-typeahead-results-container/ul/li"
		)[-1].click()


def n():
	global i
	l.append('NONE')
	print(l)
	i = i+1

def y():
	global i
	l.append(d.current_url)
	print(l)
	i = i+1

def check():
	_list = d.find_elements_by_xpath(
				"//form[@id='extended-nav-search']//artdeco-typeahead-results-container/ul/li")

	if len(_list) != 2:
		return False

	t = _list[0].text.lower()
	if 'see all results' in t:
		return False

	elif (l[0].lower() in t) and (l[1].lower() in t):
		return True

	else:
		return False


while True:

	g()
	m()

	time.sleep(2.5)

	if check():
		c()
		time.sleep(3)
		y()

	else:
		n()



def o():

	global l, i
	l = la[i]

	if l[-1] != 'NONE':
		l.append(l[-1])
		i += 1
		continue

	g()
	m()
	# cc()

def o():

	global l, i
	l = la[i]

	while l[-1] != 'NONE':
	    l.append(l[-1])
	    print(l[-1])
	    i += 1
	    l = la[i]
	    continue

	g()
	m()



def save():
	with open('out.csv', 'w', newline='') as f:
		wr = csv.writer(f, dialect='excel-tab')
		for x in la:
			wr.writerow(x)



x = 1
while True:
    try:
        print x
        time.sleep(.3)
        x += 1
    except KeyboardInterrupt:
        break
