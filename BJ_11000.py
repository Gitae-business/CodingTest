# 강의실 배정 https://www.acmicpc.net/problem/11000
import heapq

def main():
    n = int(input())
    times = [list(map(int, input().split())) for _ in range(n)]
    times.sort()

    last_time = []  # 가장 빨리 끝나는 수업 시간
    for start, end in times:
        if last_time and last_time[0] <= start: # 다른 수업 시작하는 것보다 빨리 수업을 마칠 수 있다면
            heapq.heappop(last_time)
            
        heapq.heappush(last_time, end)

    print(len(last_time))

if __name__ == '__main__':
    main()
