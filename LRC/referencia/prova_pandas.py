import pandas as pd

a = pd.DataFrame({'Respostes Sociais':[],'l':[]})
ll = ['cata','tarra','girona']
for n in ll:
    for i in range(5):
        p = pd.DataFrame({'Respostes Sociais':[i],'l':[i]})
        print(p)
        a = a.append(p)
    with pd.ExcelWriter("Libro1.xlsx") as writer:
        a.to_excel(writer, index = False, sheet_name=n)
    a = pd.DataFrame({'Respostes Sociais':[],'l':[]})
print(a)
