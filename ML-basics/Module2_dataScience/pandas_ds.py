### Title           :   Pandas_ds.py
### Author          :	Srinikethan M
### Date & Time     :	2019-12-04 17:03:11

import json
import pandas as pd
from pandas.io.json import json_normalize 

# tab delimited files
employee = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\EmployeeData.tsv',sep = '\t')

# pipe delimited files
reads_pipes = pd.read_table('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\\2009PowerStatus.txt',sep ='|')
reads_pipe = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\\2009PowerStatus.txt',sep ='|')

# json files
reads_json = pd.read_json('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\\json_data.json')


with open('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\\Server_data.json') as f:
    data = json.load(f)

# printing the data

print("\n \n")
print(employee.head())
print("\n \n")
print(reads_pipes.head())
print("\n \n")
print(reads_pipe.head())
print("\n \n")
print(reads_json.head())

reads_population_json = json_normalize(data = data['programs'], record_path="works", meta= ['id','orchestra','programID','season'])
soloist_data = json_normalize(data = data['programs'], record_path =['works','soloists'], meta=['id'])
# print(reads_population_json.head(3))
# print(soloist_data.head(3))