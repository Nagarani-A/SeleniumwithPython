from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.way2automation.com/angularjs-protractor/multiform/#/form/profile")

user_ele = driver.find_element_by_name("name")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("email")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("test")
pwd_ele.send_keys("test")

driver.find_element_by_xpath("//*[@id='form-views']/div[3]/div/a").click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=xbox]")
print("status", roundtrip_radio.is_selected())

onetrip_radio = driver.find_element_by_css_selector("input[value=ps]")
print("status", onetrip_radio.is_selected())




'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://demo.guru99.com/selenium/newtours/")

user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")


driver.find_element_by_name("submit").click()


roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print("status",roundtrip_radio.is_selected())

onetrip_radio=driver.find_element_by_css_selector("input[value=oneway]")
print("status",onetrip_radio.is_selected())


'''