# 최솟값 찾기 https://www.acmicpc.net/problem/11003
from collections import deque

def main():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    dq = deque()    # (값, 인덱스) 쌍
    result = []

    for i, v in enumerate(a):
        # 오른쪽에서부터 현재 값보다 큰 값들 제거
        while dq and dq[-1][0] > v:
            dq.pop()
        
        # (값, 인덱스) 추가
        dq.append((v, i))

        # 범위 벗어나는 값 무시
        if dq[0][1] <= i - l:
            dq.popleft()
        
        result.append(dq[0][0])

    print(*result)

if __name__ == '__main__':
    main()
