
def main():
    n = int(input())

    '''
    N   cnt arr
    0   0
    1   1   1
    2   2   11 00
    3   3   111 100 001
    4   5   1111 1100 1001 0011 0000
    
    Dn   Dn-2 + Dn-1
    '''

    dp = [0] * max(n + 1, 5)
    dp[0], dp[1], dp[2], dp[3], dp[4] = (0, 1, 2, 3, 5)
    for i in range(5, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

    print(dp[n])


if __name__ == '__main__':
    main()
