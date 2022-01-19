class Polinomi:

   def __init__(self):
      """
      Crea un polinomi amb tots els coeficients nuls
      """
      self.__coefs = {}


   def __setitem__(self, i, v):
      """
      Assigna v al coeficient de grau i del polinomi.
      """
      if v == 0:
         if i in self.__coefs:
            self.__coefs.pop(i)
      else:
         self.__coefs[i] = v
      

   def __getitem__(self, i):
      """
      Retorna el coeficient de grau i del polinomi.
      """
      return self.__coefs.get(i, 0)
      

   def grau(self):
      """
      Retorna el grau del polinomi; zero si és el polinomi nul.
      """
      if len(self.__coefs) == 0:
         g = 0
      else:
         g = max(self.__coefs.keys())
      return g

   def __add__(self, p):
      """Suma de polinomis"""
      return suma_polinomis(self, p)

   def __mul__(self, p):
      """Producte de polinomis"""
      return producte_polinomis(self, p)

   def __str__(self):
      """
      Retorna un string corresponent a la representació del 
      polinomi on la variable es representa pel caràcter 'x'.
      """ 
      s = ''
      for i in range(0,self.grau()+1):
         ai = self[i]
         if ai!=0:
            if ai>0.0:
               sgn = '+'
            else:
               sgn = ''
            if i==0:
               pot =''
            elif i==1:
               pot = 'x'
            else:
               pot = 'x'+'^'+str(i)
            coef = str(ai)
            if i>0:
               if ai==1:
                  coef = ''
               elif ai==-1:
                  coef = '-'
            s = sgn + coef + pot + s
      if s=='':
         s = '0'
      if s.startswith('+'):
         s = s[1:]
      return s


def suma_polinomis(pol1, pol2):
   g1 = pol1.grau()
   g2 = pol2.grau()
   gsuma = max(g1, g2)
   suma = Polinomi()
   for g in range(gsuma + 1):
      suma[g] = pol1[g] + pol2[g]
   return suma


def producte_polinomis(pol1, pol2):
   prod = Polinomi()
   for g1 in range(pol1.grau() + 1):
      for g2 in range(pol2.grau() + 1):
         prod[g1 + g2] += pol1[g1] * pol2[g2]
   return prod
