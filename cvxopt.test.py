# Import the necessary libraries
from cvxopt import matrix, solvers

# Create problem Variables
x = matrix([0.0, 0.0, 0.0])
z = matrix([0, 0, 0, 0, 0], tc='i')

# Define the objective function
c = matrix([1.0, 1.0, 1.0, 1.0, 1.0])

# Define the inequality constraints matrix
G = matrix([
    [-1.0, 0.0, 0.0, -1000.0, 0.0],
    [1.0, -1.0, 0.0, 0.0, -1000.0],
    [1.0, 1.0, -1.0, 0.0, 0.0],
    [-1.0, 1.0, 1.0, 0.0, 0.0],
    [-1.0, -1.0, -1.0, 0.0, 0.0],
    [1.0, 0.0, 0.0, 1000.0, 0.0],
    [-1.0, 1.0, 0.0, 0.0, 1000.0],
    [-1.0, -1.0, 1.0, 0.0, 0.0]
])

# Define the inequality constraints vector
h = matrix([3.0, 1.0, 1.0, 1.0, 0.0, -3.0, -1.0, -1.0])

# Solve the problem
sol = solvers.glpk(c, G, h, A=None, B=None, I=None, BVS=None, 
                   freevars=None, maxiter=None, msg_lev=None, options=None, 
                   primalstart=None, dualstart=None, pricing=None, 
                   callback=None)

# Extract the optimal solution
x = sol['x']

# Print the optimal solution
print('Optimal solution:')
print('x0 =', x[0])
print('x1 =', x[1])
print('x2 =', x[2])
print('z0 =', int(x[3]))
print('z1 =', int(x[4]))
print('z2 =', int(x[5]))
print('z3 =', int(x[6]))
print('z4 =', int(x[7]))
