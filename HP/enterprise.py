import pandas as pd
df = pd.read_csv("enterprise.csv",parse_dates=['Cutoff'])
dfn = pd.read_csv("inventory.csv",)
dfnn=pd.read_csv('week.csv')

def backlog(df):
    gb=df.groupby('ModelName')
    total= gb['GoodsIssueQuantityEA'].sum()
    return total

def inventory(dfn):
    grouped = dfn.groupby(['MODEL_NM'])
    res = grouped['UNRESTRICTED_QT'].sum()
    res_df = pd.DataFrame({'MODEL_NM':res.index, 'UNRESTRICTED_QT':res.values})
    return print(res_df)



def fun1(df,dfn):
    gb=df.groupby('ModelName')
    df1= gb['GoodsIssueQuantityEA'].sum()
    gbn=dfn.groupby('MODEL_NM')
    dfn1= gbn['UNRESTRICTED_QT'].sum()
    a = pd.concat([df1, dfn1], axis=1)
    aa=a['UNRESTRICTED_QT']-a['GoodsIssueQuantityEA']
    newl=[]
    for aaa in aa.keys():
        if aa[aaa]<0:
            newl.append(aaa)
    return newl
        
def fun(df,dfn):
    gb=df.groupby('ModelName')
##    print(gb['Cutoff'].min())
    df2=df[['ModelName','Cutoff']]
    df1= gb['GoodsIssueQuantityEA'].sum()
    dt = gb['Cutoff'].max()
##    print(dt)
##    print('espai')
##    print(df1)
    gbn=dfn.groupby('MODEL_NM')
    dfn1= gbn['UNRESTRICTED_QT'].sum()
    a = pd.concat([df1, dfn1], axis=1)
    aa=a['UNRESTRICTED_QT']-a['GoodsIssueQuantityEA']
    newl=[]
    for aaa in aa.keys():
        if aa[aaa]<0:
            newl.append((aaa, dt[aaa]))
##    for i in range(len(df2)):
##        print(df2.loc[i]['Cutoff'],df2.loc[i]['ModelName'])
    return newl


fun(df,dfn)       
        
        
    
    
