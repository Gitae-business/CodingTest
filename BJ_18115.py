# 카드 놓기 https://www.acmicpc.net/problem/18115
from collections import deque

def main():
    n = int(input())
    acts = list(map(int, input().split()))

    hand = deque()
    field = deque([i for i in range(1, n+1)])

    for a in reversed(acts):
        card = field.popleft()

        if a == 1:  # 제일 위에 있는 카드 내려놓기
            hand.appendleft(card)
        elif a == 2: # 핸드가 2장 이상일 때 두 번째 카드 내려놓기
            first = hand.popleft()
            hand.appendleft(card)
            hand.appendleft(first)
        elif a == 3: # 핸드가 2장 이상일 때 마지막 카드 내려놓기
            hand.append(card)

    print(*hand)

if __name__ == '__main__':
    main()
