# 휴게소 세우기 https://www.acmicpc.net/problem/1477
INF = int(1e9)

def main():
    n, m, l = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [l]
    arr.sort()  # 휴게소 위치

    # 주어진 만큼의 울타리로 해당 간격 커버 가능한지 판별
    def check(gap, arr, m):
        count = 0
        for i in range(1, len(arr)):
            dist = arr[i] - arr[i-1]
            count += (dist - 1) // gap
        return count <= m

    left = 1
    right = l
    answer = 0
    
    # 이분탐색
    while left <= right:
        mid = (left + right) // 2
        if check(mid, arr, m):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)

if __name__ == '__main__':
    main()
