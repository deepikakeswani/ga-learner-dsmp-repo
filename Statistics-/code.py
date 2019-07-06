# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#print(data.head(10))
#Code starts here 

#print(data['Gender'])
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot.bar()
plt.show()


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot.pie()
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
#print(data.columns)
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df['Combat'].cov(sc_df['Strength'])
#print(sc_covariance)
sc_strength = sc_df['Strength'].std()
#print('sc_strength',sc_strength)
sc_combat = sc_df['Combat'].std()
#print(sc_combat)
sc_pearson = sc_covariance/(sc_strength * sc_combat)
#print(sc_pearson)
ic_df = data[['Combat','Intelligence']]
ic_covariance = ic_df['Combat'].cov(ic_df['Intelligence'])
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance /(ic_intelligence * ic_combat)
print('Pearson''s correlation of Strength and Combat is', sc_pearson)
print('Pearson''s correlation of Intelligence and Combat is', ic_pearson)




# --------------
#Code starts here
total_high = float(data.Total.quantile([0.99]))
print(total_high)
super_best = data[data['Total'] > total_high]
#print(super_best)
super_best_names = list(super_best['Name'])
print(super_best_names)
# Code ends here



# --------------
#Code starts here
fig,(ax_1, ax_2 , ax_3) = plt.subplots(1, 3)
data.boxplot(column=['Intelligence'])
ax_1.set_title('Intelligence')
data.boxplot(column=['Speed'])
ax_2.set_title('Speed')
data.boxplot(column=['Power'])
ax_3.set_title('Power')
plt.show()



