# Python for Data Science

## Summary
Introduction to Data science for Python. 
Explores the Predicting and Pattern Analyzing the data.

<H3>
_Machine Learning_ is the field of computer Science that gives computers the ability to learn, without explicitly being programmed.
</H3>



### Machine Learning Model
     _ _ _ _ _ _ _ _ _ _ _            _ _ _ _ _ _ _ _ _ _ _           _ _ _ _ _ _ _ _ _ _ _
    |                     |          |  Machine Learning   |         |Pattern / Predictions|
    |      Input Data     |  ---->   |    Algorithm        | ---->   | Knowledge           |
    |_ _ _ _ _ _ _ _ _ _ _|          |_ _ _ _ _ _ _ _ _ _ _|         |_ _ _ _ _ _ _ _ _ _ _|

1. <H4>The inputs need to be relevent to the algorithm </H4>
2. <H4>There are two types of Algorithms</H4>
        <p><H4>* Supervised Learning </p>
            * UnSupervised Learning </H4>



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

