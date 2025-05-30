# 구간 나누기 2 https://www.acmicpc.net/problem/13397
def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    def isPossible(limit):
        cnt = 1
        max_v = min_v = arr[0]
        for i in range(1, n):
            max_v = max(max_v, arr[i])
            min_v = min(min_v, arr[i])
            section_score = max_v - min_v
            if section_score > limit:
                cnt += 1
                max_v = min_v = arr[i]
        return cnt <= m
    
    left = 0
    right = max(arr) - min(arr)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if isPossible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)
                

if __name__ == '__main__':
    main()
