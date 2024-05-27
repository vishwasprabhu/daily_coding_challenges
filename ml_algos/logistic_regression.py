"""
Implement a basic binary logistic regression classifier. It should perform the following operations:

Train model
Predict on testing data
Assume the training and testing data is in the form of 2D matrix and the class labels is a 1-D array.

Solution:

Important methods to consider:

Computing sigmoid scores
Computing the logistic loss
Gradient descent (batch or stochastic)
"""
import math


def sigmoid_probs(data, weights, bias):
    ...
    return probabilities

def loss(data, labels, weights, bias, reg_lambda):
    ...
    return l