import linearRegression
import retrieveData
import numpy as np

(data_x, data_y) = retrieveData.retrieveData()

x = np.array(data_x)
y = np.array(data_y)

min_x = np.amin(x)
max_x = np.amax(x)

# Scaling
scaled_x = (x - min_x) / (max_x - min_x)
list_x = scaled_x.tolist()

# Normalization
normalized_y = y / 100
list_y = normalized_y.tolist()

(alpha, beta, stdError, lowerBound, upperBound) = linearRegression.linearRegression(list_x, list_y)

print("\nWith given format of Y = alpha + beta*X:\n")
print("Alpha value is: " + str(alpha))
print("Beta value is: " + str(beta))
print("Standard error is: " + str(stdError))
print("95% Confidence interval for beta: " + str(lowerBound) + " - " + str(upperBound))

linearRegression.plotGraph(list_x, list_y, alpha, beta)
