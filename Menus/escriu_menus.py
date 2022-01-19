from mes_class import *
from lectura_menus import *

llista_dies_set=['Dilluns','Dimarts','Dimecres','Dijous','Divendres','Dissabte','Diumenge']
with open('menus.txt','w') as f2:
    linia='    '
    #creacio de la primera linia amb els dies
    for i in range (7):#iteracio per els dies de la setmana
        n=28-len(llista_dies_set[i])
        linia=linia+llista_dies_set[i]+' '*n
    f2.write(linia)
    f2.write('\n')

    # utlilitzar els atributs .setmanes per accedir als menus de cada mes
    for setmana in mes.setmanes:
        linia = ''
        for apat in setmana:
            n=28-len(apat)
            linia=linia+'1r '+apat+' '*n
        f2.write(linia+'\n')
        f2.write('2n                             '*7+'\n')
        f2.write('\n')
        
            
        
        
