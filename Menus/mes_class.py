
from menus_class import *
from DATA import *
import random as r
llista_etiquetes_prim=['sopes','pasta','arros','estofat']
    
class Mes:
    
    def __init__(self, ll_1, ll_2):
        self.ll_1 = ll_1
        self.ll_2 = ll_2
        self.dic_menjar_1 = diccionari_tipos_llista(ll_1)
        self.dic_menjar_2 = diccionari_tipos_llista(ll_2)
        self.setmanes = []
        self.setmana = 0
        self.llista = [] # TO DO 
        
    def crea_mes(self):
        for mes in range(3):
            for setmana in range(4):
                primers_plats=[]
                for i in range(7): # i = dia
                    if i == 0 or i == 3: #Dilluns i dijous
                        if len(self.dic_menjar_1['verdura']) == 0:
                            self.dic_menjar_1['verdura'] = llista_tipus_plats(self.ll_1,'verdura')
                        plat = self.dic_menjar_1['verdura'][0] # seleccio del numero de la llista
                        self.dic_menjar_1['verdura'].remove(plat)# seleccionar i eliminar el plat de la llista d'opcions
                        primers_plats.append(plat)
                    elif i == 1: #Dimarts
                        if len(self.dic_menjar_1['llegums']) == 0:
                            self.dic_menjar_1['llegums'] = llista_tipus_plats(self.ll_1,'llegums')
                        plat = r.choice(self.dic_menjar_1['llegums']) # seleccio del numero de la llista
                        self.dic_menjar_1['llegums'].remove(plat)# seleccionar i eliminar el plat de la llista d'opcions
                        primers_plats.append(plat)
                    elif i == 6: # Diumenge
                        if len(self.dic_menjar_1['altres']) == 0:
                            self.dic_menjar_1['altres'] = llista_tipus_plats(self.ll_1,'altres')
                        plat = r.choice(self.dic_menjar_1['altres'])# seleccio del numero de la llista
                        self.dic_menjar_1['altres'].remove(plat)# seleccionar i eliminar el plat de la llista d'opcions
                        primers_plats.append(plat)
                    else: # Dimecres, Divendres, Diss
                        t = r.choice(llista_etiquetes_prim) # seleccio de tipus de plat
                        if len(self.dic_menjar_1[t]) == 0:
                            self.dic_menjar_1[t] = llista_tipus_plats(self.ll_1,t)
                        plat = r.choice(self.dic_menjar_1[t]) # seleccio del numero de la llista
                        self.dic_menjar_1[t].remove(plat)# seleccionar i eliminar el plat de la llista d'opcions
                        primers_plats.append(plat)
                self.setmanes.append(primers_plats)
                print(self.setmanes[setmana])
                print('\n')
