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

# 11 correct equations passing through [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Lp_prob += 15*x0 + 57*x1 + 27*x2 + 29*x3 + 51*x4 + 0*x5 + 63*x6 + 3*x7 + 6*x8 + 49*x9 + -600 >= -1000*z0
Lp_prob += 36*x0 + 86*x1 + 61*x2 + 25*x3 + 92*x4 + 29*x5 + 59*x6 + 97*x7 + 29*x8 + 86*x9 + -1200 >= -1000*z1
Lp_prob += 3*x0 + 59*x1 + 98*x2 + 66*x3 + 16*x4 + 75*x5 + 87*x6 + 70*x7 + 18*x8 + 17*x9 + -1018 >= -1000*z2
Lp_prob += 59*x0 + 33*x1 + 69*x2 + 30*x3 + 94*x4 + 72*x5 + 75*x6 + 75*x7 + 6*x8 + 8*x9 + -1042 >= -1000*z3
Lp_prob += 40*x0 + 85*x1 + 22*x2 + 28*x3 + 70*x4 + 68*x5 + 38*x6 + 56*x7 + 8*x8 + 29*x9 + -888 >= -1000*z4
Lp_prob += 22*x0 + 3*x1 + 3*x2 + 43*x3 + 36*x4 + 70*x5 + 1*x6 + 21*x7 + 19*x8 + 25*x9 + -486 >= -1000*z5
Lp_prob += 39*x0 + 97*x1 + 44*x2 + 65*x3 + 73*x4 + 85*x5 + 24*x6 + 70*x7 + 66*x8 + 44*x9 + -1214 >= -1000*z6
Lp_prob += 67*x0 + 31*x1 + 97*x2 + 41*x3 + 12*x4 + 11*x5 + 12*x6 + 18*x7 + 100*x8 + 78*x9 + -934 >= -1000*z7
Lp_prob += 72*x0 + 2*x1 + 47*x2 + 46*x3 + 32*x4 + 39*x5 + 21*x6 + 1*x7 + 29*x8 + 75*x9 + -728 >= -1000*z8
Lp_prob += 82*x0 + 97*x1 + 5*x2 + 91*x3 + 97*x4 + 13*x5 + 78*x6 + 28*x7 + 68*x8 + 22*x9 + -1162 >= -1000*z9
Lp_prob += 71*x0 + 61*x1 + 76*x2 + 18*x3 + 57*x4 + 92*x5 + 19*x6 + 12*x7 + 95*x8 + 39*x9 + -1080 >= -1000*z10
#------------------
Lp_prob += 15*x0 + 57*x1 + 27*x2 + 29*x3 + 51*x4 + 0*x5 + 63*x6 + 3*x7 + 6*x8 + 49*x9 + -600 <= 1000*z0
Lp_prob += 36*x0 + 86*x1 + 61*x2 + 25*x3 + 92*x4 + 29*x5 + 59*x6 + 97*x7 + 29*x8 + 86*x9 + -1200 <= 1000*z1
Lp_prob += 3*x0 + 59*x1 + 98*x2 + 66*x3 + 16*x4 + 75*x5 + 87*x6 + 70*x7 + 18*x8 + 17*x9 + -1018 <= 1000*z2
Lp_prob += 59*x0 + 33*x1 + 69*x2 + 30*x3 + 94*x4 + 72*x5 + 75*x6 + 75*x7 + 6*x8 + 8*x9 + -1042 <= 1000*z3
Lp_prob += 40*x0 + 85*x1 + 22*x2 + 28*x3 + 70*x4 + 68*x5 + 38*x6 + 56*x7 + 8*x8 + 29*x9 + -888 <= 1000*z4
Lp_prob += 22*x0 + 3*x1 + 3*x2 + 43*x3 + 36*x4 + 70*x5 + 1*x6 + 21*x7 + 19*x8 + 25*x9 + -486 <= 1000*z5
Lp_prob += 39*x0 + 97*x1 + 44*x2 + 65*x3 + 73*x4 + 85*x5 + 24*x6 + 70*x7 + 66*x8 + 44*x9 + -1214 <= 1000*z6
Lp_prob += 67*x0 + 31*x1 + 97*x2 + 41*x3 + 12*x4 + 11*x5 + 12*x6 + 18*x7 + 100*x8 + 78*x9 + -934 <= 1000*z7
Lp_prob += 72*x0 + 2*x1 + 47*x2 + 46*x3 + 32*x4 + 39*x5 + 21*x6 + 1*x7 + 29*x8 + 75*x9 + -728 <= 1000*z8
Lp_prob += 82*x0 + 97*x1 + 5*x2 + 91*x3 + 97*x4 + 13*x5 + 78*x6 + 28*x7 + 68*x8 + 22*x9 + -1162 <= 1000*z9
Lp_prob += 71*x0 + 61*x1 + 76*x2 + 18*x3 + 57*x4 + 92*x5 + 19*x6 + 12*x7 + 95*x8 + 39*x9 + -1080 <= 1000*z10
# 9 wrong equations
Lp_prob += 25*x0 + 53*x1 + 55*x2 + 86*x3 + 12*x4 + 41*x5 + 90*x6 + 56*x7 + 25*x8 + 36*x9 + 28 >= -1000*z11
Lp_prob += 45*x0 + 91*x1 + 45*x2 + 78*x3 + 58*x4 + 36*x5 + 31*x6 + 15*x7 + 5*x8 + 16*x9 + 75 >= -1000*z12
Lp_prob += 17*x0 + 35*x1 + 72*x2 + 55*x3 + 41*x4 + 2*x5 + 10*x6 + 94*x7 + 8*x8 + 92*x9 + 23 >= -1000*z13
Lp_prob += 15*x0 + 83*x1 + 51*x2 + 93*x3 + 80*x4 + 43*x5 + 65*x6 + 35*x7 + 77*x8 + 70*x9 + 58 >= -1000*z14
Lp_prob += 77*x0 + 92*x1 + 76*x2 + 68*x3 + 100*x4 + 15*x5 + 18*x6 + 60*x7 + 47*x8 + 51*x9 + 4 >= -1000*z15
Lp_prob += 70*x0 + 95*x1 + 68*x2 + 38*x3 + 52*x4 + 44*x5 + 16*x6 + 57*x7 + 45*x8 + 41*x9 + 19 >= -1000*z16
Lp_prob += 51*x0 + 28*x1 + 96*x2 + 25*x3 + 54*x4 + 27*x5 + 51*x6 + 67*x7 + 9*x8 + 100*x9 + 94 >= -1000*z17
Lp_prob += 25*x0 + 95*x1 + 14*x2 + 27*x3 + 94*x4 + 98*x5 + 91*x6 + 15*x7 + 31*x8 + 81*x9 + 24 >= -1000*z18
Lp_prob += 11*x0 + 100*x1 + 65*x2 + 85*x3 + 87*x4 + 23*x5 + 29*x6 + 89*x7 + 71*x8 + 81*x9 + 25 >= -1000*z19
#------------------
Lp_prob += 25*x0 + 53*x1 + 55*x2 + 86*x3 + 12*x4 + 41*x5 + 90*x6 + 56*x7 + 25*x8 + 36*x9 + 28 <= 1000*z11
Lp_prob += 45*x0 + 91*x1 + 45*x2 + 78*x3 + 58*x4 + 36*x5 + 31*x6 + 15*x7 + 5*x8 + 16*x9 + 75 <= 1000*z12
Lp_prob += 17*x0 + 35*x1 + 72*x2 + 55*x3 + 41*x4 + 2*x5 + 10*x6 + 94*x7 + 8*x8 + 92*x9 + 23 <= 1000*z13
Lp_prob += 15*x0 + 83*x1 + 51*x2 + 93*x3 + 80*x4 + 43*x5 + 65*x6 + 35*x7 + 77*x8 + 70*x9 + 58 <= 1000*z14
Lp_prob += 77*x0 + 92*x1 + 76*x2 + 68*x3 + 100*x4 + 15*x5 + 18*x6 + 60*x7 + 47*x8 + 51*x9 + 4 <= 1000*z15
Lp_prob += 70*x0 + 95*x1 + 68*x2 + 38*x3 + 52*x4 + 44*x5 + 16*x6 + 57*x7 + 45*x8 + 41*x9 + 19 <= 1000*z16
Lp_prob += 51*x0 + 28*x1 + 96*x2 + 25*x3 + 54*x4 + 27*x5 + 51*x6 + 67*x7 + 9*x8 + 100*x9 + 94 <= 1000*z17
Lp_prob += 25*x0 + 95*x1 + 14*x2 + 27*x3 + 94*x4 + 98*x5 + 91*x6 + 15*x7 + 31*x8 + 81*x9 + 24 <= 1000*z18
Lp_prob += 11*x0 + 100*x1 + 65*x2 + 85*x3 + 87*x4 + 23*x5 + 29*x6 + 89*x7 + 71*x8 + 81*x9 + 25 <= 1000*z19
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
