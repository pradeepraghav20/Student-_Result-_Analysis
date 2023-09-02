import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:\Users\prade\OneDrive\Desktop\pandas_project\stu_res_ana\Expanded_data_with_more_features.csv')

# print(df.head(20))
# print(df.describe())
# print(df.info())
# print (df.isnull().sum())

df=df.drop('Unnamed: 0',axis=1)
print(df)

# chage the weekly hours

df['WklyStudyHours']=df['WklyStudyHours'].str.replace('< 5','5 - 10')
print(df)

plt.figure(figsize=(5,5))
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.show()


# gb=df.groupby('ParentEduc').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})
print(gb)

plt.figure(figsize=(5,5))
sns.heatmap(gb,annot=True)
plt.show()

gb2=df.groupby('ParentMaritalStatus').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})
print(gb2)

print(df['EthnicGroup'].unique())

gropupA=df.loc[(df['EthnicGroup']=='group A')].count()
gropupB=df.loc[(df['EthnicGroup']=='group B')].count()
gropupC=df.loc[(df['EthnicGroup']=='group C')].count()
gropupD=df.loc[(df['EthnicGroup']=='group D')].count()
gropupE=df.loc[(df['EthnicGroup']=='group E')].count()


mlist=[gropupA['EthnicGroup'],  gropupB['EthnicGroup'] ,gropupC['EthnicGroup'] ,gropupD['EthnicGroup']  ]


plt.pie(mlist,autopct="%1.2f %%")
plt.show()

