# 후위 표기식2 https://www.acmicpc.net/problem/1935
from collections import deque

opers = ['+', '-', '*', '/']

def main():
    n = int(input())
    expression = input().strip()
    values = []
    for _ in range(n):
        values.append(int(input()))
        
    d = {}
    for i in range(n):
        d[chr(65 + i)] = values[i]

    stack = deque()
    for c in expression:
        if c in opers:
            b = stack.pop()
            a = stack.pop()
            if c == '+':
                stack.append(a + b)
            elif c == '-':
                stack.append(a - b)
            elif c == '*':
                stack.append(a * b)
            elif c == '/':
                stack.append(a / b)
        else:
            stack.append(d[c])

    answer = stack.pop()
    print(f"{answer:.2f}")

if __name__ == '__main__':
    main()
