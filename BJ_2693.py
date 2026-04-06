# N번째 큰 수 https://www.acmicpc.net/problem/2693
import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        arr.sort(reverse=True)
        print(arr[2])

if __name__ == '__main__':
    main()
