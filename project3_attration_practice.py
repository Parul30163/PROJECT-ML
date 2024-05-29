import numpy  as np
import pandas as pd

df=pd.read_csv("D:\\regex2024\\ml exp\Attrition - Attrition.csv")

df.head()

df.isnull().sum()

df.describe()

from sklearn.preprocessing import LabelEncoder

lb=LabelEncoder()

df['Attrition']=lb.fit_transform(df['Attrition'])
df['BusinessTravel']=lb.fit_transform(df['BusinessTravel'])
df['Department']=lb.fit_transform(df['Department'])
df['EducationField']=lb.fit_transform(df['EducationField'])
df['Gender']=lb.fit_transform(df['Gender'])
df['JobRole']=lb.fit_transform(df['JobRole'])
df['MaritalStatus']=lb.fit_transform(df['MaritalStatus'])
df['Over18']=lb.fit_transform(df['Over18'])
df['OverTime']=lb.fit_transform(df['OverTime'])

df.sample(5)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()



df_sc=sc.fit_transform(df)

df_new =pd.DataFrame(df_sc,columns=df.columns)

np.round(df.describe(),1)

x= df.drop(columns=['Attrition'],axis=1)#independent
y=df['Attrition']#target

print(x.shape)
print(y.shape)

from sklearn. model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

np.round(x_train.describe(),2)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

x_train_sc=sc.fit_transform(x_train) 

x_train_new=pd.DataFrame(x_train_sc,columns=x_train.columns)

x_train_new.head(3)

np.round(x_train_new.describe(),3)

from sklearn.preprocessing import MinMaxScaler

mn=MinMaxScaler()

x_train_mn=mn.fit_transform(x_train)

x_train_new=pd.DataFrame(x_train_mn,columns=x_train.columns)

np.round(x_train.describe(),1)

np.round(x_train_new.describe(),1)



