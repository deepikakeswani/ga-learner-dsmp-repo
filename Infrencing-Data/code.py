# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data = pd.read_csv(path)
data_sample = data.sample(n=sample_size,random_state=0)
sample_mean = data_sample["installment"].mean()
sample_std = data_sample["installment"].std()
margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))
print("Margin of error is ",margin_of_error)
# finding the confidence interval
confidence_interval =[sample_mean-margin_of_error,sample_mean+margin_of_error]
print("Confidence interval is ",confidence_interval)
# finding the true mean
true_mean = data["installment"].mean()
print("True mean is ", true_mean)
if (true_mean >= confidence_interval[0]) & (true_mean < confidence_interval[1]):
    print("True mean falls in range of confidence interval")
else:
    print("True mean doesnt fall in range of confidence interval")



# Code ends here


# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
plt.fig , axes = plt.subplots(nrows=3,ncols=1)
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        n=sample_size[i]
        sample_data = data['installment'].sample(n)
        m.append(sample_data.mean())
#print(m)
mean_series = pd.Series(m)
axes[i] = mean_series.hist()
#print(mean_series)
#plt.show()


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
#print(data['int.rate'])
#print(data['int.rate'][100])
data['int.rate'] = data['int.rate'].astype(str).str[:-1].astype(float)
data['int.rate'] = data['int.rate']/100
#print(data['int.rate'][100])
#print(data['int.rate'])
z_statistic, p_value = ztest(x1=data[data['purpose']=='small_business']['int.rate'],x2=None,value=data['int.rate'].mean(),alternative='larger')
if p_value > 0.05:
    inference = "Accept"
elif p_value <= 0.05:
    inference = "Reject"
print(inference)

#data['int.rate'] = data['int.rate'].astype(float)
#data['int.rate'] = data['int.rate']/100


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here

z_statistic, p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'])
if p_value > 0.05:
    inference = "Accept"
elif p_value <= 0.05:
    inference = "Reject"
print(inference)


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
#print(data[(data['paid.back.loan']=='Yes')]['purpose'])
yes = data[(data['paid.back.loan']=='Yes')]['purpose'].value_counts()
no = data[(data['paid.back.loan']=='No')]['purpose'].value_counts()
print(yes.transpose())
observed = pd.concat([yes.transpose(),no.transpose()],keys=['Yes','No'],axis=1)
chi2, p , dof, ex = chi2_contingency(observed)
print(chi2,critical_value)
if(chi2 > critical_value):
    print("Reject")
else:
    print("Accept")



