# Breaking Branches https://www.acmicpc.net/problem/17783
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n & 1 == 0:
        print('Alice')
        print(1)
    else:
        print('Bob')

if __name__ == '__main__':
    main()
