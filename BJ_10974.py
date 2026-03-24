# 모든 순열 https://www.acmicpc.net/problem/10974
import sys
from itertools import permutations
input = sys.stdin.readline

def main():
    N = int(input())
    for i in permutations(range(1, N+1)):
        print(*i)

if __name__ == '__main__':
    main()
