
def main():
    a = input()
    b = input()

    la = len(a)
    lb = len(b)

    dp = [[0 for _ in range(lb+1)] for _ in range(la+1)]

    for i in range(1, la+1):
        for j in range(1, lb+1):
            if (a[i-1] == b[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    i, j = la, lb
    result = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            result.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    result.reverse()
    print(dp[la][lb])
    if (result): print("".join(map(str, result)))


if __name__ == '__main__':
    main()
