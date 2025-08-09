# 회장뽑기 https://www.acmicpc.net/problem/2660
INF = int(1e9)

def main():
    n = int(input())
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    num_and_score = []
    
    for i in range(1, n+1):
        dp[i][i] = 0
        
    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        
        dp[a][b] = 1
        dp[b][a] = 1
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
      
    for i in range(1, n+1):
        score = max(dp[i][1:])
        num_and_score.append((i, score))
    
    num_and_score.sort(key=lambda x:(x[1], x[0]))
    
    min_score = min([i[1] for i in num_and_score])
    candidates = [i[0] for i in num_and_score if i[1] == min_score]
    
    print(min_score, len(candidates))
    print(*candidates)

if __name__ == '__main__':
    main()
