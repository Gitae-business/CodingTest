# 오등큰수 https://www.acmicpc.net/problem/17299
from collections import Counter

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = Counter(arr)

    answer = [-1] * n
    stack = []

    for i in range(n):
        while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
            answer[stack.pop()] = arr[i]
        stack.append(i)

    print(' '.join(map(str, answer)))

if __name__ == '__main__':
    main()