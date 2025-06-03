# 카드 정렬하기 https://www.acmicpc.net/problem/1715
import heapq

def main():
    n = int(input())
    cards = []
    for _ in range(n):
        i = int(input())
        heapq.heappush(cards, i)
    
    answer = 0
    while cards and len(cards) >= 2:
        p1 = heapq.heappop(cards)
        p2 = heapq.heappop(cards)
        answer += p1 + p2

        heapq.heappush(cards, p1 + p2)

    print(answer)

if __name__ == '__main__':
    main()