from selenium import webdriver


driver = webdriver.Chrome() #get chrome driver from installed driver

driver.get('http://netaccess.iitm.ac.in')

usernameBox = driver.find_element('xpath','//*[@id="username"]')
passBox = driver.find_element('xpath','//*[@id="password"]')
loginBtn = driver.find_element('xpath','//*[@id="submit"]')
approveBtn = driver.find_element('xpath','//*[@id="content"]/div/div[1]/div[2]/a/span')
oneDayBtn = driver.find_element('xpath','//*[@id="content"]/div/div[1]/form/div[2]/label')
autorizeBtn = driver.find_element('xpath','//*[@id="approveBtn"]')

usernameBox.send_keys('roll number')
passBox.send_keys('password')

#click login
loginBtn.click()
#wait for webpage to load
#approveBtn.click()

#wait for webpage to load
oneDayBtn.click()
autorizeBtn.click()

