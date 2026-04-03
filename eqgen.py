import random


def hyperplanes(n, m, l, point, upper, bigm):
    """
    input1: n, Number of variables in the equation
    input2: m, Number of equations you need which pass through point
    input3: l, Number of equations you need which doesn't have to pass through point
    input4: point, point through which equation should pass
    input5: upper, upper bound on the value of variable
    input6: bigm, big m value used in eqns

    output: Print the whole source code for LP problem
    """
    correct_lines = []
    # For the m correct lines i will generate a list with n-1 random numbers
    # nth number will be set according to the point
    for _ in range(m):
        coefficients = [random.random() for _ in range(n)]
        const = 0
        for i in range(n):
            const += coefficients[i] * point[i]
        coefficients.append(-1 * const)
        correct_lines.append(coefficients)

    wrong_lines = []
    for _ in range(l):
        while True:
            coefficients = [random.random() for _ in range(n + 1)]
            does_it_pass = False
            ans = 0
            for i in range(n):
                ans += coefficients[i] * point[i]
            ans += coefficients[n]
            does_it_pass = ans == 0
            if not (does_it_pass):
                wrong_lines.append(coefficients)
                break

    with open("eqn.txt", "w") as f:
        f.write(str(n))
        f.write('\n')
        f.write(str(m))
        f.write('\n')
        f.write(str(l))
        f.write('\n')
        f.write(str(bigm))
        f.write('\n')
        f.write(str(point))
        f.write('\n')
        for i in range(m):
            f.write(",".join(list(map(str, correct_lines[i]))))
            f.write('\n')
        for i in range(l):
            f.write(",".join(list(map(str, wrong_lines[i]))))
            f.write('\n')


"""
input1: n, Number of variables in the equation
input2: m, Number of equations you need which pass through point
input3: l, Number of equations you need which doesn't have to pass through point
input4: point, point through which equation should pass
input5: upper, upper bound on the value of variable
input6: bigm, big m value used in eqns

output: Print the whole source code for LP problem
"""

# NO_OF_CORRECT_EQNS >= NO_OF_VARS + 1

UPPER_BOUND_ON_VARS = 1
NO_OF_VARS = 10
NO_OF_CORRECT_EQNS = 11
NO_OF_WRONG_EQNS = 9
BIG_M = 10 * NO_OF_VARS

POINT = [random.randint(0, 100000000) / 100000000 for _ in range(NO_OF_VARS)]
hyperplanes(
    NO_OF_VARS, NO_OF_CORRECT_EQNS, NO_OF_WRONG_EQNS, POINT, UPPER_BOUND_ON_VARS, BIG_M
)
