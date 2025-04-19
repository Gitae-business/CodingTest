import heapq

def main():
    N, K = map(int, input().split())
    jews = []  # (무게, 가치)

    for _ in range(N):
        m, v = map(int, input().split())
        heapq.heappush(jews, (m, v))  # 무게에 대해 오름차순으로 저장

    C = [int(input()) for _ in range(K)]    # 가방 최대 무게
    C.sort()    # 크기에 대해 오름차순 정렬

    ans = 0
    ableVals = []

    for vol in C:
        while jews and jews[0][0] <= vol:
            _, value = heapq.heappop(jews)
            heapq.heappush(ableVals, -value)    # 내림차순 저장

        if ableVals:
            ans += -heapq.heappop(ableVals) # 가장 비싼 거

    print(ans)

if __name__ == '__main__':
    main()
