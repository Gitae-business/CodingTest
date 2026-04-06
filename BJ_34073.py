# DORO https://www.acmicpc.net/problem/34073
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    li = list(input().split())

    for i in li:
        print(i + 'DORO', end=" ")

if __name__ == '__main__':
    main()
