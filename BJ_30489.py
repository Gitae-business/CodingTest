# apt upgrade https://www.acmicpc.net/problem/30489
import sys
input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(f"{sum(arr[:(m+k)]) / sum(arr) * 100}")

if __name__ == '__main__':
    main()
