# 수들의 합 2 https://www.acmicpc.net/problem/2003
def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    left = 0
    right = 0
    total = 0
    
    cnt = 0

    while 1:
        if total >= m:
            if total == m:
                cnt += 1
            total -= arr[left]
            left += 1
        elif right == n:
            break
        else:
            total += arr[right]
            right += 1


    print(cnt)

if __name__ == '__main__':
    main()
