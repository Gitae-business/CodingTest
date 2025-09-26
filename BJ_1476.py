# 날짜 계산 https://www.acmicpc.net/problem/1476
import sys
input = sys.stdin.readline

def main():
    E, S, M = map(int, input().split())

    answer = 1
    e, s, m = 1, 1, 1
    while 1:
        if e == E and s == S and m == M:
            print(answer)
            return
        
        answer += 1
        e = e + 1 if e + 1 <= 15 else 1
        s = s + 1 if s + 1 <= 28 else 1
        m = m + 1 if m + 1 <= 19 else 1

if __name__ == '__main__':
    main()
