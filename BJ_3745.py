from bisect import bisect_left

def main():
    while(1):
        try:
            n = int(input())
            arr = list(map(int, input().split()))

            dp = []
            for i in arr:
                idx = bisect_left(dp, i)
                if len(dp) == idx:
                    dp.append(i)
                else:
                    dp[idx] = i

            print(len(dp))
        except:
            break

if __name__ == '__main__':
    main()
