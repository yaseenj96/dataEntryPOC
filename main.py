from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSd56AgLkLvHRZiUHKIqOUHzltYyle6iLGnQaSzMKUWGKN0TJg/viewform?usp=sf_link'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://appbrewery.github.io/Zillow-Clone/')

#Scrape price, address, and links:
prices = driver.find_elements(By.CLASS_NAME, value="PropertyCardWrapper__StyledPriceLine")
text_prices = []
for price in prices:
    text_prices.append(price.text[0:6])

addresses = driver.find_elements(By.CSS_SELECTOR, value="address")
text_addresses =[]
for address in addresses:
    text_addresses.append(address.text)

links = driver.find_elements(By.CLASS_NAME, value="StyledPropertyCardDataArea-anchor")
text_links =[]
for link in links:
    text_links.append(link.get_attribute('href'))

driver.close()
driver.quit()

driver2 = webdriver.Chrome(options=chrome_options)
driver2.get(form_link)

for n in range(0, len(text_prices)):
    address_input = driver2.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver2.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver2.find_element(By.XPATH, value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(text_addresses[n])
    price_input.send_keys(text_prices[n])
    link_input.send_keys(text_links[n])
    submit_button = driver2.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    submit_another_response = driver2.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response.click()

driver2.close()
driver2.quit()