print 'hahaha'


from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('window-size=1200x600')

c = webdriver.Chrome(chrome_options=options)

c.get('https://coincheckup.com/coins/dogecoin/charts/basic')

b = c.find_element_by_xpath('//*[@ng-if="::(!_.isNull(details.scores.E))"]/span')

print b.text



# USD price




# b = c.find_element_by_xpath('//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[1]')

# # BTC price
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/div[2]/span'

# # ETH price
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[2]'

# # Price: Last 1h
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[3]'

# # Price: Last 24 h
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[4]'

# # Price: Last 7 days
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[5]'

# # Price: Last 30 days
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[6]'

# # Volume: Last 24h
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[7]'

# # Market cap
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[8]/span[1]'

# # % of total market
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[9]'

# # Org.structure

# # Consensus method

# # Algorithm

# # Updated

# # Total coin analysis score
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[1]/span'

# # Open communication channels
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[2]/span'


# # Team strength
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[3]/span'

# # Product strength
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[4]/span'


# Github


# Coin strength
# Brand awareness/Buzz
# Advisory board strength
# Acritivity on social media

# Average Daily ROI
# Average Monthly ROI
# Total ROI
# Volatility trailing 30 days
# Volatility trailing 7 days
