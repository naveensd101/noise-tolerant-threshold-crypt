import random
import numpy as np
p = 997
def gen(n = 10):
    eqs = []
    for i in range(2*n):
        res = ""
        for j in range(n):
            res += (str(random.randint(0, p)) + "*x%d"%j)
            if j != n-1:
                res += ("+")
            elif i < n-1:
                res += ("=="+str(random.randint(0, p)))
            else:
                res += ("==0")
        #eqs.append(f"({res}, 1)")
        eqs.append(f"{res}")
    #print("[")
    for i in eqs:
        print(i, end="\n")
    #print("]")


