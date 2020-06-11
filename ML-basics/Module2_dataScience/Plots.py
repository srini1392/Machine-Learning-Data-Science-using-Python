### Title           :   Plots.py
### Author          :	Srinikethan M
### Date & Time     :	2019-12-30 14:05:22

# importing the required module 
import pandas as pd
import matplotlib.pyplot as plt 

'''
# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()
'''


# Concept of Joins
#data frame 1
dataframe1 = pd.DataFrame({
    "employee"  :["ABC", "XYZ", "MNO"],
    "Age"    :["22", "25", "30"]
})

dataframe2 = pd.DataFrame({
    "employee"  :["ABC", "XYZ", "PQR"],
    "Salary"    :["100000", "125000", "30000"]
})

df3 =  pd.merge(dataframe1,dataframe2, on="employee")               #inner joining of data frames
df4 =  pd.merge(dataframe1,dataframe2, on="employee", how="outer")  #outer joining of data frames
df5 =  pd.merge(dataframe1,dataframe2, on="employee", how="left")   #left joining of data frames
df6 =  pd.merge(dataframe1,dataframe2, on="employee", how="right")  #right joining of data frames

# print(df3)
# print('\n \n')
# print(df4)
# print('\n \n')
# print(df5)
# print('\n \n')
# print(df6)
# print('\n \n')


# Pivoting 
webtraffic = pd.read_csv('D:\VMC\Git_commits\Python-Programming\ML-basics\Module2_dataScience\pivot.csv')
# print(webtraffic)

#pivot the rows and columns
webtraffic.pivot(index="Page_Name",columns="Date")
# print(webtraffic.pivot_table(index="Page_Name",aggfunc="sum"))
# print(webtraffic.pivot_table(index="Page_Name",aggfunc="mean"))
# print(webtraffic.pivot_table(index="Page_Name",aggfunc="count"))