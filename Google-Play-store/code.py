# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
data['Rating'].hist()
data = data[data['Rating']<=5]
data['Rating'].hist()
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())*100
missing_data = pd.concat([total_null,percent_null],keys=['Total','Percent'],axis=1)
#print(missing_data)
data = data.dropna()
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())*100
missing_data_1 = pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis=1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here
g=sns.catplot(x="Category",y="Rating",data=data,kind="box",height=10)
g.set_xticklabels(rotation=90)
g.fig.suptitle("Rating vs Category [BoxPlot]")
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

#Removing `,` from the column
data['Installs']=data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs']=data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installs[RegPlot]',size = 20)

#Code ends here



# --------------
#Code starts here
data['Price']=data['Price'].str.replace('$','')

#Converting the column to `float` datatype
data['Price'] = data['Price'].astype(float)

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Price", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Price [RegPlot]',size = 20)

#Code ends here





# --------------

#Code starts here
#print(data['Genres'])
#data['Genres'].unique()
data['Genres'] = data['Genres'].str.split(';').str[0]
cols = ['Genres']
gr_mean =data.groupby(cols, as_index = False).mean() 
print(gr_mean.describe())
gr_mean = gr_mean.sort_values(by=['Rating'])
print(gr_mean.head(1))
print(gr_mean.tail(1))
#Code ends here


# --------------

#Code starts here
data['Last Updated'] = data['Last Updated'].astype('datetime64[ns]') 
max_date = max(data['Last Updated'])
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
plt.figure(figsize = (10,10))
#Plotting Regression plot between Rating and Installs
sns.regplot(x="Last Updated Days", y="Rating", color = 'teal',data=data)
#Setting the title of the plot
plt.title('Rating vs Last Updated [RegPlot]',size = 20)


#Code ends here


