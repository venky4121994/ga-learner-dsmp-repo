# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
data.hist(['Rating'])
data = data[data['Rating']<=5]
data.hist(['Rating'])
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())
missing_data = pd.concat([total_null,percent_null],keys=['Total','Percent'],axis=1)
print(missing_data)

data.dropna(inplace=True)

total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())
missing_data_1 = pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis=1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here
plt.figure(figsize=(10,20))
catplot = sns.catplot(x = "Category", y = "Rating", data=data, kind="box",height=10)
catplot.set_xticklabels(rotation=90)
plt.title('Rating vs Category [BoxPlot]',size = 20)
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'])
data['Installs'] = data['Installs'].str.replace('+','')
data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].astype('int32')
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
graph = sns.regplot(data['Installs'],data['Rating'],data=data)
graph.set_title('Rating vs Installs [Boxplot]')
plt.show()
#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts())
data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype('float32')
graph2 = sns.regplot(data['Price'],data['Rating'],data=data)
graph2.set_title('Rating vs Price [RegPlot]')
#Code ends here


# --------------

#Code starts here
print(len(data['Genres'].unique()), "genres")
data['Genres'] = data['Genres'].str.split(';').str[0]
gr_mean = data[['Genres','Rating']].groupby(['Genres'],as_index=False).mean()
print(gr_mean.describe())
gr_mean=gr_mean.sort_values('Rating')
print(gr_mean.head(1))
print(gr_mean.head(1))

#Code ends here


# --------------

#Code starts here
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated']).dt.days
plt.figure(figsize = (10,10))
sns.regplot(x="Last Updated Days", y="Rating",color='lightpink',data=data)
plt.title('Rating vs Last Updated [Regplot]',size =20)
#Code ends here


