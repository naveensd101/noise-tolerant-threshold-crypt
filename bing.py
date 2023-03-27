import scipy.optimize as opt
import numpy as np

# Define the coefficient matrix A and the constant vector b
A = np.array([[4, 3, 1], [7, 5, 9], [2, 4, 6]])
b = np.array([10, 20, 30])

# Define the objective function to be minimized as the negative sum of b
def objective(x):
    return -np.sum(b)

# Define the constraints as the system of equations
def constraint(x):
    return A @ x - b

# Define the bounds for the variables as non-negative
bounds = [(0, None) for _ in range(len(A[0]))]

# Solve the optimization problem using scipy.optimize.minimize function
result = opt.minimize(objective, x0=np.zeros(len(A[0])), bounds=bounds, constraints={'type': 'eq', 'fun': constraint})

# Print the optimal solution and the number of solved equations
print(result.x)
print(np.count_nonzero(np.isclose(A @ result.x, b)))