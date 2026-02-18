from util import fcr
import numpy as np
x = input().split()
p, q, r = fcr(x)
np.set_printoptions(sign= ' ')
print(p)
print(q)
print(r)