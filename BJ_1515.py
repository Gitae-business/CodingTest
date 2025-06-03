# 수 이어 쓰기 https://www.acmicpc.net/problem/1515
from collections import deque

def main():
    n = input()
    q = deque(n)

    answer = 0
    while q:
        answer += 1
        for c in str(answer):
            if q and q[0] == c:
                q.popleft()

    print(answer)

if __name__ == '__main__':
    main()
