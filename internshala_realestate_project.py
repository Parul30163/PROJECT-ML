import pandas as pd


it=pd.read_csv("is2.csv")

it

it.dtypes

it.head(10)

it.tail(10)

# what is descriptive statics
##count of value
##mean 
##sd
#min
#max
#3 %-1st,2nd ,3rd

it.describe()

it.describe(include='all')

it.info()

it['Sale Price'].mean()

it['Sale Price'].min()

it['Sale Price'].max()

it['Sale Price'].std()

it['Sale Price'].quantile(.25) #for percentile

it['Condition of the House'].unique()

import numpy as np

np.std(it['Sale Price'])

it['Sale Price'].std()-np.std(it['Sale Price'])

np.std(it['Sale Price'],ddof=1)

it['Sale Price'].std()

dir(np)

# PLotting Graph

import matplotlib.pyplot as plt

plt.plot(it['Sale Price'])


plt.plot(it['Sale Price'], color ='green')
plt.xlabel("Record Numberrr")
plt.ylabel("Sale Pricree")
plt.title("my first graph")
plt.show()


plt.plot(it['Sale Price'],marker='o',markerfacecolor='Blue',markersize=5,color ='green',linewidth=5,linestyle='dashed')

it.groupby('Condition of the House')['ID'].count()

# PIE CHART

values=(500,1701,14031,5679,1172)

labels=('Bad','Excellent','Fair','Good','Okay')

plt.pie(values,labels=labels)

# Bar Graph

plt.bar(labels,values,color='green')

plt.bar(labels,values,color='green',linewidth=5,linestyle='dashed')
plt.xlabel("Record Numberrr")
plt.ylabel("Sale Pricree")
plt.title("my first graph")
plt.show()

it['Condition of the House'].value_counts().plot(kind='bar')# regex

# Scatter plot

import matplotlib.pyplot as plt


plt.scatter(x=it['Flat Area (in Sqft)'],y=it['Sale Price'],color='red')
plt.xlabel("Area")
plt.ylabel('selling prive')
plt.title("selling privr vs area")

plt.show()

plt.scatter(x= it['No of Bathrooms'],y =it['Sale Price'],color='red')
plt.xlabel("No of bathroms")
plt.ylabel('selling prive')
plt.title("selling privr vs no of bathrooms")

plt.show()





plt.scatter(x= it['Age of House (in Years)'],y =it['Sale Price'],color='red')
plt.xlabel("Age of House (in Years)")
plt.ylabel('selling prive')
plt.title("selling privr vs Age of House (in Years)")

plt.show()

it.describe()

# Histogram

plt.hist(it['Age of House (in Years)'],bins=10)
plt.xlabel("Age of House (in Years)")
plt.ylabel('no of records')
plt.title("Age distribution of houses")

plt.show()

plt.hist(it['Age of House (in Years)'],bins=10)

plt.boxplot(it['Age of House (in Years)'])

# Part2

it['Sale Price'].mean()

 #initialising a new column 
it['condition_sale']=0

# calculate mean based on the condition of the house
for i in it['Condition of the House'].unique():
    
    it['condition_sale'][it['Condition of the House'] == str(i)] = it['Sale Price'][it['Condition of the House'] == str(i)].mean()

#potting the mean sales based on the condition of the house
plt.figure(dpi=100)
plt.bar(it['Condition of the House'].unique(),it['condition_sale'].unique())

plt.xlabel("Condition of the House")
plt.ylabel(' Mean sale of price ')

plt.show()



#initialising a new column 
it['zip_condition_sale']=0

C='Condition of the House'
Z='Zipcode'

#calculating mean based on the condition of the House  and Zipcode
for i in it[C].unique():
    for j in it[Z].unique():
        it['zip_condition_sale'][(it[C]==str(i))&(it[Z]==j)]= it['Sale Prce'][it[C]==str(i)&(it[Z]==j)].mean()

