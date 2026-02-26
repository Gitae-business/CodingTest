# 본대 산책2 https://www.acmicpc.net/problem/12850
import sys
input = sys.stdin.readline
DIV = 1_000_000_007

def main():
    D = int(input())
    A = [[0]*8 for _ in range(8)]
    
    edges = {
        0: [1,2],
        1: [0,2,3],
        2: [0,1,3,4],
        3: [1,2,4,5],
        4: [2,3,5,6],
        5: [3,4,7],
        6: [4,7],
        7: [5,6]
    }
    
    for i in edges:
        for j in edges[i]:
            A[i][j] = 1
    
    result = mat_pow(A, D)
    
    print(result[0][0])

def mat_mul(A, B):
    size = 8
    result = [[0] * size for _ in range(size)]
    
    for i in range(size):
        for k in range(size):
            if A[i][k] == 0:
                continue
            
            for j in range(size):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= DIV

    return result

def mat_pow(matrix, n):
    size = 8
    result = [[0] * size for _ in range(size)]
    
    for i in range(size):
        result[i][i] = 1
    
    while n > 0:
        if n % 2 == 1:
            result = mat_mul(result, matrix)
        matrix = mat_mul(matrix, matrix)
        n //= 2
    
    return result

if __name__ == '__main__':
    main()
