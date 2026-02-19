from util import mean
import numpy as np
if __name__ == '__main__':
    a, b = map(float, input())
    matrix = []
    for i in range(a):
        matrix.append(list(map(float, input())))
        p, q, r = mean(matrix)
        print(p)
        print(q)
        print(r)