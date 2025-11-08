# 차이를 최대로 https://www.acmicpc.net/problem/10819
import sys
from itertools import permutations
input = sys.stdin.readline

def calc(arr, n):
    res = 0
    for i in range(n - 1):
        res += abs(arr[i] - arr[i+1])
    return res

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0

    for v in permutations(arr, n):
        temp = calc(v, n)
        answer = max(answer, temp)
    
    print(answer)

if __name__ == '__main__':
    main()
