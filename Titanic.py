import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("titanic_train.csv")
avg1=round(df[df["Pclass"]==1]['Age'].mean())
avg2=round(df[df["Pclass"]==2]['Age'].mean())
avg3=round(df[df["Pclass"]==3]['Age'].mean())

df.fillna(0,inplace=True)

set1=df[df['Pclass']==1]
set1['Age']=df['Age'].replace(0,avg2)

set2=df[df['Pclass']==2]
set2['Age']=df['Age'].replace(0,avg2)

set3=df[df['Pclass']==3]
set3['Age']=df['Age'].replace(0,avg3)

c=set1.combine_first(set2)
final=c.combine_first(set3)