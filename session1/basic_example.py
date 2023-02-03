import random
from sklearn.linear_model import LinearRegression
import numpy as np

"""
Solve for a, b and c using the following equations

 a + b + c = 9
 2a + 4b + 3c = 9
 23x + 62y + z = 10
"""

coef = [
    [1, 1, 1],
    [2, 4, 3],
    [23, 62, 1]
]

values = [9, 9, 10]

alpha = 0.001

soln = [
    random.random() for i in range(3)
]

n = len(values)
m = 3

for epoch in range(500000):
    soln_new = [i for i in soln]
    for i in range(n):
        h = 0
        for j in range(m):
            h += coef[i][j] * soln[j]
        for j in range(m):
            soln_new[j] += (alpha / n) * coef[i][j] * (values[i] - h)
        
    soln = soln_new
    
print(soln)
# Expected: [13.24096386, -4.75903614,  0.51807229]

y = 5
X = 6

for epoch in range(500000):
    h = X @ soln
    soln += ((alpha / n) * (X.T @ (y - h)))


