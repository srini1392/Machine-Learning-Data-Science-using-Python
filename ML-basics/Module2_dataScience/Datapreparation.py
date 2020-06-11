### Title           :   Datapreparation.py
### Author          :	Srinikethan M
### Date & Time     :	2019-12-27 14:27:13

import pandas as pd
import numpy as np


''' Selection of Columns
cols = ['Name','Position']
# tab delimited files
employee = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\EmployeeData.tsv',sep = '\t')
print(employee[cols].head())
'''

'''Selection of Rows
employee = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\EmployeeData.tsv', sep ='\t',nrows =4)
print(employee)
'''

''' Displaying Data types'''
employee = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\EmployeeData.tsv', sep ='\t')
print(employee.select_dtypes(include = [np.number]).dtypes)
print(employee.shape)
print(type(employee))

