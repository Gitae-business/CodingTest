# 겹치는 건 싫어 https://www.acmicpc.net/problem/20922
from collections import defaultdict

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    left = 0
    count = defaultdict(int)
    answer = 0

    for right in range(n):
        count[arr[right]] += 1

        while count[arr[right]] > k:
            count[arr[left]] -= 1
            left += 1
        
        answer = max(answer, right - left + 1)

    print(answer)


if __name__ == '__main__':
    main()
