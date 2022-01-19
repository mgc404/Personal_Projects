import random as r
# el 2 i el 25 non poden estar junts
# el 15 i el 19
# el
llista_opcions=[]
def grups_classe(num_nens,k):
    global llista_opcions
    num_nens=num_nens+num_nens%4
    llista_grups=[]
    llnens=[]
    for i in range(num_nens):
        llnens.append(i)
    n=0
    while n<=k:
        r.shuffle(llnens)
        p=0
        for i in range(num_nens//4):
            llista_grups.append(llnens[p:p+4])
            p+=4
        llista_opcions.append(llista_grups)
        llista_grups=[]
        n+=1

def opcio(o):
    global llista_opcions
    if o>=len(llista_opcions) or o==0:
        x = input(
            """Mare vols una opció que no li has fet calcular!\n
Has de posar un numero que sigui mes petit del numero d'opcions que has posat avans.
Pero tranquila totom es pot equivocar, no cal que repeteixis un altre cop tot, simplement
prem un numero que sigui més petit que el numero d'opcions i donali al ENTER

Opcio vàlida: 
""")
        
    for i in llista_opcions[o-1]:
        print(i)
