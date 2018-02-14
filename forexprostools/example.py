from investing_scraper import scrape_url

url1 = "https://sslecal2.forexprostools.com/?columns=exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&category=_employment,_economicActivity,_inflation,_credit,_centralBanks,_confidenceIndex,_balance,_Bonds&features=datepicker,timezone&countries=25,34,32,6,37,72,71,22,17,51,39,14,33,10,35,43,60,38,36,110,11,26,9,12,4,5&calType=week&timeZone=15&lang=51"
url2 = "https://sslecal2.forexprostools.com/?columns=exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&category=_employment,_economicActivity,_inflation,_credit,_centralBanks,_confidenceIndex,_balance,_Bonds&features=datepicker,timezone&countries=25,34,32,6,37,72,71,22,17,51,39,14,33,10,35,43,60,38,36,110,11,26,9,12,4,5&calType=day&timeZone=15&lang=51"

try:
	j1 = scrape_url(url1)
	print j1
except Exception as e:
	print e

try:
	j2 = scrape_url(url2)
	print j2
except Exception as e:
	print e
