'''
IRIS Data Set Solutions Using KNN Machine Learning Model

Pseudo Code:
1. Load the Data
2. Initialise the value of k (nearest neighbour value)
3. For getting the predicted class, iterate from 1 to total number of training data points
    a. Calculate the distance between test data and each row of training data. We will use the Euclidean distance as our metric.
    b. Sort the calculated distances in ascending order based on distance values. 
    c. Get the top k rows from the sorted array
    d. Get the most frequent class of these rows. 
    e. Return the predicted class. 

Building in pYthon from Scratch
'''
#Importing libraries
import pandas as pd
import numpy as np 
import math
import operator

#### STEP 1
#Load the Data
data = pd.read_csv("iris_data.csv")
data.head()

### Defining a function to calculate the EUCLIDEAN distance between two data points
def euclideanDistance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    return np.sqrt(distance)


##Defining our KNN model
def knn(trainingSet, testInstance, k):
    distances ={}
    sort = {}
    length = testInstance.shape[1]
#end
#---------------------------------------------------------------------------------------#

##### STEP 3
# Calculating the euclidean distance between each row of training data and test data
    for x in range(len(trainingSet)):
        #STEP 3.1
        dist = euclideanDistance(testInstance, trainingSet.iloc[x], length)
        distances[x] = dist[0]
        #end

    #STEP 3.2
    #sorting them on the basis of distance
    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    #end
    neighbours = []


    #STEP 3.3
    #extracting top k neighbours
    for x in range(k):
        neighbours.append(sorted_d[x][0])
    #end
    classVotes = {}


    #STEP 3.4
    #calculating the most frequent class in the neighbours
    for x in range(len(neighbours)):
        response = trainingSet.iloc[neighbours[x]][-1]

        if response in classVotes:
            classVotes[response] +=1
        else:
            classVotes[response] =1
    #end


    #STEP 3.5
    sortedVotes =  sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return(sortedVotes[0][0],neighbours)
#end
#---------------------------------------------------------------------------------------#


##### Creating a dummy Test set
testSet = [[7.2,3.6,5.1,2.5]]
test = pd.DataFrame(testSet)

#### STEP 2
#setting number of neighbours
# k = 1
k = 3
# k = 5
#end

#### Running the KNN Model
result,neigh = knn(data,test,k)

#Predicted class, Nearest Neighbour
print(result)
print(neigh)
#---------------------------------------------------------------------------------------#







'''
Building in pYthon from Module
Comparing the Model with Scikit-Learn
'''
from sklearn.neighbors import KNeighborsClassifier
scikit_neigh = KNeighborsClassifier(n_neighbors =3)
scikit_neigh.fit(data.iloc[:,0:4],data['Name'])

#predicted class
print("\n Output Prediction from SCIKIT-LEARN MODEL")
print(scikit_neigh.predict(test))
print(scikit_neigh.kneighbors(test)[1])
#---------------------------------------------------------------------------------------#