# 파일 정리 https://www.acmicpc.net/problem/20291
from collections import Counter

def main():
    n = int(input())
    arr = [input().split('.') for _ in range(n)]

    c = Counter([x[1] for x in arr])
    names = list(c.keys())
    names.sort()

    for i in names:
        print(i, c[i])

if __name__ == '__main__':
    main()
