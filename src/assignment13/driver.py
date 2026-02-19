from util import determinant
if __name__ == '__main__':
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(float, input())))
    result = determinant(matrix)
    print(result)