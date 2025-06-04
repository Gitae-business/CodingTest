# 햄버거 분배 https://www.acmicpc.net/problem/19941
import heapq

def main():
    n, k = map(int, input().split())
    table = input()

    people = []
    hamburgers = []

    for i, v in enumerate(table):
        if v == 'H':
            heapq.heappush(hamburgers, i)
        else:
            heapq.heappush(people, i)
    
    answer = 0
    while people:
        p = heapq.heappop(people)
        if not hamburgers:
            break

        if hamburgers[0] > p + k:   # 오른쪽 범위 밖
            continue
        elif hamburgers[0] < p - k: # 왼쪽 범위 밖
            heapq.heappop(hamburgers)
            heapq.heappush(people, p)   # 햄버거 빼고 다시 확인
        else:
            heapq.heappop(hamburgers)
            answer += 1
    
    print(answer)


if __name__ == '__main__':
    main()
