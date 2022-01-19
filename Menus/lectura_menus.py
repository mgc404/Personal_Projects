from menus_class import *
from mes_class import *
from DATA import diccionari_tipos_llista
import random as r

#-----------------------------cosees a recordar--------------------------------------

seasons={'hivern':['gener','febrer','març'],'primavera':['abril','maig','juny'],'estiu':['juliol','agost','septembre'],'tardo':['octubre','novembre','desembre']}
llista_etiquetes_prim=['verdura','llegums','sopes','pasta','arros','estofat','altres']
llista_etiquetes_segon=['pollastre','vedella','peix','porc','conill','ous']

#-------------------------------------------------------------------------------------------
#                               lectura de fitxers
#--------------------------------------------------------------------------------------------

#----------------------------lectura primer plat----------------------------------------
llista_primers_plats = []
with open('Primers_plats.txt','r') as f1:
    for line in f1: # Recorre el fitxer lina per linea
        line=line.strip('\n')
        if line[0]=='·':# cas d'etiquetas
            n+=1
            if n==1:
                plat.tipus=line[1:]
            elif n==2:
                plat.temps=line[1:]
            else:
                plat.estacio.append(line[1:])
        elif line[0]!='-':# cas base = nom de la recepta
            nom_plat=line[:-1]
            plat=Recepta(nom_plat)
            llista_primers_plats.append(plat)
            n=0
        else: # cas ingredients
            plat.ingredients.append(line[1:])
diccionari_llista_tipus_1r = diccionari_tipos_llista(llista_primers_plats) #base dades 1r plat

#-----------------------------lectura segon plat--------------------------------------------
llista_segons_plats = []
with open('Segons_plats.txt','r') as f1:
    for line in f1: # Recorre el fitxer lina per linea
        line=line.strip('\n')
        if line[0]=='·':# cas d'etiquetas
            n+=1
            if n==1:
                plat.tipus=line[1:]
            elif n==2:
                plat.temps=line[1:]
            else:
                plat.estacio.append(line[1:])
        elif line[0]!='-':# cas base = nom de la recepta
            nom_plat=line[:-1]
            plat=Recepta(nom_plat)
            llista_segons_plats.append(plat)
            n=0
        else: # cas ingredients
            plat.ingredients.append(line[1:])
diccionari_llista_tipus_2r = diccionari_tipos_llista(llista_segons_plats) #base dades 1r plat

mes = Mes(llista_primers_plats, llista_segons_plats)
mes.crea_mes()
