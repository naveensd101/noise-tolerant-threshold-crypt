# import the library pulp as p
import pulp as p
import orloge

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMinimize)
# Create problem Variables
x0 = p.LpVariable("x0")
x1 = p.LpVariable("x1")
x2 = p.LpVariable("x2")
x3 = p.LpVariable("x3")
x4 = p.LpVariable("x4")
x5 = p.LpVariable("x5")
x6 = p.LpVariable("x6")
x7 = p.LpVariable("x7")
x8 = p.LpVariable("x8")
x9 = p.LpVariable("x9")

z0 = p.LpVariable("z0", cat = p.LpBinary)
z1 = p.LpVariable("z1", cat = p.LpBinary)
z2 = p.LpVariable("z2", cat = p.LpBinary)
z3 = p.LpVariable("z3", cat = p.LpBinary)
z4 = p.LpVariable("z4", cat = p.LpBinary)
z5 = p.LpVariable("z5", cat = p.LpBinary)
z6 = p.LpVariable("z6", cat = p.LpBinary)
z7 = p.LpVariable("z7", cat = p.LpBinary)
z8 = p.LpVariable("z8", cat = p.LpBinary)
z9 = p.LpVariable("z9", cat = p.LpBinary)
z10 = p.LpVariable("z10", cat = p.LpBinary)
z11 = p.LpVariable("z11", cat = p.LpBinary)
z12 = p.LpVariable("z12", cat = p.LpBinary)
z13 = p.LpVariable("z13", cat = p.LpBinary)
z14 = p.LpVariable("z14", cat = p.LpBinary)
z15 = p.LpVariable("z15", cat = p.LpBinary)
z16 = p.LpVariable("z16", cat = p.LpBinary)
z17 = p.LpVariable("z17", cat = p.LpBinary)
z18 = p.LpVariable("z18", cat = p.LpBinary)
z19 = p.LpVariable("z19", cat = p.LpBinary)

# Objective Function
Lp_prob += z0 + z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10 + z11 + z12 + z13 + z14 + z15 + z16 + z17 + z18 + z19

bigM = 10000
# 11 correct equations passing through [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Lp_prob += 11*x0 + 27*x1 + 56*x2 + 17*x3 + 65*x4 + 77*x5 + 85*x6 + 28*x7 + 89*x8 + 46*x9 + -1002 >= -1*bigM*z0
Lp_prob += 92*x0 + 38*x1 + 76*x2 + 29*x3 + 41*x4 + 43*x5 + 93*x6 + 60*x7 + 91*x8 + 77*x9 + -1280 >= -1*bigM*z1
Lp_prob += 49*x0 + 71*x1 + 65*x2 + 94*x3 + 75*x4 + 33*x5 + 72*x6 + 67*x7 + 85*x8 + 83*x9 + -1388 >= -1*bigM*z2
Lp_prob += 50*x0 + 83*x1 + 12*x2 + 89*x3 + 73*x4 + 94*x5 + 48*x6 + 26*x7 + 17*x8 + 11*x9 + -1006 >= -1*bigM*z3
Lp_prob += 18*x0 + 86*x1 + 31*x2 + 96*x3 + 58*x4 + 86*x5 + 59*x6 + 8*x7 + 58*x8 + 81*x9 + -1162 >= -1*bigM*z4
Lp_prob += 37*x0 + 14*x1 + 63*x2 + 74*x3 + 46*x4 + 78*x5 + 48*x6 + 92*x7 + 95*x8 + 41*x9 + -1176 >= -1*bigM*z5
Lp_prob += 11*x0 + 46*x1 + 68*x2 + 13*x3 + 18*x4 + 71*x5 + 30*x6 + 66*x7 + 3*x8 + 62*x9 + -776 >= -1*bigM*z6
Lp_prob += 83*x0 + 91*x1 + 86*x2 + 98*x3 + 100*x4 + 41*x5 + 44*x6 + 90*x7 + 6*x8 + 46*x9 + -1370 >= -1*bigM*z7
Lp_prob += 71*x0 + 11*x1 + 38*x2 + 63*x3 + 10*x4 + 80*x5 + 8*x6 + 31*x7 + 92*x8 + 29*x9 + -866 >= -1*bigM*z8
Lp_prob += 14*x0 + 6*x1 + 74*x2 + 0*x3 + 52*x4 + 77*x5 + 32*x6 + 96*x7 + 96*x8 + 82*x9 + -1058 >= -1*bigM*z9
Lp_prob += 59*x0 + 43*x1 + 100*x2 + 98*x3 + 34*x4 + 32*x5 + 26*x6 + 5*x7 + 15*x8 + 19*x9 + -862 >= -1*bigM*z10
#------------------
Lp_prob += 11*x0 + 27*x1 + 56*x2 + 17*x3 + 65*x4 + 77*x5 + 85*x6 + 28*x7 + 89*x8 + 46*x9 + -1002 <= bigM*z0
Lp_prob += 92*x0 + 38*x1 + 76*x2 + 29*x3 + 41*x4 + 43*x5 + 93*x6 + 60*x7 + 91*x8 + 77*x9 + -1280 <= bigM*z1
Lp_prob += 49*x0 + 71*x1 + 65*x2 + 94*x3 + 75*x4 + 33*x5 + 72*x6 + 67*x7 + 85*x8 + 83*x9 + -1388 <= bigM*z2
Lp_prob += 50*x0 + 83*x1 + 12*x2 + 89*x3 + 73*x4 + 94*x5 + 48*x6 + 26*x7 + 17*x8 + 11*x9 + -1006 <= bigM*z3
Lp_prob += 18*x0 + 86*x1 + 31*x2 + 96*x3 + 58*x4 + 86*x5 + 59*x6 + 8*x7 + 58*x8 + 81*x9 + -1162 <= bigM*z4
Lp_prob += 37*x0 + 14*x1 + 63*x2 + 74*x3 + 46*x4 + 78*x5 + 48*x6 + 92*x7 + 95*x8 + 41*x9 + -1176 <= bigM*z5
Lp_prob += 11*x0 + 46*x1 + 68*x2 + 13*x3 + 18*x4 + 71*x5 + 30*x6 + 66*x7 + 3*x8 + 62*x9 + -776 <= bigM*z6
Lp_prob += 83*x0 + 91*x1 + 86*x2 + 98*x3 + 100*x4 + 41*x5 + 44*x6 + 90*x7 + 6*x8 + 46*x9 + -1370 <= bigM*z7
Lp_prob += 71*x0 + 11*x1 + 38*x2 + 63*x3 + 10*x4 + 80*x5 + 8*x6 + 31*x7 + 92*x8 + 29*x9 + -866 <= bigM*z8
Lp_prob += 14*x0 + 6*x1 + 74*x2 + 0*x3 + 52*x4 + 77*x5 + 32*x6 + 96*x7 + 96*x8 + 82*x9 + -1058 <= bigM*z9
Lp_prob += 59*x0 + 43*x1 + 100*x2 + 98*x3 + 34*x4 + 32*x5 + 26*x6 + 5*x7 + 15*x8 + 19*x9 + -862 <= bigM*z10
# 9 wrong equations
Lp_prob += 27*x0 + 19*x1 + 55*x2 + 1*x3 + 23*x4 + 74*x5 + 26*x6 + 80*x7 + 7*x8 + 95*x9 + 71 >= -1*bigM*z11
Lp_prob += 13*x0 + 82*x1 + 68*x2 + 25*x3 + 93*x4 + 92*x5 + 39*x6 + 49*x7 + 62*x8 + 17*x9 + 100 >= -1*bigM*z12
Lp_prob += 75*x0 + 52*x1 + 3*x2 + 21*x3 + 33*x4 + 27*x5 + 78*x6 + 45*x7 + 87*x8 + 56*x9 + 79 >= -1*bigM*z13
Lp_prob += 28*x0 + 55*x1 + 81*x2 + 85*x3 + 80*x4 + 74*x5 + 81*x6 + 12*x7 + 75*x8 + 97*x9 + 43 >= -1*bigM*z14
Lp_prob += 20*x0 + 32*x1 + 18*x2 + 94*x3 + 84*x4 + 16*x5 + 47*x6 + 89*x7 + 20*x8 + 58*x9 + 96 >= -1*bigM*z15
Lp_prob += 50*x0 + 69*x1 + 14*x2 + 66*x3 + 95*x4 + 9*x5 + 27*x6 + 2*x7 + 61*x8 + 80*x9 + 22 >= -1*bigM*z16
Lp_prob += 15*x0 + 20*x1 + 79*x2 + 91*x3 + 4*x4 + 26*x5 + 42*x6 + 98*x7 + 64*x8 + 20*x9 + 67 >= -1*bigM*z17
Lp_prob += 47*x0 + 7*x1 + 41*x2 + 83*x3 + 24*x4 + 22*x5 + 10*x6 + 86*x7 + 46*x8 + 88*x9 + 72 >= -1*bigM*z18
Lp_prob += 88*x0 + 63*x1 + 66*x2 + 65*x3 + 33*x4 + 83*x5 + 93*x6 + 77*x7 + 96*x8 + 73*x9 + 80 >= -1*bigM*z19
#------------------
Lp_prob += 27*x0 + 19*x1 + 55*x2 + 1*x3 + 23*x4 + 74*x5 + 26*x6 + 80*x7 + 7*x8 + 95*x9 + 71 <= bigM*z11
Lp_prob += 13*x0 + 82*x1 + 68*x2 + 25*x3 + 93*x4 + 92*x5 + 39*x6 + 49*x7 + 62*x8 + 17*x9 + 100 <= bigM*z12
Lp_prob += 75*x0 + 52*x1 + 3*x2 + 21*x3 + 33*x4 + 27*x5 + 78*x6 + 45*x7 + 87*x8 + 56*x9 + 79 <= bigM*z13
Lp_prob += 28*x0 + 55*x1 + 81*x2 + 85*x3 + 80*x4 + 74*x5 + 81*x6 + 12*x7 + 75*x8 + 97*x9 + 43 <= bigM*z14
Lp_prob += 20*x0 + 32*x1 + 18*x2 + 94*x3 + 84*x4 + 16*x5 + 47*x6 + 89*x7 + 20*x8 + 58*x9 + 96 <= bigM*z15
Lp_prob += 50*x0 + 69*x1 + 14*x2 + 66*x3 + 95*x4 + 9*x5 + 27*x6 + 2*x7 + 61*x8 + 80*x9 + 22 <= bigM*z16
Lp_prob += 15*x0 + 20*x1 + 79*x2 + 91*x3 + 4*x4 + 26*x5 + 42*x6 + 98*x7 + 64*x8 + 20*x9 + 67 <= bigM*z17
Lp_prob += 47*x0 + 7*x1 + 41*x2 + 83*x3 + 24*x4 + 22*x5 + 10*x6 + 86*x7 + 46*x8 + 88*x9 + 72 <= bigM*z18
Lp_prob += 88*x0 + 63*x1 + 66*x2 + 65*x3 + 33*x4 + 83*x5 + 93*x6 + 77*x7 + 96*x8 + 73*x9 + 80 <= bigM*z19
#------------------
#------------------
solver = p.PULP_CBC_CMD(threads=16, timeLimit=60)
status = Lp_prob.solve(solver) # Solver
print(p.value(Lp_prob.objective))

# Printing x values
print("x0 = ", p.value(x0))
print("x1 = ", p.value(x1))
print("x2 = ", p.value(x2))
print("x3 = ", p.value(x3))
print("x4 = ", p.value(x4))
print("x5 = ", p.value(x5))
print("x6 = ", p.value(x6))
print("x7 = ", p.value(x7))
print("x8 = ", p.value(x8))
print("x9 = ", p.value(x9))
