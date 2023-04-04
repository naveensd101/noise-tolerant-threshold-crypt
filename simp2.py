# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMinimize)

# Create problem Variables
x0 = p.LpVariable("x0")
x1 = p.LpVariable("x1")
x2 = p.LpVariable("x2")

z0 = p.LpVariable("z0", cat = p.LpBinary)
z1 = p.LpVariable("z1", cat = p.LpBinary)
z2 = p.LpVariable("z2", cat = p.LpBinary)
z3 = p.LpVariable("z3", cat = p.LpBinary)
z4 = p.LpVariable("z4", cat = p.LpBinary)

# Objective Function
Lp_prob += z0 + z1 + z2 + z3 + z4

# Constraints:

Lp_prob += x0+x1+x2<=3+1000*z0
Lp_prob += x0-x1+x2<=1+1000*z1
Lp_prob += x0+x1-x2<=1+1000*z2
Lp_prob += -x0+x1+x2<=1+1000*z3
Lp_prob += x0+x1+x2<=4+1000*z4

Lp_prob += x0+x1+x2>=3-1000*z0
Lp_prob += x0-x1+x2>=1-1000*z1
Lp_prob += x0+x1-x2>=1-1000*z2
Lp_prob += -x0+x1+x2>=1-1000*z3
Lp_prob += x0+x1+x2>=4-1000*z4

# Display the problem
print(Lp_prob)

status = Lp_prob.solve(p.GLPK()) # Solver
print(p.LpStatus[status]) # The solution status

# Printing the final solution
print(p.value(Lp_prob.objective))
