import numpy as np
import matplotlib.pyplot as plot
import math

# Simple linear regression formula used.

# References:
# http://seismo.berkeley.edu/~kirchner/eps_120/Toolkits/Toolkit_10.pdf
# https://www.wikiwand.com/en/Linear_regression
# https://www.wikiwand.com/en/Linear_least_squares


def linearRegression(data_x, data_y):
    x = np.array(data_x)
    y = np.array(data_y)

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    observations = np.size(y)

    SSxy = np.sum(y*x) - observations*y_mean*x_mean
    SSxx = np.sum(x*x) - observations*np.square(x_mean)

    beta = SSxy/SSxx
    alpha = y_mean - beta*x_mean

    y_predicted = alpha + beta*x

    stdError = math.sqrt(np.sum(np.square(y_predicted - y)) / ((observations - 2) * np.sum(np.square(x - x_mean))))

    lowerBound = beta - 1.96*stdError
    upperBound = beta + 1.96*stdError

    return alpha, beta, stdError, lowerBound, upperBound


def plotGraph(data_x, data_y, alpha, beta):
    x = np.array(data_x)
    y = np.array(data_y)

    y_predicted = alpha + beta*x

    plot.scatter(x, y, c='b', marker='o')
    plot.plot(x, y_predicted, c='r')

    plot.xlabel('GDP per capita (current US$)')
    plot.ylabel('Unemployment, total (% of total labor force) (modeled ILO estimate)')

    plot.show()

