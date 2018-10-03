''' IRIS Target Prediction using Both KNN and Logistic Regression ML Algorithms '''

import sklearn
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

iris = load_iris()
sklearn.utils.Bunch
X = iris.data
y = iris.target


#### Using KNN algorithm to get the prediction -----------------------#
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)

print("\n Names of the Type of iris are")
print(iris.target_names)
prediction_knn = knn.predict([[5.1,3.5,1.4,0.2],[6.3,3.3,4.7,1.6]])
print("\n the prediction using KNN is:")
print(prediction_knn)

# --------------------------------------------------------------------#




#### Using Logistic Regression to get the prediction -----------------#
logisticreg = LogisticRegression()
logisticreg.fit(X,y)
prediction_logisticReg = logisticreg.predict([[5.1,3.5,1.4,0.2],[6.3,3.3,4.7,1.6]])
print("\n the prediction using logistic reg is:")
print(prediction_logisticReg)
# --------------------------------------------------------------------#