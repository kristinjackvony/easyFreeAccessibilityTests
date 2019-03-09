from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/s?k=goodnight+moon&ref=nb_sb_noss_1")
elem = driver.find_element_by_class_name("s-image")
val = elem.get_attribute('alt')
if val == 'Goodnight Moon':
	print('Alt text is present')
else:
	print('Alt text is missing or incorrect')

driver.get("https://www.audi.com/en.html")
driver.find_element_by_link_text("DE").click()
try:
	elem = driver.find_element_by_link_text("Kontakt")
	if elem:	
		print('Page is in German')
except:
	print('Page is not in German')

driver.quit()
