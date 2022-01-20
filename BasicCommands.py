from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get("https://www.w3schools.com/html") #W3

print(driver.title)  #returns title
print(driver.current_url) #returns URL

driver.find_element_by_xpath("//*[@id='main']/div[4]/a").click()
#time.sleep(5)

driver.close()