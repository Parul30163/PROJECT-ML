import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv('"D:\\regex2024\internshala ml\\1. Regression - Module - (Housing Prices).csv"')
data.head()
data['Zipcode'].unique()
data['Sale Price'].mean()
#Initialising a new column
data['condition_sale'] = 0

# Calculating mean based on the condition of the House
for i in data['Condition of the House'].unique():
  data['condition_sale'][data['Condition of the House'] == str(i)] = data['Sale Price'][data['Condition of the House'] == str(i)].mean()

data['condition_sale'].unique()
import time
#Initialising a new column
data['zip_condition_sale'] = 0

C = 'Condition of the House'
Z = "Zipcode"

tick = time.time()
# Calculating mean based on the condition of the House and zipcode
for i in data[C].unique():
  for j in data[Z].unique() :
    data['zip_condition_sale'][(data[C] == str(i)) & (data[Z] == j) ] = data['Sale Price'][(data[C] == str(i)) & (data[Z] == j)].mean()
tock = time.time()
time1 = tock - tick
len(data['zip_condition_sale'].unique())
zip_condition_sale2  = pd.pivot_table(data, index=["Condition of the House","Zipcode"], values=["Sale Price"], aggfunc=np.mean,)
zip_condition_sale2
zip_condition_sale3  = pd.pivot_table(data, index=["Zipcode"], columns = ['Condition of the House'], values=["Sale Price"], aggfunc=np.mean)
zip_condition_sale3
data['plot_length'] = data['Flat Area (in Sqft)']**0.5
data['plot_length'].head()
data['new_rank'] = data['Overall Grade']/data['Overall Grade'].sum()
data['total_area'] = data['Flat Area (in Sqft)'] + data['Lot Area (in Sqft)']
data['total_area'].head()
data['Condition of the House'][data['Condition of the House'] == 'Fair'] = '1'
data['Condition of the House'][data['Condition of the House'] == 'Okay'] = '0'
data['Condition of the House'][data['Condition of the House'] == 'Bad'] = '0'
data['Condition of the House'][data['Condition of the House'] == 'Good'] = '1'
data['Condition of the House'][data['Condition of the House'] == 'Excellent'] = '3'
data['Condition of the House'].unique()
data['Condition of the House'] = data['Condition of the House'].map({'Good':'1',
                                                                     'Excellent':'3',
                                                                     'Bad':'0',
                                                                     'Fair': '1',
                                                                     'Okay': '0'})
data['Condition of the House'].unique()
data['Date House was Sold'].head()
year = []
for i in range(len(data['Date House was Sold'])):
  k = data['Date House was Sold'][i].split()[-1]
  year.append(k)

data['year_sold'] = year
data['year_sold'].head()
def year(value):
  return value.split()[-1]

data['year_sold'] = data['Date House was Sold'].map(year)
data['year_sold'].head()
#### Ignore THIS CELL ####

tick = time.time()
year = []
for i in range(len(data['Date House was Sold'])):
  k = data['Date House was Sold'][i].split()[-1]
  year.append(k)

data['year_sold'] = year
tock = time.time()
time1 = tock-tick

tick = time.time()
def year(value):
  return value.split()[-1]

data['year_sold'] = data['Date House was Sold'].map(year)
tock = time.time()
time2 = tock-tick
time1/time2
data.head()
data['total_rooms'] = (data['No of Bedrooms'] + data['No of Bathrooms']) * data['No of Floors']
data['total_rooms'].head()
def Room(row):
  return (row[0] + row[1]) * row[2]

data['total_rooms'] = data[['No of Bedrooms','No of Bathrooms','No of Floors']].apply(Room , axis = 1)
data['total_rooms'].head()
data[['No of Bedrooms','No of Bathrooms','No of Floors']]
#### Ignore THIS CELL ####
tick = time.time()
data['total_rooms'] = (data['No of Bedrooms'] + data['No of Bathrooms']) * data['No of Floors']
tock = time.time()
time1 = tock-tick
#### IGNORE THIS CELL ####
tick = time.time()
def Room(row):
  return (row[0] + row[1]) * row[2]

data['total_rooms'] = data[['No of Bedrooms','No of Bathrooms','No of Floors']].apply(Room , axis = 1)
tock = time.time()
time2 = tock-tick
time1/time2
data.describe()
data.head()
data['luxury_home'] = 0

for i in range(len(data)):
  count = 0
  if data['Waterfront View'][i] == 'Yes':
    count = count+1
  if data['Condition of the House'][i] in ['Good','Excellent']:
    count = count+1    
  if data['Overall Grade'][i] >= 8:
    count = count+1
  if count >= 2:
    data['luxury_home'][i] = 'Yes'
  else:
    data['luxury_home'][i] = 'No'
    
data['luxury_home'].unique()
def luxury_home(row):
  count = 0
  if row[0] =='Yes':
    count = count+1
  if row[1] in ['Good', 'Excellent']:
    count = count+1
  if row[2] >= 8:
    count = count+1  
  if count >= 2:
    return 'Yes'
  else:
    return "No"
  
data['luxury_home'] = data[['Waterfront View','Condition of the House','Overall Grade']].apply(luxury_home, axis = 1)

data['luxury_home'].unique()
luxury_home(['Yes','Good', 5])
