import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/linear_regression/train.csv').dropna()
print(data.info())
print(data.head())

def gradient_descent(m, b, points, L = 0.0001):
    """Basic Gradient descent for linear regression

    Parameters
    ----------
    m : float
        slope
    b : float
        bias
    points :  pandas dataframe
        data points
    L : float, optional
        Learning rate, by default 0.001

    Returns
    -------
    (m, b)
        Updated m,b
    """    
    m_grad = b_grad = 0
    n = len(points)

    for i in range(n):
        X = points.iloc[i].x 
        y = points.iloc[i].y

        m_grad += -(2/n) * X * (y - (m * X + b))
        b_grad += -(2/n) * (y - (m * X + b))
    # print(m,b, m_grad, b_grad)
    m = m - m_grad * L 
    b = b - b_grad * L 
    return m,b 

m = b = 0
epochs = 200

for i in range(epochs):
    if i % 50 == 0:
        print(f'epoch: {i},m: {m}, b: {b}')
    m, b = gradient_descent(m, b, data)

print(m,b)

test_data = pd.read_csv('../data/linear_regression/test.csv').dropna()

plt.scatter(test_data.x, test_data.y, color = 'black')
plt.plot(list(range(0,100)), [m * x +b for x in range(0,100)], color='red')
plt.show()