from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import random
proxy = '127.0.0.1:10808'
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
# options.add_argument('--proxy-server=socks5://' + proxy)
driver = webdriver.Chrome(options=options)
url="https://passport.bilibili.com/login"
url2="https://live.bilibili.com/22632157"
driver.get(url)
username = driver.find_element_by_id('login-username')
password = driver.find_element_by_id('login-passwd')
name=""
paswd=""
username.send_keys(name)
password.send_keys(paswd)
time.sleep(1.0)
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
time.sleep(15.0)
driver.get(url2)
time.sleep(3.0)
comment = driver.find_element_by_xpath('//*[@id="control-panel-ctnr-box"]/div[2]/div[2]/textarea')
# comment.send_keys("bot test")
time.sleep(1.0)
driver.execute_script("window.scrollBy(0,500)")
while 1:
    c=random.randint(0, 5)
    # list="测试测试测试测试测试测试测试测试"
    text="卒業しろ"*c
    time.sleep(0.5)
    comment.send_keys(text)
    print(text)
    driver.find_element_by_xpath('//*[@id="control-panel-ctnr-box"]/div[3]/div/button/span').click()


