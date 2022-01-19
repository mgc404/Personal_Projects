'''
exemple:
aveiro-Todos-Todos-Personas mayores-Estructura residencial para personas mayores

Posar data directa a un excel:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd


class Miki:
    def __init__(self):
        self.driver = webdriver.Chrome('D:\Programas\Selenium\chromedriver_win32\chromedriver')
        self.driver.get("http://www.cartasocial.pt/index2.php?filtrar=hidden&foco=cb_distrito&cod_distrito=02&cod_concelho=0&cod_freguesia=0&cod_area=21&cod_valencia=2107&dcf=02")
        self.districte = ''
        self.data_frame = pd.DataFrame({'Distrito':[], 'Nombre':[], 'Código Postal':[], 'Entidad propietária':[],\
                                        'Natureza Jurídica':[], 'Respostas Sociais':[], 'Capacidade':[],\
                                            'Utentes':[], 'Horário':[], 'Última Actualização':[],\
                                        'Entidade Gestora':[], 'Natureza Jurídica(EG)':[], 'Links repes':[], 'dos resis en un link':[]})
        self.equip = 0
        self.num_pagines = 0
        self.capacitat = 0
        self.utentes = 0
        self.rapid = False
        self.links_repe = []
        self.ll_2resis = []
        print('BOT iniciat')

    def torna_inici(self):
        self.driver.get("http://www.cartasocial.pt/index2.php?filtrar=hidden&foco=cb_distrito&cod_distrito=02&cod_concelho=0&cod_freguesia=0&cod_area=21&cod_valencia=2107&dcf=02")
            
    def comprova_capacitat(self, dist, rapid=False):
        self.rapid = rapid
        for i in range(2,20): # recorro els districtest
            # Selecciono el districte
            self.driver.find_element_by_xpath('//*[@id="cb_distrito"]/option[{}]'.format(i))\
                .click()
            self.districte = self.driver.find_element_by_xpath('//*[@id="cb_distrito"]/option[{}]'.format(i)).text
            if self.districte == dist:
                #Selecciono els parametres restants
                self.driver.find_element_by_xpath('//*[@id="cb_area"]/option[7]')\
                    .click()
                self.driver.find_element_by_xpath('//*[@id="cb_valencia"]/option[5]')\
                    .click()
                # Fa click sobre el buscador
                self.driver.find_element_by_xpath('//*[@id="pesq"]')\
                    .click()
                print('-'*30+' Districte actual: {} '.format(self.districte) + '-'*30)
                # Recorre les pagines
                self.recorre_les_pagines(test=True)
                self.torna_inici()
                break
        # Escriu en el excel
        with pd.ExcelWriter("prova_districte.xlsx") as writer:
            self.data_frame.to_excel(writer, index = False, sheet_name=self.districte)
            
            
    def get_llistes(self, n):
        b = False
        ll_general = [[],[],[],[]]
        for fila in range(3, n+3):
            i = 0
            for columna in range(2, 6):
                try:
                    ll_general[i].append(self.driver.find_element_by_xpath('//*[@id="corpo2as"]/div/table[1]/tbody/tr[{}]/td[{}]'.format(fila,columna)).text)
                except:
                    b = True
                    break
                i += 1
            if b:
                break
        return ll_general
    
    def ompla_DataFrame(self, nom, cp, ep, nj, ll_rs, ll, eg, nj_eg, test, pag):
        n = len(ll[0])
        dos_resis = 0
        dos_resis_st = ''
        l_repe = ''
        if nom in self.links_repe:
            l_repe = 'link repetit'
        else:
            self.links_repe.append(nom)
        for fila in range(n):
            if 'Residencial' in ll_rs[fila] and 'Pessoas Idosas' in ll_rs[fila]:
                dos_resis += 1
                if test and not self.rapid:
                    print('Es vol sumar: {} + {} = {}'.format(self.capacitat, int(ll[0][fila]), self.capacitat+int(ll[0][fila])))
                    y = input('Tot correcte? (y or n)\n')
                    if y == 'n':
                        print(self.capacitat)
                        exit()
                self.utentes += int(ll[1][fila])
                self.capacitat += int(ll[0][fila])
                if dos_resis >= 2:
                    print(self.districte, 'Pag: {} '.format(pag)+nom, ll_rs[fila])
                    dos_resis_st = 'Dos resisi'
                    self.ll_2resis.append((self.districte, 'Pag: {} '.format(pag)+nom, ll_rs[fila]))
            ndf = pd.DataFrame({'Distrito':self.districte, 'Nombre':nom, 'Código Postal':cp, 'Entidad propietária':ep,\
                                    'Natureza Jurídica':nj, 'Respostas Sociais':ll_rs[fila], 'Capacidade':int(ll[0][fila]),\
                                    'Utentes':int(ll[1][fila]), 'Horário':ll[2][fila], 'Última Actualização':ll[3][fila],\
                                    'Entidade Gestora': eg, 'Natureza Jurídica(EG)': nj_eg, 'Links repes':l_repe, 'dos resis en un link':dos_resis_st}, index = [0])
            self.data_frame = self.data_frame.append(ndf)

                    
    def recorre_equipaments(self, pag, equiàmientos_r, test):
        for e in range(25):#loop equipaments
            sleep(0.3)
            links = self.driver.find_elements_by_class_name('pesq')
            links[e].click()
            nom = self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table/tbody/tr[1]/td/div').text
            if len(links) != 25 and pag != self.num_pagines-1:
                raise Exception('La llista de links es de {}, pag: {}, equipament: {}'.format(len(links), pag, nom))
            sleep(0.2)
            cp = self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table/tbody/tr[4]/td[2]').text # codi postal
            ep = self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table/tbody/tr[7]/td[2]').text # entitat propietaria
            nj = self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table/tbody/tr[8]/td[2]').text # naturaleza juridica
            respostas_sociais = [nom.text for nom in self.driver.find_elements_by_tag_name('i')]
            # Comprovu si hi ha entitat gestora
            try:
                t = self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table/tbody/tr[9]/td[1]').text
            except:
                t = ''
            eg = ''
            nj_eg = ''
            if t == 'Entidade Gestora:':
                eg = self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table/tbody/tr[9]/td[2]').text
                nj_eg = self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table/tbody/tr[10]/td[2]').text
            # S'omple el DataFrame
            self.ompla_DataFrame(nom, cp, ep, nj, respostas_sociais, self.get_llistes(len(respostas_sociais)), eg, nj_eg, test, pag)
            # Back a los equipos
            self.driver.find_element_by_xpath('//*[@id="rodape"]/table/tbody/tr/td[6]/a')\
                .click()
            self.equip += 1
            if self.equip == equiàmientos_r:
                break
        print('Pagina {} completada'.format(pag+1))
            
    def recorre_les_pagines(self,test=False):
        self.ll_resp_soc = []
        equiàmientos_r = int(self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table[1]/tbody/tr[3]/td[1]/b').text)
        self.equip = 0
        capacitat_t = int(self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table[1]/tbody/tr[3]/td[2]/b').text.replace(' ',''))
        self.capacitat = 0
        utentes_t = int(self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table[1]/tbody/tr[3]/td[3]/b').text.replace(' ',''))
        self.utentes = 0
        self.num_pagines = equiàmientos_r//25
        if equiàmientos_r%25 != 0:
            self.num_pagines += 1
        # loop per les PAGINES
        for pag in range(self.num_pagines):
            self.recorre_equipaments(pag, equiàmientos_r, test)
            if self.num_pagines >= 10:
                if pag <= 9:
                    self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table[2]/tbody/tr/td/div/table/tbody/tr/td[13]')\
                        .click()
                else:
                    self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table[2]/tbody/tr/td/div/table/tbody/tr/td[{}]'.format(self.num_pagines-10+3))\
                        .click()
            else:
                self.driver.find_element_by_xpath('//*[@id="corpo2as"]/table[2]/tbody/tr/td/div/table/tbody/tr/td[{}]'.format(self.num_pagines+3))\
                    .click()
        correct = True
        if self.equip != equiàmientos_r:
            raise Exception("El numero d'equips total no concorda amb els equips de la pagina ({} != {})".format(self.equips,equiàmientos_r))
        if self.capacitat != capacitat_t:
            print("La capacitat total no concorda amb la suma de capacitats de la pagina ({} != {})".format(self.capacitat,capacitat_t))
            correct = False
        if self.utentes != utentes_t:
            print("Els utentes total no concorda amb la suma dels utentes de la pagina ({} != {})".format(self.utentes,utentes_t))
            correct = False
        with open('resp_repetides.txt', mode='w') as f1:
            for elem in self.ll_2resis:
                line = ''
                for item in elem:
                    line += item+', '
                line = line[:-2]
                f1.write(line+'\n')
        if correct:
            print('Les dades concorden amb els resultats!')
        else:
            seguir = input('seguim amb el seguent districte? (y or n)\n')
            if seguir == 'n':
                exit()
            
    def get_excel(self, excel_name):
        print('Accedint als districtes')
        with pd.ExcelWriter("{}.xlsx".format(excel_name)) as writer:
            for i in range(2,20): # recorro els districtest
                # Selecciono el districte
                self.driver.find_element_by_xpath('//*[@id="cb_distrito"]/option[{}]'.format(i))\
                    .click()
                self.districte = self.driver.find_element_by_xpath('//*[@id="cb_distrito"]/option[{}]'.format(i)).text
                #Selecciono els parametres restants
                self.driver.find_element_by_xpath('//*[@id="cb_area"]/option[7]')\
                    .click()
                self.driver.find_element_by_xpath('//*[@id="cb_valencia"]/option[5]')\
                    .click()
                # Fa click sobre el buscador
                self.driver.find_element_by_xpath('//*[@id="pesq"]')\
                    .click()
                print('-'*30+' Districte actual: {} '.format(self.districte) + '-'*30)
                # Recorre les pagines
                self.recorre_les_pagines()
                # Escriu en el excel
                self.data_frame.to_excel(writer, index = False, sheet_name=self.districte)
                self.data_frame = pd.DataFrame({'Distrito':[], 'Nombre':[], 'Código Postal':[], 'Entidad propietária':[],\
                                        'Natureza Jurídica':[], 'Respostas Sociais':[], 'Capacidade':[],\
                                            'Utentes':[], 'Horário':[], 'Última Actualização':[],\
                                        'Entidade Gestora':[], 'Natureza Jurídica(EG)':[], 'Links repes':[], 'dos resis en un link':[]})
                self.torna_inici()
        self.driver.close()

                
miki = Miki()
##miki.comprova_capacitat('Faro', rapid=True)
miki.get_excel('Prova')











        
