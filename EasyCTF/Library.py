from numpy import linalg as LA
import sys
sys.setrecursionlimit(100000)

def result(n):
    numpy.matrix = [[0, 1], [1, 2]]
    matrix2 = matrix ** (n - 1)
    print(matrix2)
    return matrix2[0][0] * 3 + matrix2[0][1] * 7

#print(result(3))
#integer = int(input())
c1 = (1 + 2 ** 0.5) / 2
c2 = (1 - 2 ** 0.5) / 2
x1 = 1 + 2 ** 0.5
x2 = 1 - 2 ** 0.5
#print(round(c1 * x1 ** integer + c2 * x2 ** integer))

n = int(input())
def mul(A, B):
    return [A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3]]

def power(A, p):
    if p == 1:
        return A
    if not p % 2 == 0:
        return mul(A, power(A, p-1))
    X = power(A, p // 2)
    for i in range(len(X)):
        X[i] = X[i] % 1000000007
    return mul(X, X)

def result(n):
    matrix = [0, 1, 1, 2]
    if n == 1:
        return 3
    matrix2 = power(matrix, n - 1)
    return matrix2[0] * 3 + matrix2[1] * 7

M = [0, 1, 1, 2]
power(M, 2 ** 1024 - 1)
print(result(n) % 1000000007)
