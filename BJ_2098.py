# 외판원 순회(TSP) https://www.acmicpc.net/problem/2098
def main():
    """
    <비트마스킹>
    이진수에서 각 비트를 플래그로 사용하여 조합을 표현하는 방식
    예: 4개 중 2,4번째를 골랐다면 0b0101로 표현
    이를 사용하여 mask & (1 << n) 같이 n번쨰가 포함되었는지 확인하거나
    mask |= (1 << n), mask |= ~(1 << n)처럼 비트 추가, 반전 가능
    """
        
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]

    maxMask = 1 << n    # 표현해야 하는 최대 마스크
    dp = [[float('inf')] * n for _ in range(maxMask)]   # dp[mask][lastCity]형태의 2차원 배열
    dp[1][0] = 0    # 0으로 가는 경로는 마지막에서 고려

    for mask in range(1, maxMask):  # 모든 마스크에 대해 순회
        for current in range(n):
            if not (mask & (1 << current)): # 이미 도달했던 도시가 있다면
                continue
            
            for next in range(n):
                if mask & (1 << next):          # 이미 다음 도시에 도달했던 경우
                    continue
                if cost[current][next] == 0:    # 도달할 수 없는 경우
                    continue

                nextMask = mask | (1 << next)   # 다음 도시 마스킹
                nextCost = dp[mask][current] + cost[current][next]
                dp[nextMask][next] = min(dp[nextMask][next], nextCost)

    answer = float('inf')
    for last in range(1, n):    # 다른 모든 곳에서 0으로 가는 최소 비용 찾기
        if cost[last][0] == 0:
            continue
        total = dp[maxMask - 1][last] + cost[last][0]
        answer = min(answer, total)

    print(answer)

if __name__ == '__main__':
    main()
