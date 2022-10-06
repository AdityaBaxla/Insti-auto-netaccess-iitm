from selenium import webdriver

driver = webdriver.Chrome() #get chrome driver from installed driver

driver.get('http://netaccess.iitm.ac.in')

usernameBox = driver.find_element_by_xpath(//*[@id="username"])
passBox = driver.find_element_by_xpath(//*[@id="password"])