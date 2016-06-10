import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

browser = webdriver.Firefox()
time.sleep(5)
browser.get('http://www.amazon.com')
SigninElem = browser.find_element_by_css_selector('#nav-link-yourAccount > span:nth-child(1)')
SigninElem.click()
EmailElem = browser.find_element_by_css_selector('#ap_email')
EmailElem.send_keys('hrliaghati@hotmail.com')
PasswordElem = browser.find_element_by_css_selector('#ap_password')
PasswordElem.send_keys('asheAmazon127')
PasswordElem.send_keys(Keys.ENTER)
Cards = ['#pm_5','#pm_8'] # use 1,2,3,5
Iterations = [10,10]
i = 0
localtime = (time.asctime(time.localtime( time.time() )))
filename = 'Amazon Purchases ' + localtime.replace(':','_')+'.txt'
f = open(filename,'w')
for CardNumber in Cards:
    for iteration in range(Iterations[i]):
        WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#nav-xshop > a:nth-child(3)')))
        browser.get('https://www.amazon.com/Amazon-1_US_Email-Gift-Card-Email/dp/B004LLIKVU/ref=lp_2238192011_1_1?s=gift-cards&ie=UTF8&qid=1452923016&sr=1-1')
        WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#gc-order-form-custom-amount')))
        AmountElem = browser.find_element_by_css_selector('#gc-order-form-custom-amount')
        AmountElem.send_keys('0.5')
        AmountElem = browser.find_element_by_css_selector('#gc-order-form-recipients')
        AmountElem.send_keys('hrliaghati@gmail.com')
        localtime = (time.asctime(time.localtime( time.time() )))
        Sender = 'Robert ' + localtime
        AmountElem = browser.find_element_by_css_selector('#gc-order-form-senderName')
        AmountElem.send_keys(Sender)
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#gc-add-to-cart-button')))
        AcctElem = browser.find_element_by_css_selector('#twotabsearchtextbox')
        AcctElem.send_keys('alphabet soup')
        for k in range(13):
            AcctElem.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        AddtoCart = browser.find_element_by_css_selector('#gc-add-to-cart-button')
        AddtoCart.click()
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#gc-mini-cart-proceed-to-checkout > span:nth-child(1) > input:nth-child(1)')))
        Proceed = browser.find_element_by_css_selector('#gc-mini-cart-proceed-to-checkout > span:nth-child(1) > input:nth-child(1)')
        Proceed.click()
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,CardNumber)))
        RadioBtn = browser.find_element_by_css_selector(CardNumber)
        RadioBtn.click()
        ContinueElem = browser.find_element_by_css_selector('#continue-top')
        ContinueElem.click()
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.place-your-order-button')))
        PlaceOrder = browser.find_element_by_css_selector('.place-your-order-button')
        PlaceOrder.click()
        line = Sender+'\t'+CardNumber+'\n'
        f.write(line)    
    i = i+1;

f.close()
        