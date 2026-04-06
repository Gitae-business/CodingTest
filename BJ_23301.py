import sys
input = sys.stdin.readline

def main():
    N, T = map(int, input().split())
    able = [0] * 1001
    limit = -1

    for i in range(N):
        k = int(input())

        for _ in range(k):
            s, e = map(int, input().split())
            limit = max(limit, e)

            for time in range(s, e):
                able[time] += 1

    temp = sum(able[0:T])
    mx = temp
    ans = 0

    for i in range(1, limit - T + 1):
        temp = temp - able[i - 1] + able[i + T - 1]
        
        if temp > mx:
            mx = temp
            ans = i

    print(ans, ans + T)

if __name__ == '__main__':
    main()