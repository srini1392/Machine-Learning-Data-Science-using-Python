<H1>Data Science for Python</H1>

## Summary
Introduction to Data science for Python. 
Explores the Predicting and Pattern Analyzing the data.

_Machine Learning_ is the field of computer Science that gives computers the ability to learn, without explicitly being programmed.

### Machine Learning Model
     _ _ _ _ _ _ _ _ _ _ _            _ _ _ _ _ _ _ _ _ _ _           _ _ _ _ _ _ _ _ _ _ _
    |                     |          |  Machine Learning   |         |Pattern / Predictions|
    |      Input Data     |  ---->   |    Algorithm        | ---->   | Knowledge           |
    |_ _ _ _ _ _ _ _ _ _ _|          |_ _ _ _ _ _ _ _ _ _ _|         |_ _ _ _ _ _ _ _ _ _ _|

1. The inputs need to be relevent to the algorithm
2. There are two types of Algorithms
        <p> * Supervised Learning </p>
            * UnSupervised Learning


## Breaking it Down – Pseudo Code of KNN
We can implement a KNN model by following the below steps:

1. Load the data
2. Initialise the value of k
3. For getting the predicted class, iterate from 1 to total number of training data points
4. Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as our distance metric   since it’s the most popular method. The other metrics that can be used are Chebyshev, cosine, etc.
5. Sort the calculated distances in ascending order based on distance values
6. Get top k rows from the sorted array
7. Get the most frequent class of these rows
8. Return the predicted class


# Logistic Regression

Logistic regression is the appropriate regression analysis to conduct when the dependent variable is dichotomous (binary).  Like all regression analyses, the logistic regression is a predictive analysis.  Logistic regression is used to describe data and to explain the relationship between one dependent binary variable and one or more nominal, ordinal, interval or ratio-level independent variables.
This is used to solve a "_Classification Problem_"

#### Binary logistic regression major assumptions:

The dependent variable should be dichotomous in nature (e.g., presence vs. absent).
There should be no outliers in the data, which can be assessed by converting the continuous predictors to standardized scores, and removing values below -3.29 or greater than 3.29.
There should be no high correlations (multicollinearity) among the predictors.  This can be assessed by a correlation matrix among the predictors. 
At the center of the logistic regression analysis is the task estimating the log odds of an event.  Mathematically, logistic regression estimates a multiple linear regression function defined as:



$$
logit(p) = \log \binom {\frac{p(y=1)}{1-(p=1)}}{ } = \beta_0 + \beta_1 {x_i}_2 + \beta_2 {x_i}_2 +  \ldots  + \beta_n {x_i}_n
$$
 
for i = 1…n .


#### Overfitting
 When selecting the model for the logistic regression analysis, another important consideration is the model fit.  Adding independent variables to a logistic regression model will always increase the amount of variance. 
 However, adding more and more variables to the model can result in overfitting,which reduces the generalizability of the model beyond the data on which the model is fit.