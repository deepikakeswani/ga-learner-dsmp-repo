# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')



# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',axis=1)
#print(banks.isnull().sum())
bank_mode=banks.mode()
print(type(bank_mode))
print(bank_mode)
for column in banks.columns:
    print("bank_mode",bank_mode[column][0])
    banks[column].fillna(bank_mode[column][0],inplace=True)
print("Gender Value",banks['Gender'].value_counts(dropna=False))
print("Total number of nan",banks.isna().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values=['LoanAmount'],aggfunc='mean')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here
print(banks.columns)




loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].shape[0]
print(loan_approved_se)
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].shape[0]  
print(loan_approved_nse)
Loan_Status = 614
percentage_se = loan_approved_se/Loan_Status * 100
print(percentage_se)
percentage_nse = loan_approved_nse/Loan_Status * 100
print(percentage_nse)
# code ends here


# --------------
# code starts here
print(bank.columns)
loan_term= banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = loan_term[loan_term >= 25].count()
print(big_loan_term)

# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
print(loan_groupby)
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
print(loan_groupby.head(5))
mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


