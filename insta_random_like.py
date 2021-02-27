from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
followings = []
followerss = []
non_mutual = []
def clickk(link):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, link))).click()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
time.sleep(2)
email = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
passw = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

email.clear()
email.send_keys('agiasbayu2@gmail.com')
passw.clear()
passw.send_keys('bajingan1234')
clickk('//*[@id="loginForm"]/div/div[3]/button')

clickk('//*[@id="react-root"]/section/main/div/div/div/div/button')
clickk('/html/body/div[4]/div/div/div/div[3]/button[2]')


def like_random():
    clickk('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
    clickk('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[1]/div')

    try:
        for i in range(5):
            clickk('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            clickk('/html/body/div[5]/div[1]/div/div/a[2]')
    finally:
        clickk('/html/body/div[5]/div[3]/button')
        clickk('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')
        #back to home

def unfollow_random():
    driver.get('https://www.instagram.com/prissepp/')
    buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
    following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
    following_button[0].click()
    for i in range (5):
        clickk(f"/html/body/div[5]/div/div/div[2]/ul/div/li["+(str(i+1))+"]/div/div[3]/button")
        clickk('/html/body/div[6]/div/div/div/div[3]/button[1]')
    clickk('/html/body/div[5]/div/div/div[1]/div/div[2]/button')
    clickk('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')

def follow_random():
    clickk('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
    clickk('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[1]/div')
    clickk('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a')
    time.sleep(2)
    buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
    followers_button = [button for button in buttons if 'followers' in button.get_attribute('href')]
    followers_button[0].click()
    for i in range(5):
        clickk('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i+1)+']/div/div[3]/button')

def check_following():
    username = 'alagias_bayu'
    time.sleep(2)
    user = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    user.send_keys(username)
    user.send_keys(Keys.RETURN)
    time.sleep(2)
    user2 = driver.find_elements_by_xpath("//a[@class='-qQT3']")
    target = [useer for useer in user2 if username in useer.get_attribute('href')]
    target[0].click()
    time.sleep(2)
    buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
    following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
    following_button[0].click()
    time.sleep(2)
    following_window = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
    following_number = driver.find_element_by_xpath( "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
    print(following_number)
    j = 1
    while j <= int(following_number):
        try:
            nama = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(j)+']/div/div[1]/div[2]/div[1]/span/a').text
            followings.append(nama)
            j+=1
        except:
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",following_window
            )
    # print(followings)
    clickk('/html/body/div[5]/div/div/div[1]/div/div[2]/button')

def check_followers():
    # username = 'alagias_bayu'
    # time.sleep(2)
    # user = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    # user.send_keys(username)
    # user.send_keys(Keys.RETURN)
    # time.sleep(2)
    # user2 = driver.find_elements_by_xpath("//a[@class='-qQT3']")
    # target = [useer for useer in user2 if username in useer.get_attribute('href')]
    # target[0].click()
    # time.sleep(2)
    buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
    following_button = [button for button in buttons if 'followers' in button.get_attribute('href')]
    following_button[0].click()
    time.sleep(2)
    follower_window = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
    follower_number = driver.find_element_by_xpath( "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
    print(follower_number)
    j = 1
    while j <= int(follower_number):
        try:
            nama = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(j)+']/div/div[1]/div[2]/div[1]/span/a').text
            followerss.append(nama)
            j+=1
        except:
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",follower_window
            )
    # print(followerss)
    clickk('/html/body/div[5]/div/div/div[1]/div/div[2]/button')

def check_unmutual():
    non_mutual = [user for user in followings if user not in followerss]
    print(non_mutual)


# unfollow_all()
# like_random()
# follow_random()
check_following()
check_followers()
check_unmutual()