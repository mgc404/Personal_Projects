
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from random import randint
from usuari import username, pasword

class PrimevideoBot:
    def __init__(self, username, pw, ubi):
        self.d = {1: 6, 2: 22, 3: 25, 4: 19, 5: 28, 6: 26, 7: 27, 8: 24, 9: 27}
        self.driver = webdriver.Chrome('D:\Programas\The_office\chromedriver_win32\chromedriver')
        self.username = username
        self.pasword = pw
        self.driver.get("https://www.amazon.com/ap/signin?accountStatusPolicy=P1&clientContext=258-3560153-7500757&language=es_ES&openid.assoc_handle=amzn_prime_video_desktop_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_encoding%3DUTF8%26location%3D%252Fref%253Dav_nav_sign_in")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ap_email"]')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="ap_password"]')\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')\
            .click()
        sleep(1)
        
    def random_episode(self):
        self.driver.find_element_by_xpath('//*[@id="pv-search-nav"]')\
            .send_keys('the office')
        print('login successful!')
        sleep(1)
        print('Escollint episodi...')
        self.driver.find_element_by_xpath('//*[@id="pv-nav"]/div/div/div[2]/div/ol/li[1]/ol/ol/li[1]/a/strong')\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="av-search"]/div[2]/div[1]/div[1]/div')\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="av-search"]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/a')\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="a-page"]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/label')\
            .click()
        sleep(1)
        temporada = randint(1,9)
        print('Temporada ' + str(temporada))
        self.driver.find_element_by_xpath('//*[@id="a-page"]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/ul/li[{}]/a'.format(temporada))\
            .click()
        sleep(2)
        episode = randint(0,self.d[temporada])
        print('Episodi ' + str(episode))
        self.driver.find_element_by_xpath('//*[@id="av-ep-episodes-{}"]/div[1]/div/div/a'.format(episode))\
            .click()

        
bot = PrimevideoBot(username, pasword, ubi)
bot.random_episode()
print("Disfruta del teu episodi aleatori de 'The Office'")
