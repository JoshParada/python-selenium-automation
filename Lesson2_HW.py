from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#__________________________________________________PART 1________________________________________________

# open the url
# driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
# sleep(3)
#
# #Amazon logo
# driver.find_element(By.XPATH, "//i[@role='img']")

# #Email field
# driver.find_element(By.ID, "ap_email")

# #Continue button
# driver.find_element(By.ID, "continue")

# #Conditions of use link
# driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")

# #Privacy Notice link

# driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

# #Need help link
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# #Forgot your password link
# driver.find_element(By.ID, "auth-fpp-link-bottom")

# #Other issues with Sign-In link
# driver.find_element(By.ID, "ap-other-signin-issues-link")

# #Create your Amazon account button
# driver.find_element(By.ID, "createAccountSubmit")




#__________________________________________________PART 2________________________________________________

# open the url
driver.get('https://www.target.com')
sleep(3)

#click sign in button
driver.find_element(By.XPATH, "//*[text()='Sign in']").click()

#click sign in button from sidebar
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

#verification via find element
sleep(3)
driver.find_element(By.ID, "login")

#verification via text
actual_result = driver.find_element(By.ID, "login").text
expected_result = "Sign in with password"

assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result}'

sleep(3)
driver.quit()