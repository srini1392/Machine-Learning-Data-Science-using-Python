import sklearn
from sklearn.datasets import load_iris

#input has to be always numerical, since the output predictions for iris data is not numerical, 
#we are using numpy to convert them (internally) which is represented in target_names
iris = load_iris()


# print(type(iris)) //to check the type of iris
sklearn.utils.Bunch


'''
feature names is the petal&sepal width,height
# iris.feature_names 
# iris.target_names
iris.target will have nominclature for the output names
0 - setosa, 1- versicolor, 2- virginica
iris.data contains all of the data as "X" 
'''


X = iris.data
y = iris.target


print("Feature names in Iris data set",iris.feature_names)
print("Target names in Iris data set",iris.target_names)


'''
Use KNN algorithm to predict the output
sklearn.kneighbours is the class used for KNN
class sklearn.neighbors


KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=1, p=2,
           weights='uniform')

'''



from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1) #instantiate the classifier with number of neighbors =1
# print(knn)
knn.fit(X,y) #fitting the model with data

print("Names of the Type of iris are\n")
print(iris.target_names)

'''
data set 1 :
for prediction with neighbour = 1
'''
# prediction1 = knn.predict([[2,4,3,1]])
# print(prediction1)

'''
data set 2 :
'''
# prediction2 = knn.predict([[1,4,5,7],[2,4,6,9],[2,4,3,1]])
# print(prediction2)

'''
data set 3 :
'''
# prediction3 = knn.predict([[2,4,3,1],[4,6,5,3]])
# print(prediction3)


'''
data set 4 :
for prediction with neighbour = 5
'''
# knn5 = KNeighborsClassifier(n_neighbors=5)
# knn5.fit(X,y)
# prediction5 = knn5.predict([[2,4,3,1],[4,6,5,3]])
# print(prediction5)


'''
data set 5:
for prediciton wih neighour ranges from 1 to 30
''' 
for i in range(1,30):
    knn_i = KNeighborsClassifier(n_neighbors=i)
    knn_i.fit(X,y)
    prediction_i = knn_i.predict([[2,4,3,1],[4,6,5,3]])
    print(" when neighbour value is " + str(i) +" , the prediction using KNN is" + str(prediction_i))