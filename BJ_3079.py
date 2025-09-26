# 입국심사 https://www.acmicpc.net/problem/3079
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    time = [int(input()) for _ in range(N)]

    start = 0
    end = max(time) * M
    answer = end
    
    while start <= end:
        mid = (start + end) // 2
        total = 0

        for t in time:
            total += mid // t

        if total >= M:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)    

if __name__ == '__main__':
    main()
