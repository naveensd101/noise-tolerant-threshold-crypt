import random
import sys

def precode(n, m, l, upper):
    print("# import the library pulp as p")
    print("import pulp as p")
    print()
    print("# Create a LP Minimization problem")
    print("Lp_prob = p.LpProblem('Problem', p.LpMinimize)")
    # we need n variables for equations
    print("# Create problem Variables")
    for i in range(n):
        print(f"x{i} = p.LpVariable(\"x{i}\", lowBound=0, upBound={upper})")
    print()
    for i in range(m+l):
        print(f"z{i} = p.LpVariable(\"z{i}\", cat = p.LpBinary)")
    print()
    print("# Objective Function")
    print("Lp_prob += p.lpSum([", end="")
    for i in range(m+l-1):
        print(f"z{i}, ", end="")
    print(f"z{m+l-1}])")
    print()
def postcode(n, m, l, point):
    print("solver = p.MOSEK()")
    print("status = Lp_prob.solve(solver) # Solver")
    print("print(p.value(Lp_prob.objective))")
    print()
    # print("# Printing x values")
    # for i in range(n):
    #     print(f"print(\"x{i} = \", p.value(x{i}))")
    print("# Finding the diff")
    print("print(", end="")
    for i in range(n):
        print(f"p.value(x{i})", " + ", end="")
    print(-sum(point), ")")
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
    # for i in range(n):
    #     print(f"x{i} = {point[i]}", file=sys.stderr)
    precode(n, m, l, upper)
    correct_lines = []
    # For the m correct lines i will generate a list with n-1 random numbers
    # nth number will be set according to the point
    for _ in range(m):
        coefficients = [random.random() for _ in range(n)]
        const = 0
        for i in range(n):
            const += coefficients[i]*point[i]
        coefficients.append(-1*const)
        correct_lines.append(coefficients)

    print(f"bigM = {bigm}")
    # Print the correct lines
    print(f"# {m} correct equations passing through {point}")
    for i in range(m):
        print("Lp_prob += p.lpSum([", end="")
        for j in range(n):
            print(f"{correct_lines[i][j]}*x{j}, ", end="")
        print(f"{correct_lines[i][n]}]) >= -1*bigM*z{i}")
    print("#------------------")
    for i in range(m):
        print("Lp_prob += p.lpSum([", end="")
        for j in range(n):
            print(f"{correct_lines[i][j]}*x{j}, ", end="")
        print(f"{correct_lines[i][n]}]) <= bigM*z{i}")

    wrong_lines = []
    for _ in range(l):
        while True:
            coefficients = [random.random() for _ in range(n+1)]
            does_it_pass = False
            ans = 0
            for i in range(n):
                ans += coefficients[i]*point[i]
            ans += coefficients[n]
            does_it_pass = ans == 0
            if not(does_it_pass):
                wrong_lines.append(coefficients)
                break
    # Print wrong lines
    print(f"# {l} wrong equations")
    for i in range(l):
        print("Lp_prob += p.lpSum([", end="")
        for j in range(n):
            print(f"{wrong_lines[i][j]}*x{j}, ", end="")
        print(f"{wrong_lines[i][n]}]) >= -1*bigM*z{i+m}")
    print("#------------------")
    for i in range(l):
        print("Lp_prob += p.lpSum([", end="")
        for j in range(n):
            print(f"{wrong_lines[i][j]}*x{j}, ", end="")
        print(f"{wrong_lines[i][n]}]) <= bigM*z{i+m}")
    print("#------------------")
    print("#------------------")
    postcode(n, m, l, point)



"""
input1: n, Number of variables in the equation
input2: m, Number of equations you need which pass through point
input3: l, Number of equations you need which doesn't have to pass through point
input4: point, point through which equation should pass
input5: upper, upper bound on the value of variable
input6: bigm, big m value used in eqns

output: Print the whole source code for LP problem
"""

UPPER_BOUND_ON_VARS = 1
NO_OF_VARS = 1000
NO_OF_CORRECT_EQNS = 1001
NO_OF_WRONG_EQNS = 999
BIG_M = 10000

POINT = [random.randint(0, 100000000)/100000000 for _ in range(NO_OF_VARS)]
#POINT = [random.random() for _ in range(NO_OF_VARS)]
hyperplanes(NO_OF_VARS, NO_OF_CORRECT_EQNS, NO_OF_WRONG_EQNS, POINT, UPPER_BOUND_ON_VARS, BIG_M)
