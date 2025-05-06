# 고층 건물
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        temp = 0
        # 왼쪽
        maxSlope = float('inf')
        for j in range(i-1, -1, -1):
            slope = (arr[j] - arr[i]) / (j - i)
            if slope < maxSlope:
                maxSlope = slope
                temp += 1
        # 오른쪽
        maxSlope = float('-inf')
        for j in range(i+1, n):
            slope = (arr[j] - arr[i]) / (j - i)
            if slope > maxSlope:
                maxSlope = slope
                temp += 1
        ans = max(ans, temp)
    
    print(ans)

if __name__ == '__main__':
    main()
