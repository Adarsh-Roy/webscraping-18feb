from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox(executable_path=".\\geckodriver.exe") 
driver.get("https://moodle.iitd.ac.in")
text = driver.find_element_by_id("login").text
if ("add" in text) :
    captcha = int(text.split(" ")[5]) + int(text.split(" ")[7])
elif ("subtract" in text):    
    captcha = int(text.split(" ")[5]) - int(text.split(" ")[7])
elif ("first" in text):
    captcha = int(text.split(" ")[7])
elif ("second" in text):
    captcha = int(text.split(" ")[9])
username = driver.find_element_by_id("username")
username.send_keys(input("Enter username: "))
password = driver.find_element_by_id("password")
password.send_keys(input("Enter password: "))
login = driver.find_element_by_id("loginbtn")
captcha_input = driver.find_element_by_id("valuepkg3")
captcha_input.clear()
captcha_input.send_keys(captcha)
actions = ActionChains(driver)
actions.click(login)
actions.perform() 



