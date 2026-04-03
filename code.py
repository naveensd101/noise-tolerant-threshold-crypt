# import the library pulp as p
import pulp as p

correct = []
wrong = []
with open('eqn.txt') as f:
    NO_OF_VARS = int(f.readline())
    NO_OF_CORRECT_EQ = int(f.readline())
    NO_OF_WRONG_EQ = int(f.readline())
    BIG_M = int(f.readline())
    POINT = list(map(float, f.readline()[1:-2].split(', ')))
    for i in range(NO_OF_CORRECT_EQ):
        correct.append(list(map(float, f.readline().split(','))))
    for i in range(NO_OF_WRONG_EQ):
        wrong.append(list(map(float, f.readline().split(','))))
TOTAL_NO_OF_EQ = NO_OF_CORRECT_EQ + NO_OF_WRONG_EQ

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMinimize)
x = p.LpVariable.dicts("x", range(NO_OF_VARS), lowBound=0, upBound=1, cat=p.LpContinuous)
z = p.LpVariable.dicts("z", range(TOTAL_NO_OF_EQ), cat=p.LpBinary)
#------------------
# Objective Function
Lp_prob += p.lpSum(z)

for eq_no in range(NO_OF_CORRECT_EQ):
    Lp_prob += p.lpSum([x[i] * correct[eq_no][i] for i in range(NO_OF_VARS)] + [correct[eq_no][NO_OF_VARS]]) >= -1 * BIG_M * z[eq_no]
    Lp_prob += p.lpSum([x[i] * correct[eq_no][i] for i in range(NO_OF_VARS)] + [correct[eq_no][NO_OF_VARS]]) <= BIG_M * z[eq_no]

for eq_no in range(NO_OF_WRONG_EQ):
    Lp_prob += p.lpSum([x[i] * wrong[eq_no][i] for i in range(NO_OF_VARS)] + [wrong[eq_no][NO_OF_VARS]]) >= -1 * BIG_M * z[eq_no+NO_OF_CORRECT_EQ]
    Lp_prob += p.lpSum([x[i] * wrong[eq_no][i] for i in range(NO_OF_VARS)] + [wrong[eq_no][NO_OF_VARS]]) <= BIG_M * z[eq_no+NO_OF_CORRECT_EQ]

#------------------
solver = p.MOSEK()
status = Lp_prob.solve(solver) # Solver
print(p.value(Lp_prob.objective))

# Finding the diff

RES = [(p.value(x[i])-POINT[i])*10e10 for i in range(NO_OF_VARS)]
# print(POINT)
# print(RES)
# print([p.value(z[i]) for i in range(TOTAL_NO_OF_EQ)])
# print(sum(POINT))
print(sum(RES))
