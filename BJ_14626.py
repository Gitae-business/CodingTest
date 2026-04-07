# ISBN https://www.acmicpc.net/problem/14626
import sys
input = sys.stdin.readline

def main():
    s = input().strip()

    pos = s.index('*')
    total = 0

    for i, ch in enumerate(s):
        if ch == '*':
            continue
        total += int(ch) * (1 if i % 2 == 0 else 3)

    weight = 1 if pos % 2 == 0 else 3

    for x in range(10):
        if (total + x * weight) % 10 == 0:
            print(x)
            return

if __name__ == '__main__':
    main()