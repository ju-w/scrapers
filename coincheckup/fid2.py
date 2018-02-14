import json

xpaths = {
# USD price
'usd_price':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[1]',

# BTC price
'btc_price':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/div[2]/span',

# ETH price
'eth_price':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[2]',

# Price: Last 1h
'last_1h':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[3]',

# Price: Last 24 h
'last_24h':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[4]',

# Price: Last 7 days
'last_7days':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[5]',

# Price: Last 30 days
'last_30days':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[6]',

# Volume: Last 24h
'volume_24h':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[7]',

# Market cap
'market_cap':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[8]/span[1]',

# % of total market
'perc_of_total_market':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[2]/span[9]',

# Org.structure

# Consensus method

# Algorithm

# Updated

# Total coin analysis score
'total_coin_analysis_score':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[1]/span',

# Open communication channels
'open_communication_channels':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[2]/span',

# Team strength
# '//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[3]/span'

# Product strength
'product_strength':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[4]/span',

# Github
'github':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[5]/span',

# Coin strength
'coin_strength':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[6]/span',

# Brand awareness/Buzz
'brand_awareness_buzz':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[7]/span',

# Advisory board strength

# Acritivity on social media
'activity_on_social_media':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[5]/dl/dt[9]/span',

# Average Daily ROI
'average_daily_roi':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[6]/span[1]',

# Average Monthly ROI
'average_monthly_roi':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[6]/span[2]',

# Total ROI
'total_roi':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[6]/span[3]',

# Volatility trailing 30 days
'volatility_trailing_30days':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[6]/span[4]',

# Volatility trailing 7 days
'volatility_trailing_7days':
'//*[@id="content"]/div[2]/section/div/div/div[2]/div/div[2]/div/div[6]/span[5]',

}


print xpaths


xp_json = json.dumps(xpaths)

for x in xpaths:
	print(x)

print xp_json

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://coincheckup.com/coins/dogecoin/charts/basic')

res = {
	k: driver.find_element_by_xpath(v).text for k, v in xpaths.viewitems()
}

res_json = json.dumps(res)

print(res_json)


driver.close()
