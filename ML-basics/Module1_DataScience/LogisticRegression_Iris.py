'''
Logistic Regression Algorithm

'''
import sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
sklearn.utils.Bunch
X = iris.data
y = iris.target


#syntax for Logistic Reg
# LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
#           intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
#           penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
#           verbose=0, warm_start=False)

logisticReg = LogisticRegression()
logisticReg.fit(X,y)
prediction_1 = logisticReg.predict([[2,4,3,1],[4,6,5,3]])
print(iris.target_names)
print ("\n The data from iris data set predicts the output using Logistic Regression algorithm is as :")
print(prediction_1)