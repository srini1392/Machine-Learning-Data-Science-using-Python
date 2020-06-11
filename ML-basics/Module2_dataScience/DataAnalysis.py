### Title           :   DataAnalysis.py
### Author          :	Srinikethan M
### Date & Time     :	2019-06-03 14:46:02


import pandas as pd
import numpy as np


employee = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\EmployeeData.tsv', sep ='\t')
# employee['Name Salary'] = employee['Name'] + employee['Salary']

''' to drop columns specifically'''
# employee.drop('Age', axis=1,inplace= True)
# employee.drop('Office', axis=1,inplace= True)
# print(employee.head())

''' Rename Columns '''
# cols = ['Name', 'Position', 'Ofc', 'Age', 'StartDate', 'Sal']
# employee.columns = cols
# print(employee.head())

''' Sorting your data '''
# employee.sort_values(by='Age', ascending=True)
# employee.sort_values(by=['Salary', 'Age'], ascending=True)
# print(employee.head())

# sort based on one column
# print(employee['Salary'].sort_values().head())

''' filtereing values based on clause
select all rows where age < 40
'''
# print(employee[(employee.Age < 40) & (employee.Salary > 10000)].head())
# cols = ['Name', 'Position', 'Age']
# print(employee[employee.Age < 40][cols].head())


''' Calculate mean'''
# print(employee.mean())

'''string manipulation'''
# print(employee.Name.str.upper().head())
# print(employee.Name.str.lower().head())

'''Find particular string'''
# print(employee[employee.Position.str.contains('Software')])

'''Replace data'''
# print(employee.Position.str.replace('Engineer','Developer').head())

'''Aggregations'''
# employee.head()
# print(employee.Age.min())
# print(employee.Age.max())

''' Group-by clause'''
# print(employee.groupby('Position').Age.min().head())
# print(employee.groupby('Position').Age.agg(['count','min','max']).sort_values(by='Position', ascending = True ))

'''Calculate mean'''
# print(employee.mean(axis=0).head())
# print(employee.mean(axis=1).head())