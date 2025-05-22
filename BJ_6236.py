# 용돈 관리 https://www.acmicpc.net/problem/6236
def main():
    n, m = map(int, input().split())
    arr = list(int(input()) for _ in range(n))

    def is_possible(K):
        count = 1  # 인출 횟수
        money = K
        for cost in arr:
            if cost > K:
                return False  # 하루 지출이 인출금보다 크면 불가능
            if money < cost:
                count += 1
                money = K
            money -= cost
        return count <= m

    low = max(arr)      # 하루 중 최대 지출이 최소 인출금
    high = sum(arr)     # 전부 커버하면 최대 인출금
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    print(result)

if __name__ == '__main__':
    main()
