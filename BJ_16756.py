from collections import deque

def main():
    n = int(input())
    intervals = list(map(int, input().split()))
    min_diff = float('inf')

    min_dq = deque()    # 최솟값 후보
    max_dq = deque()    # 최댓값 후보

    l = 0
    for r in range(n):
        # 최솟값 유지
        while (min_dq) and (intervals[min_dq[-1]] >= intervals[r]):
            min_dq.pop()    # 새로 들어오는 값이 기존 deque 마지막 값보다 작으면 해당 값을 대체함
        min_dq.append(r)

        # 최댓값 유지
        while (max_dq) and (intervals[max_dq[-1]] <= intervals[r]):
            max_dq.pop()    # 새로 들어오는 값이 기존 deque 마지막 값보다 크면 해당 값을 대체함
        max_dq.append(r)
    
        while l < r:
            curr_diff = intervals[max_dq[0]] - intervals[min_dq[0]]
            min_diff = min(min_diff, curr_diff)

            l += 1
            if min_dq[0] < l:
                min_dq.popleft()
            if max_dq[0] < l:
                max_dq.popleft()
    
    print(min_diff)

if __name__ == '__main__':
    main()
