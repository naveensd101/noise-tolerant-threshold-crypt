import gurobipy as gp

# Define the LP problem
model = gp.Model("LP example")
x1 = model.addVar(lb=0, name="x1")
x2 = model.addVar(lb=0, name="x2")
y1 = model.addVar(vtype=gp.GRB.BINARY, name="y1")
model.setObjective(2*x1 + x2 + y1, gp.GRB.MAXIMIZE)
model.addConstr(3*x1 + 4*x2 + y1 <= 10, name="c1")
model.addConstr(2*x1 - x2 >= 1, name="c2")

# Set solver parameters (optional)
model.Params.OutputFlag = 0  # suppress solver output
model.Params.TimeLimit = 10  # set solver time limit to 10 seconds

# Solve the LP problem
model.optimize()

# Print the solution
if model.status == gp.GRB.OPTIMAL:
    print("Optimal solution found")
    print(f"x1 = {x1.X:.2f}")
    print(f"x2 = {x2.X:.2f}")
    print(f"y1 = {y1.X}")
    print(f"Objective value = {model.objVal:.2f}")
else:
    print("No optimal solution found")
