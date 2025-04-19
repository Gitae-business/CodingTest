from bisect import bisect_left

def main():
    n = int(input())
    ports = list(map(int, input().split()))

    dp = []
    for i in ports:
        idx = bisect_left(dp, i)
        if idx == len(dp):
            dp.append(i)
        else:
            dp[idx] = i

    print(len(dp))

if __name__ == '__main__':
    main()
