from selenium import webdriver
import random
import time

user_name = "iamlearningpython"

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
driver.get("http://www.instagram.com/")

time.sleep(0.5)
driver.find_element_by_link_text("Zaloguj się").click()
time.sleep(0.5)
driver.find_element_by_name("username").send_keys(user_name)
time.sleep(0.25)
with open("pass", "r") as f:
    my_password = f.readline()
driver.find_element_by_name("password").send_keys(my_password)
time.sleep(0.25)
driver.find_element_by_css_selector(".\_0mzm- > .Igw0E").click() #logon button
time.sleep(0.25)

for x in range (0,10): #generate 10 random instagram profiles (from 0 to 9)

    with open("insta.txt", "r") as f:
        user = (generator())  # custom made function
        for line in f.readlines(): #looping through the file if the user has been followed already
            if line.strip() == user:
                cond = "true"
    if cond != "true":  #if user is not in the file then it goes to it's profile
        time.sleep(0.5)
        driver.get("http://www.instagram.com/" + user)
        time.sleep(0.25)
        try:
            driver.find_element_by_css_selector(".\_6VtSN").click() #Click FOLLOW button
            time.sleep(0.25)
            with open("insta.txt", "a") as f: #write that user down
                print(user, file=f)
        except:
            try:
                time.sleep(0.25)
                driver.find_element_by_css_selector(".BY3EC").click() #Click FOLLOW button if account is private
                with open("insta.txt", "a") as f: #write that user down
                    print(user, file=f)
            except:
                time.sleep(0.25) #Do nothing if there is no valid account
driver.close()

time.sleep(5)
