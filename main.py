from selenium import webdriver


driver = webdriver.Chrome() #get chrome driver from installed driver

driver.get('http://netaccess.iitm.ac.in/account/login')

usernameBox = driver.find_element('xpath','//*[@id="username"]')
passBox = driver.find_element('xpath','//*[@id="password"]')
loginBtn = driver.find_element('xpath','//*[@id="submit"]')


usernameBox.send_keys('rollnumber')
passBox.send_keys('password')

#click login
loginBtn.click()

#wait for webpage to load
approveBtn = driver.find_element('xpath','//*[@id="content"]/div/div[1]/div[2]/a/span')
approveBtn.click()

#wait for webpage to load
oneDayBtn = driver.find_element('xpath','//*[@id="content"]/div/div[1]/form/div[2]/label')
authorizeBtn = driver.find_element('xpath','//*[@id="approveBtn"]')

oneDayBtn.click()
authorizeBtn.click()

