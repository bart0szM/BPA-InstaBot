from selenium import webdriver
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

user_name = "iamlearningpython"
cond = "false"

Alphabet = ['a' ,'b' ,'c','d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k','l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'w' ,'v' ,'x' ,'y' ,'z']

def generator():
    char1 = random.randint(0, 25)
    char2 = random.randint(0, 25)
    char3 = random.randint(0, 25)
    char4 = random.randint(0, 25)
    return Alphabet[char1] + Alphabet[char2] + Alphabet[char3] + Alphabet[char4]

with open("path", "r") as f:
    my_path = f.readline()
driver = webdriver.Chrome(my_path)
driver.get("https://www.instagram.com/")

try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Zaloguj się"))) 
    driver.find_element_by_link_text("Zaloguj się").click()

except:
      WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Log in")))
      driver.find_element_by_link_text("Log in").click()

WebDriverWait(driver, 3).until(EC.title_contains("Login")) #Wait for login page to load

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "username")))
driver.find_element_by_name("username").send_keys(user_name)

with open("pass", "r") as f:
    my_password = f.readline()
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "password")))
driver.find_element_by_name("password").send_keys(my_password)
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\_0mzm- > .Igw0E")))
driver.find_element_by_css_selector(".\_0mzm- > .Igw0E").click() #logon button

WebDriverWait(driver, 5).until(EC.title_is("Instagram")) #Wait for welcome page

for x in range (0,10): #generate 10 random instagram profiles (from 0 to 9)

    with open("insta.txt", "r") as f:
        user = (generator())  # custom made function
        for line in f.readlines(): #looping through the file if the user has been followed already
            if line.strip() == user:
                cond = "true"
    if cond != "true":  #if user is not in the file then it goes to it's profile
        driver.get("http://www.instagram.com/" + user)
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\_6VtSN")))
            driver.find_element_by_css_selector(".\_6VtSN").click() #Click FOLLOW button
            with open("insta.txt", "a") as f: #write that user down
                print(user, file=f)
        except:
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".BY3EC")))
                driver.find_element_by_css_selector(".BY3EC").click() #Click FOLLOW button if account is private
                with open("insta.txt", "a") as f: #write that user down
                    print(user, file=f)
            except:
                time.sleep(0.25) #Do nothing if there is no valid account

driver.get("http://www.instagram.com/" + user_name)

WebDriverWait(driver, 3).until(EC.title_contains(user_name))

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "glyphsSpriteSettings__outline__24__grey_9")))
driver.find_element_by_class_name("glyphsSpriteSettings__outline__24__grey_9").click()

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Log Out']")))
driver.find_element_by_xpath("//*[text()='Log Out']").click()

time.sleep(3)

driver.close()
