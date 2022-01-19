from selenium import webdriver
from time import sleep


class Shrek:
    def __init__(self, username, pw):
        
        self.canço = []
        with open('Somebodyoncetoldme.txt', mode='r') as f1:
            for linia in f1:
                ll_par = linia.strip().split()
                for par in ll_par:
                    self.canço.append(par)
        
        self.driver = webdriver.Chrome('D:\Programas\Selenium\chromedriver_win32\chromedriver')
        self.driver.get("https://instagram.com")
        
        sleep(0.5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        print("Ha entrat dins l'usuari")
        sleep(1)

    def open_chat(self, pers):
        print('Opening chat...')
        sleep(1)
        # Click al avio de paper
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')\
            .click()
        sleep(1)
        # Click sobre el buscador i busca la persona
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')\
            .click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input")\
            .send_keys(pers)
        sleep(2)
        # Escull la persona correcta
        final = 'no'
        while final == 'no':
            inp = input('A quina posicio esta? (1, 2, 3, 4,...)\n')
            if inp.isdigit():
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div[{}]/div/div[3]/button'.format(inp))\
                    .click()
                final = input('Es aquest? (yes/no)\n')
        if final == 'yes':
            # Obra el chat
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/button')\
                .click()
        sleep(1)

        
    def send_message(self, text):
       
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")\
            .send_keys(text)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')\
            .click()
        
    def envia_canço(self, ll_pers):
        print('Sending positiviti...')
        print('Enviant la canço a: {}'.format(', '.join(ll_pers)))
        for persona in ll_pers:
            self.open_chat(persona)
            self.send_message('Hola soc el SHREK i vinc de part de a cantar-vos una canço:')
            c = 0
            p = 0
            print(p,'%')
            for par in self.canço[:39]:
                c += 1
                self.send_message(par)
                percent = (c*100)/39
                if abs(percent - p) >= 10:
                    print(int(percent),'%')
                    p = percent
                sleep(2)
            print(100,'%')
            
                
            self.send_message('I fins aqui el meu bot del SHREK!')
                
        
                    

shrek = Shrek('mateugarciacusi', 'mateu115020393')
shrek.envia_canço(['victor_barres', ''])
