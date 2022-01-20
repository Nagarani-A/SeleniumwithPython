from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get("https://demo.guru99.com/selenium/newtours/")

driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

user_ele = driver.find_element_by_name("userName").send_keys("mercury")

driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()
