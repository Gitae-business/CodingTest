from bisect import bisect_left

def main():
    n = int(input())
    lines = list(map(int, input().split()))

    dp = []

    for i in range(n):
        num = lines[i]
        idx = bisect_left(dp, num)

        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num

    l = len(dp)
    print(n - l)

if __name__ == '__main__':
    main()
