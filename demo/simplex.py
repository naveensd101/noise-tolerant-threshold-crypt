# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMinimize)

# Create problem Variables
x0 = p.LpVariable("x0")
x1 = p.LpVariable("x1")
x2 = p.LpVariable("x2")
x3 = p.LpVariable("x3")
x4 = p.LpVariable("x4")
x5 = p.LpVariable("x5")
x7 = p.LpVariable("x7")
x6 = p.LpVariable("x6")
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

# Constraints:

Lp_prob += 98*x0+1*x1+37*x2+93*x3+6*x4+33*x5+91*x6+29*x7+37*x8+38*x9<=94+int(1000)*z0
Lp_prob += 6*x0+93*x1+90*x2+51*x3+30*x4+33*x5+94*x6+98*x7+19*x8+35*x9<=91+int(1000)*z1
Lp_prob += 36*x0+16*x1+63*x2+55*x3+69*x4+86*x5+96*x6+58*x7+74*x8+84*x9<=85+int(1000)*z2
Lp_prob += 61*x0+79*x1+76*x2+0*x3+51*x4+73*x5+10*x6+81*x7+8*x8+52*x9<=39+int(1000)*z3
Lp_prob += 16*x0+82*x1+23*x2+40*x3+48*x4+30*x5+101*x6+62*x7+66*x8+59*x9<=32+int(1000)*z4
Lp_prob += 33*x0+83*x1+23*x2+64*x3+12*x4+45*x5+93*x6+39*x7+25*x8+89*x9<=39+int(1000)*z5
Lp_prob += 40*x0+28*x1+97*x2+16*x3+76*x4+71*x5+6*x6+21*x7+87*x8+7*x9<=100+int(1000)*z6
Lp_prob += 68*x0+34*x1+14*x2+94*x3+75*x4+85*x5+0*x6+1*x7+29*x8+5*x9<=50+int(1000)*z7
Lp_prob += 58*x0+57*x1+81*x2+73*x3+68*x4+46*x5+65*x6+54*x7+83*x8+49*x9<=57+int(1000)*z8
Lp_prob += 37*x0+74*x1+0*x2+1*x3+98*x4+88*x5+65*x6+82*x7+25*x8+4*x9<=0+int(1000)*z9
Lp_prob += 65*x0+53*x1+88*x2+81*x3+33*x4+56*x5+53*x6+84*x7+37*x8+93*x9<=0+int(1000)*z10
Lp_prob += 99*x0+25*x1+55*x2+53*x3+32*x4+48*x5+77*x6+80*x7+91*x8+54*x9<=0+int(1000)*z11
Lp_prob += 32*x0+98*x1+10*x2+91*x3+2*x4+34*x5+87*x6+0*x7+30*x8+43*x9<=0+int(1000)*z12
Lp_prob += 83*x0+24*x1+1*x2+60*x3+66*x4+3*x5+57*x6+29*x7+71*x8+81*x9<=0+int(1000)*z13
Lp_prob += 52*x0+13*x1+90*x2+77*x3+101*x4+97*x5+63*x6+101*x7+69*x8+87*x9<=0+int(1000)*z14
Lp_prob += 5*x0+74*x1+90*x2+81*x3+64*x4+5*x5+95*x6+87*x7+12*x8+32*x9<=0+int(1000)*z15
Lp_prob += 46*x0+16*x1+80*x2+53*x3+94*x4+33*x5+70*x6+88*x7+37*x8+21*x9<=0+int(1000)*z16
Lp_prob += 34*x0+81*x1+54*x2+49*x3+26*x4+6*x5+51*x6+17*x7+61*x8+14*x9<=0+int(1000)*z17
Lp_prob += 17*x0+53*x1+25*x2+81*x3+97*x4+99*x5+97*x6+33*x7+41*x8+8*x9<=0+int(1000)*z18
Lp_prob += 80*x0+28*x1+23*x2+24*x3+29*x4+48*x5+42*x6+11*x7+62*x8+14*x9<=0+int(1000)*z19

Lp_prob += 98*x0+1*x1+37*x2+93*x3+6*x4+33*x5+91*x6+29*x7+37*x8+38*x9>=94-int(1000)*z0
Lp_prob += 6*x0+93*x1+90*x2+51*x3+30*x4+33*x5+94*x6+98*x7+19*x8+35*x9>=91-int(1000)*z1
Lp_prob += 36*x0+16*x1+63*x2+55*x3+69*x4+86*x5+96*x6+58*x7+74*x8+84*x9>=85-int(1000)*z2
Lp_prob += 61*x0+79*x1+76*x2+0*x3+51*x4+73*x5+10*x6+81*x7+8*x8+52*x9>=39-int(1000)*z3
Lp_prob += 16*x0+82*x1+23*x2+40*x3+48*x4+30*x5+101*x6+62*x7+66*x8+59*x9>=32-int(1000)*z4
Lp_prob += 33*x0+83*x1+23*x2+64*x3+12*x4+45*x5+93*x6+39*x7+25*x8+89*x9>=39-int(1000)*z5
Lp_prob += 40*x0+28*x1+97*x2+16*x3+76*x4+71*x5+6*x6+21*x7+87*x8+7*x9>=100-int(1000)*z6
Lp_prob += 68*x0+34*x1+14*x2+94*x3+75*x4+85*x5+0*x6+1*x7+29*x8+5*x9>=50-int(1000)*z7
Lp_prob += 58*x0+57*x1+81*x2+73*x3+68*x4+46*x5+65*x6+54*x7+83*x8+49*x9>=57-int(1000)*z8
Lp_prob += 37*x0+74*x1+0*x2+1*x3+98*x4+88*x5+65*x6+82*x7+25*x8+4*x9>=0-int(1000)*z9
Lp_prob += 65*x0+53*x1+88*x2+81*x3+33*x4+56*x5+53*x6+84*x7+37*x8+93*x9>=0-int(1000)*z10
Lp_prob += 99*x0+25*x1+55*x2+53*x3+32*x4+48*x5+77*x6+80*x7+91*x8+54*x9>=0-int(1000)*z11
Lp_prob += 32*x0+98*x1+10*x2+91*x3+2*x4+34*x5+87*x6+0*x7+30*x8+43*x9>=0-int(1000)*z12
Lp_prob += 83*x0+24*x1+1*x2+60*x3+66*x4+3*x5+57*x6+29*x7+71*x8+81*x9>=0-int(1000)*z13
Lp_prob += 52*x0+13*x1+90*x2+77*x3+101*x4+97*x5+63*x6+101*x7+69*x8+87*x9>=0-int(1000)*z14
Lp_prob += 5*x0+74*x1+90*x2+81*x3+64*x4+5*x5+95*x6+87*x7+12*x8+32*x9>=0-int(1000)*z15
Lp_prob += 46*x0+16*x1+80*x2+53*x3+94*x4+33*x5+70*x6+88*x7+37*x8+21*x9>=0-int(1000)*z16
Lp_prob += 34*x0+81*x1+54*x2+49*x3+26*x4+6*x5+51*x6+17*x7+61*x8+14*x9>=0-int(1000)*z17
Lp_prob += 17*x0+53*x1+25*x2+81*x3+97*x4+99*x5+97*x6+33*x7+41*x8+8*x9>=0-int(1000)*z18
Lp_prob += 80*x0+28*x1+23*x2+24*x3+29*x4+48*x5+42*x6+11*x7+62*x8+14*x9>=0-int(1000)*z19

# Display the problem
print(Lp_prob)

solver = p.PULP_CBC_CMD(threads=16)

status = Lp_prob.solve(solver) # Solver

print(p.LpStatus[status]) # The solution status

# Printing the final solution
print(p.value(Lp_prob.objective))
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

