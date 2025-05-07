# 카드 구매하기
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [0 for _ in range(n+1)]
    dp[0] = 0

    '''
    [점화식]
    dp[i]을 카드를 i장 구매할 때의 최소 비용이라고 할 때
    dp[i] = max(dp[i], dp[i - cnt] + cost)
    cnt는 카드의 개수, cost는 카드 구매 비용
    '''

    for i, cost in enumerate(arr):
        cnt = i + 1
        for j in range(cnt, n + 1):
            dp[j] = max(dp[j], dp[j - cnt] + cost)

    print(dp[n])

if __name__ == '__main__':
    main()
