import sklearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier


iris = load_iris()
sklearn.utils.Bunch
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size =0.3)
# total data size currently
print(X.shape)

# Split of the X data present
print(X_train.shape)
print(X_test.shape)

# Split of the y data present
print(y_train.shape)
print(y_test.shape)


#using logistic regression
logisticReg = LogisticRegression()
logisticReg.fit(X_train, y_train)

y_pred = logisticReg.predict(X_test)
print("logistic predicitons")
print(metrics.accuracy_score(y_test,y_pred))


knn = KNeighborsClassifier(n_neighbors=1)
knn5 = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn5.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)
y_pred5_knn = knn5.predict(X_test)
print("\n knn predicitions")
print(metrics.accuracy_score(y_test,y_pred_knn))

print("\n knn5 predicitions")
print(metrics.accuracy_score(y_test,y_pred5_knn))


######### New training test set with Split of 40%
X_train1, X_test1, y_train1, y_test1 = train_test_split(X,y, test_size =0.4, random_state =4)

# Split of the X data present
print(X_train1.shape)
print(X_test1.shape)

# Split of the y data present
print(y_train1.shape)
print(y_test1.shape)


#using logistic regression
logisticReg = LogisticRegression()
logisticReg.fit(X_train1, y_train1)

y_pred = logisticReg.predict(X_test1)
print("logistic predicitons")
print(metrics.accuracy_score(y_test1,y_pred))


knn = KNeighborsClassifier(n_neighbors=1)
knn5 = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train1, y_train1)
knn5.fit(X_train1, y_train1)

y_pred_knn = knn.predict(X_test1)
y_pred5_knn = knn5.predict(X_test1)
print("\n knn predicitions")
print(metrics.accuracy_score(y_test1,y_pred_knn))

print("\n knn5 predicitions")
print(metrics.accuracy_score(y_test1,y_pred5_knn))