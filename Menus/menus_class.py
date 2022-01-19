
class Recepta(str):
    def __init__(self, nom_recepta):
        self.nom = nom_recepta
        self.ingredients = []
        self.tipus = ''
        self.temps = 0
        self.estacio = []
        
    def __print__(self):
        return self.nom
    

