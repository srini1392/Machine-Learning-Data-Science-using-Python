import sklearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


#IRIS datasets
iris = load_iris()
sklearn.utils.Bunch
X = iris.data
y = iris.target


#K-FOLD Cross Validation
# knn = KNeighborsClassifier(n_neighbors=5)
#for 10iterations, provide accuracy
# scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
# print(scores.mean())

k_range = range(1,45)
k_scores = []
for k in k_range:
    knn=KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
    k_scores.append(scores.mean())
# print(k_scores)

#USing matplotlibs to plot the graph
plt.plot(k_range,k_scores)
plt.xlabel('K value for KNN algorithm')
plt.ylabel('Mean accuracy scores')
plt.show()