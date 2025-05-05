INF = int(1e9)

def main():
    n = int(input())    # 보드 크기
    w = int(input())    # 사건 수
    locs = [tuple(map(int, input().split())) for _ in range(w)] # 사건 위치 (x, y)

    """
    dp[a][b]: 지금까지의 최소 이동거리
    a, b는 각각 경찰차 1, 2가 마지막으로 처리한 사건 번호
    지금까지 해결한 사건 = map(a, b)
    """
    dp = [[-1] * (w + 1) for _ in range(w + 1)]  
        
    def getDist(a, b):  # 사건 번호로 거리 계산
        ax, ay = (1, 1) if a == 0 else locs[a - 1]
        bx, by = (n, n) if b == 0 else locs[b - 1]
        return abs(ax - bx) + abs(ay - by)

    def solve(a, b):
        if max(a, b) == w:  # 모든 사건 해결했다면
            return 0

        if dp[a][b] != -1:
            return dp[a][b]
        
        next = max(a, b) + 1    # 다음 해결할 사건의 번호
        cop1 = solve(next, b) + getDist(a, next)    # 경찰차 1이 처리
        cop2 = solve(a, next) + getDist(next, b)    # 경찰차 2가 처리

        dp[a][b] = min(cop1, cop2)  # dp 갱신
        return dp[a][b]
    
    # 각 사건을 누가 해결했는지 추적
    def trace(a, b):
        if max(a, b) == w:
            return
        next = max(a, b) + 1
        d1 = getDist(a, next)
        d2 = getDist(next, b)

        if solve(next, b) + d1 < solve(a, next) + d2:   # a로 움직이는데 더 가깝다면
            print(1)
            trace(next, b)
        else:   # b로 움직이는게 더 가깝다면
            print(2)
            trace(a, next)

    print(solve(0, 0))
    trace(0, 0)

if __name__ == '__main__':
    main()
