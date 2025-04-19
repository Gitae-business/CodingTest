from bisect import bisect_left

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = []
    pos = [0] * n   # LIS에 들어간 위치
    past = [-1] * n # 이전 LIS 원소의 인덱스

    indices = []    # dp[i] 위치의 실제 인덱스 저장

    for i, x in enumerate(arr):
        idx = bisect_left(dp, x)
        if idx == len(dp):
            dp.append(x)
            indices.append(i)
        else:
            dp[idx] = x
            indices[idx] = i

        pos[i] = idx
        if idx > 0:
            past[i] = indices[idx - 1]

    lis = []
    lis_len = len(dp) - 1
    k = indices[-1] # 수열 끝 찾기
    for i in reversed(range(n)):
        if pos[i] == lis_len:
            k = i
            break

    while k != -1:  # 역추적하며 LIS 복원
        lis.append(arr[k])
        k = past[k]
    
    lis.reverse()   # 원본 상태로 복귀
    
    print(len(lis))
    print(*lis)


if __name__ == '__main__':
    main()
