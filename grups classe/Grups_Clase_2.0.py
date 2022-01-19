import random as r
llista_opcions=[]
def grups_classe(num_nens,k):
    global llista_opcions
    num_nens=num_nens+num_nens%4
    llista_grups=[]
    llnens=[]
    for i in range(num_nens):
        llnens.append(i)
    n=0
    while n<k:
        r.shuffle(llnens)
        p=0
        for i in range((num_nens//4)):
            llista_grups.append(llnens[p:p+4])
            p+=4
        llista_opcions.append(llista_grups)
        llista_grups=[]
        n+=1
def opció(o):
    global llista_opcions
    for i in llista_opcions[o-1]:
        print(i)
    print('')
run=True
print(
    '''
Benvinguda al programa per fer grups de clase.
Siusplau segueixi les instruccions que apareixen en pantalla.
Per a sortir del programa en qualssevol instant premi la creueta o escrigui la lletra 'q' mes enter.''')
num_nens=input(
    '''
Siusplau introdueixi el numero de nens de la clase.
Numero de nens: ''')
num_opcions=input(
    '''
Siusplau introdueixi el numero d'opcions que vol consular.
Cada opció li donara una distribució diferent dels alumnes en els diferents grups 
Numero d'opcions a calcular: ''')
grups_classe(int(num_nens),int(num_opcions))
print(
    '''
Escrigui l'operació que desitgi realitzar.
    -Si vol crear una distribucio nova d'alumnes escrigui: 'nova classe'.
    -Si vol consultar un dels grups ja creats introdueixi el numero de l'opcio desitjada.
    ''')
while run:
    order=input('Esperant ordre: ')
    if order=='q':
        run=False
    elif order=='nova classe':
        num_nens=input(
    '''
Siusplau introdueixi el numero de nens de la clase.
Numero de nens: ''')
        num_nens=num_nens+num_nens%4
        num_opcions=input(
    '''
siusplau introdueixi el numero d'opcions que vol consular.
Cada opció li donara una distribució diferent dels alumnes en els diferents grups 
Numero d'opcions a calcular: ''')
        llista_grups=[]
        llnens=[]
        #Es crea la llista amb el numero de la llista de cada nen.
        for i in range(num_nens):
            llnens.append(i)
        n=0
        while n<=int(num_opcions):
            r.shuffle(llnens)
            p=0
            for i in range((num_nens//4)):
                llista_grups.append(llnens[p:p+4])
                p+=4
            llista_opcions.append(llista_grups)
            llista_grups=[]
            n+=1
    elif order.isdigit():
        opció(int(order))

        
quit
        
        
    
    
