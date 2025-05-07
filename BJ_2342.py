# Dance Dance Revolution
'''
두 발의 위치 [a, b]
시작 위치는 0, 0. 이후 항상 a != b

<드는 힘>
중앙, 상, 좌, 하, 우를 0, 1, 2, 3, 4라 하면
1. 중앙, 0 -> 1/2/3/4                : cost 2
2. 인접, i not 0 -> (i +- 1) % 4 + 1 : cost 3
3. 반대, 1<->3 OR 2<->4              : cost 4  
4. 동일, i -> i                      : cost 1

밟아야 하는 위치가 배열로 주어짐
가장 최소 코스트 찾기
'''
INF = int(1e9)

def main():
    arr = list(map(int, input().split()))
    arr.pop()
    n = len(arr)    # n <= 100,000
    
    # dp[n][a][b]: n번째까지 처리했을 때까지의 비용, 왼발 a, 오른발 b
    dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(n+1)]  
    dp[0][0][0] = 0

    def getCost(past, next):
        if past == next:    # 동일
            return 1
        elif past == 0:     # 중앙
            return 2
        elif abs(past - next) == 2: # 반대
            return 4
        else:               # 인접
            return 3

    for i in range(n):
        next = arr[i]
        for l in range(5):
            for r in range(5):
                if dp[i][l][r] != INF:  # 이전 자세에 도달한 경우가 있을 때만
                    dp[i+1][next][r] = min(dp[i+1][next][r], dp[i][l][r] + getCost(l, next))    # 왼발 이동
                    dp[i+1][l][next] = min(dp[i+1][l][next], dp[i][l][r] + getCost(r, next))    # 오른발 이동

    ans = INF
    for l in range(5):
        for r in range(5):
            ans = min(ans, dp[n][l][r]) # 가능한 모든 발 위치 중의 최소 비용
    print(ans)

if __name__ == '__main__':
    main()
