def llista_tipus_plats(llista_receptes,tipus_de_plat):
    # Retorna una llista de plats del tipus escollit amb la llista de primers plats inicials
    ll=[]
    for i in llista_receptes:
        if i.tipus==tipus_de_plat:
            ll.append(i)
    return ll

def diccionari_tipos_llista(llista_receptes):
    dic={}
    llista_etiquetes_prim=['verdura','llegums','sopes','pasta','arros','estofat','altres']
    for tipus in llista_etiquetes_prim:
        dic[tipus] = llista_tipus_plats(llista_receptes,tipus)
    return dic
def escollir_plat_especific(llista_plats,plats_set_anterior,especificacio):
    # Escull un plat aleatoriament que no hagi sortit a la setmana pasada que no sigui
    # ni verdura ni 
    trobat = False
    iteracions = 0
    while not trobat:
        pass
    
        
        
