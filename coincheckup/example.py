from selenium import webdriver
from coincheckup_scraper import scrape_url

# make driver

# headless
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(chrome_options=options)

# normal
driver = webdriver.Chrome()


try:
	doge = scrape_url('https://coincheckup.com/coins/dogecoin/charts/basic', driver)
	print doge

	btc = scrape_url('https://coincheckup.com/coins/bitcoin/charts/basic', driver)
	print btc

	eth = scrape_url('https://coincheckup.com/coins/ethereum/charts/basic', driver)
	print eth

finally:
	# quit driver
	driver.quit()
