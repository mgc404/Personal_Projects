'''
Popsar minim un palat de cada etiqueta cada setmana amb dos de verdura
Els estofats posarlos en cap de setmana com la carn d'olla.
En els segons plats, posar conill un cop al mes i en caps de setmana.
Els ous dos vegades per setmana
Dilluns verdura o llegums
'''

import random as r
#-----------------------------cosees a recordar--------------------------------------

seasons={'hivern':['gener','febrer','març'],'primavera':['abril','maig','juny'],'estiu':['juliol','agost','septembre'],'tardo':['octubre','novembre','desembre']}
llista_etiquetes_prim=['verdura','llegums','amanida','sopes','pasta','arros','estofat','altres']
llista_etiquetes_segon=['pollastre','vedella','peix','porc','conill','ous']

#-----------------------------Declaració de variables--------------------------------------

d={}#diccionari amb clau=nom_plat valor=[ingredients]
dicc_etiqueta_1rPlat={}
for etic in llista_etiquetes_prim:#creacio dicc_etiqueta_1rPlat
    dicc_etiqueta_1rPlat[etic]=[]
dicc_etiqueta_2nPlat={}
for etic in llista_etiquetes_segon:#creacio dicc_etiqueta_2nPlat
    dicc_etiqueta_2nPlat[etic]=[]
llista_primers_plats=[]
llista_segons_plats=[]

#-------------------------------------------------------------------------------------------
#                               lectura de fitxers
#--------------------------------------------------------------------------------------------

#----------------------------lectura primer plat----------------------------------------
with open('Primers_plats.txt','r') as f1:
    for line in f1: # Recorre el fitxer lina per linea
        line=line.strip('\n')
        if line[0]=='·':
            dicc_etiqueta_1rPlat[line[1:]].append(plat)
        elif line[0]!='-':# cas base = nom de la recepta
            plat=line[:-1]
            llista_primers_plats.append(plat)
            d[plat]=[]
        else:
            d[plat].append(line[1:])

#-----------------------------lectura segon plat--------------------------------------------
with open('Segons_plats.txt','r') as f1:
    for line in f1: # Recorre el fitxer lina per linea
        line=line.strip('\n')
        if line[0]=='·':
            dicc_etiqueta_2nPlat[line[1:]].append(plat)
        elif line[0]!='-':# cas base = nom de la recepta
            plat=line[:-1]
            llista_segons_plats.append(plat)
            d[plat]=[]
        else:
            d[plat].append(line[1:])

#--------------------------------------------------------------------------------------------
#                               modificació del fitxer menus
#--------------------------------------------------------------------------------------------

#-----------------------------estructura dels fitxer menus------------------------------------------
llista_1&2_plats=[]
llista_dies_set=['Dilluns','Dimarts','Dimecres','Dijous','Divendres','Dissabte','Diumenge']
with open('menus.txt','w') as f2:
    linia=''
    #creacio de la primera linia amb els dies
    for i in range (7):#iteracio per els dies de la setmana
        n=22-len(llista_dies_set[i])
        linia=linia+'    '+llista_dies_set[i]+' '*n
    f2.write(linia)
    f2.write('\n')
    #estructura de l'organitzacio del mes
    total=26
    f=0
    t=0
    for e in range(4):#iteracio per a les 4 SETMANES del mes amb 1r i 2n
        llista_1Plats=[]
        llista_2Plats=[]
        for dia in range(7): # iteracio per a cada dia de la setmana
            if dia ==0:
                llista_1Plats.append(dicc_etiqueta_1rPlat['verdura'].pop(dicc_etiqueta_1rPlat['verdura'].index(r.choice(dicc_etiqueta_1rPlat['verdura']))))
                llista_2Plats.append(llista_segons_plats.pop(llista_segons_plats.index(r.choice(llista_segons_plats))))
                

                
















