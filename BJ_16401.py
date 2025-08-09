# 과자 나눠주기 https://www.acmicpc.net/problem/16401
def main():
    M, N = map(int, input().split())
    snacks = list(map(int, input().split()))
    snacks.sort()
    
    left, right = 0, snacks[-1]
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid == 0:
            left = 1
            continue
        
        cnt = 0
        for snack in snacks:
            cnt += snack // mid
        
        if cnt >= M:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

if __name__ == '__main__':
    main()
