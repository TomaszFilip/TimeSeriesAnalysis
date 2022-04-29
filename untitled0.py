# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:21:16 2022

@author: Tomasz Filip
"""

import numpy as np 
import pandas as pd

labels=['a','b','c']

mylist=[10,20,30]
arr=np.array(mylist)

arr

d={'a':10,'b':20,'c':30}

pd.Series(mylist)
pd.Series(data=mylist)
pd.Series(arr)
pd.Series(arr,labels)
pd.Series(d)
ser1=pd.Series(data=[1,2,3,4], index=['USA','Ger','GB','Japan'])
ser1['Japan']
ser1[3]
ser2=pd.Series(data=[1,2,3,4], index=['USA','Ger','Italy','Japan'])
ser=ser1+ser2


np.random.seed(101)
rand_mat=np.random.randn(5,4)
rand_mat

df=pd.DataFrame(data=rand_mat, index='A B C D E'.split(),columns='W X Y Z'.split())
dfOriginal=df.copy()

df['W']
type(df['W'])
type(df)
df[['W','X']]
df['NEW']=df['W']+df['X']

df1=df.drop('NEW', axis=1)
df.drop('NEW',axis=1,inplace=True)

df.drop('A', axis=0)
df.loc['A']
df.iloc[0,2]
df.loc[['A','B']][['W','X']]

df.iloc[[0,1],[0,1]]
df.iloc[0:2,0:2]

cond1=df['W']>0
cond2=df['Y']>1
df[cond1&cond2]

df.reset_index(inplace=True)
df.drop('index',axis=1,inplace=True)
df['States']='CA NY WY OR CO'.split()
df.set_index('States', inplace=True)

df.info()
df.describe()

#NaNs
df=pd.DataFrame({'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]})
df
df.dropna()
df.dropna(axis=1)
#df.dropna(tresh=2) #something wrong?
df.fillna('FILL VALUE')
df.fillna(0)
df.fillna(df.mean())

data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Person':['Sam','Charlie','Amy','Eve','Carl','Sarah'],'Sales':[200,120,340,243,350,344]}
df=pd.DataFrame(data)
df.groupby('Company').mean()
df.groupby('Company').describe().transpose()

df=pd.DataFrame({'col1':[1,2,3,4], 'col2':[444,555,666,444], 'col3':['abs','def','ghi','xyz']})
df['col2'].nunique()
df['col2'].unique()

df['col2'].value_counts()

def times_two(number):
    return 2*number

times_two(4)

df['new']=df['col1'].apply(times_two)
df.sort_values('col2', ascending=False)






