from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
'''
//*[@id="main"]/div[3]/div/div/div[3]/div[7]/div/div/div/div[1]/div
//*[@id="main"]/div[3]/div/div/div[3]/div[6]/div/div/div/div[1]/div
//*[@id="main"]/div[3]/div/div/div[3]/div[81]


//*[@id="main"]/div[3]/div/div/div[3]/div[8]/span/div/div
//*[@id="main"]/div[3]/div/div/div[3]/div[7]/span/div/div
'''



class Whats:
    def __init__(self):
        self.ll_nums = []
        self.driver = webdriver.Chrome('D:\Programas\Selenium\chromedriver_win32\chromedriver')
        self.driver.get("https://web.whatsapp.com/")
        
    def extract_nums(self, nom_f_csv, nom_col):
        df = pd.read_csv(nom_f_csv)
        self.ll_nums = list(df[nom_col])

    def ultim_m(self):
        nm = 0
        while nm<15:
            nm += 1
            try:
                print(self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div[{}]'.format(nm)).text)
                print(nm)
            except:
                print('intent numero: {}'.format(nm))
            input()

        return nm
            

    def ves_al_chat(self, num_origen):
        # Buscar numero
        self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(num_origen)
        sleep(2)
        # seleccionar contacte //*[@id="pane-side"]/div[1]/div/div/div[3]/div
        self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
        # tres punts
        self.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div').click()
        # Opcio seleccio missatges
        self.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/ul/li[4]/div').click()
        
    def enviar_missatge(self, missatge):
        for num in self.ll_nums:
            # Buscar numero
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(num)
            sleep(2)
            # seleccionar contacte //*[@id="pane-side"]/div[1]/div/div/div[3]/div
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
##            self.driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[5]').click()
            sleep(1)
            # Escriure missatge
            self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(missatge)
            sleep(1)
            i = input()
            # Enviar
            self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()


    
w = Whats()
##w.extract_nums('contactes.csv', 'numeros telefon')
input()
w.ves_al_chat('633535151')
print(w.ultim_m())
