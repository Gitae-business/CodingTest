# 점프 https://www.acmicpc.net/problem/1890
INF = int(1e9)

def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    
    for y in range(n):
        for x in range(n):
            step = arr[y][x]
            
            if step == 0:
                continue
            
            for d in [(1, 0), (0, 1)]:
                nx = x + d[0] * step
                ny = y + d[1] * step
                
                is_valid_pos = (0 <= nx < n) and (0 <= ny < n)
                if not is_valid_pos:
                    continue
                
                dp[ny][nx] += dp[y][x]
    
    print(dp[n-1][n-1])

if __name__ == '__main__':
    main()
