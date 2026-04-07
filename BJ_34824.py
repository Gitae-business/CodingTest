# 연대 다음 고대 https://www.acmicpc.net/problem/34824
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    for s in arr:
        if s == 'yonsei':
            print("Yonsei Won!")
            return
        elif s == 'korea':
            print("Yonsei Lost...")
            return

if __name__ == '__main__':
    main()
