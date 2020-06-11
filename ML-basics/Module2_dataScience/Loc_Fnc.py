### Title           :   Loc_Fnc.py
### Author          :	Srinikethan M
### Date & Time     :	2019-12-30 13:46:13


import pandas as pd

#the data
employee = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\EmployeeData.tsv', sep ='\t')

''' row, :-> all columns ''' 
# print(employee.loc[0:2,:])

'''rows 0->2 columns 2'''
# print(employee.loc[0:2,['Name', 'Position']])
# print(employee.loc[0:2,'Name':'Office'])

''' rows with certain conditions'''
# print(employee.loc[employee.Position=='Accountant',:])

''' drop NA '''

employee = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\MissingValues.tsv', sep ='\t')
# print(employee.head())
# print(employee.shape)

#this is to drop rows with all missing values in every column
# print(employee.dropna(how='any').shape)

#this is to drop rows with all missing values in certain columns
print(employee.dropna(how='any').shape)
print('\n \n')

print(employee.fillna(0).shape)
print(employee)