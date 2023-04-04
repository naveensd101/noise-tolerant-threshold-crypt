import numpy as np
from random import randint

def generate_hyperplanes(num_hyperplanes, point):
    # Determine the dimensionality of the space (based on the length of the point vector)
    dim = len(point)

    # Generate num_hyperplanes random vectors of length dim
    vectors = np.random.rand(num_hyperplanes, dim)

    # Normalize the vectors to have unit length
    vectors = vectors / np.linalg.norm(vectors, axis=1)[:, np.newaxis]

    # Generate the hyperplanes passing through the given point
    hyperplanes = []
    for v in vectors:
        # Calculate the constant term for the hyperplane
        constant = np.dot(point, v)

        # Generate the equation of the hyperplane
        eqn = [f"{v[i]}x{i}" if v[i] != 0 else "" for i in range(dim)]
        eqn = " + ".join(eqn) + f" = {constant}"

        # Add the hyperplane to the list
        hyperplanes.append(eqn)

    return hyperplanes

def mod_generate_hyperplanes(num_planes, point):
    planes = []
    for i in range(num_planes):
        # Generate a random set of coefficients for the hyperplane
        coeffs = [randint(1, 10) for _ in range(10)]

        # Compute the constant term to ensure the hyperplane passes through the given point
        constant = 0
        for j in range(10):
            constant += coeffs[j] * point[j]

        # Construct the hyperplane string
        plane_str = " + ".join([f"{coeffs[j]}*x{j}" for j in range(10)]) + f" = {constant}"

        # Add the hyperplane string to the list of planes
        planes.append(plane_str)

    # Construct the LP constraints strings for the planes
    constraints = []
    for plane in planes:
        constraint1 = plane.replace(" = ", " <= ")
        constraint2 = plane.replace(" = ", " >= ")
        constraints.append(constraint1 + " + 1000*z" + str(i))
        constraints.append(constraint2 + " - 1000*z" + str(i))

    # Combine the constraints into a single LP constraints string
    lp_constraints = "\n".join(["Lp_prob += " + c for c in constraints])

    return lp_constraints

#point = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3, 1])
#num_hyperplanes = 20
#hyperplanes = generate_hyperplanes(num_hyperplanes, point)
##print(hyperplanes)
#for i in hyperplanes:
#    print(i)

point = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2])
num_hyperplanes = 40
hyperplanes = generate_hyperplanes(num_hyperplanes, point)
#print(hyperplanes)
for i in hyperplanes:
    print(i)
