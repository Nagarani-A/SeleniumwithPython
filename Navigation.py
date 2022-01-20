from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get("https://www.w3schools.com/html/") #W3
print(driver.title)  #returns title

driver.get("https://www.tutorialspoint.com/blue_prism/index.htm") #TUT
time.sleep(5) #time delay

print(driver.title)  #returns title

driver.back()
time.sleep(5) #time delay

print(driver.title) #W3

driver.forward()
time.sleep(5) #time delay

print(driver.title) #TUT

