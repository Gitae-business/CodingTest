from bisect import bisect_left

def main():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key=lambda x: x[0])

    dp = []
    pos = [0] * n       # 원소가 dp에 들어간 위치
    trace = [-1] * n    # 이전 인덱스 추적

    from_idx = [-1] * n # dp[i]가 lines의 몇 번째 index인지 기록

    for i in range(n):
        _, b = lines[i]
        idx = bisect_left(dp, b)
        pos[i] = idx

        if idx == len(dp):
            dp.append(b)
            from_idx[idx] = i
        else:
            dp[idx] = b
            from_idx[idx] = i

        if idx > 0:
            trace[i] = from_idx[idx-1]
    
    l = len(dp)
    
    lis_idx = []
    now = from_idx[l-1]
    while now != -1:
        lis_idx.append(now)
        now = trace[now]
    lis_idx = set(lis_idx)

    print(n - l)
    for i in range(n):
        if i not in lis_idx:
            print(lines[i][0])

if __name__ == '__main__':
    main()
