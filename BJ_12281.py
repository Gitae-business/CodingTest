import heapq

def main():
    T = int(input())
    for n in range(T):
        N = int(input())
        arr = list(map(int, input().split()))

        is_even = []
        evens = []  # 짝수는 내림차순
        odds = []   # 홀수는 오름차순

        for i in arr:
            is_even.append(i % 2 == 0)
            heapq.heappush(evens, -i) if (i % 2 == 0) else heapq.heappush(odds, i)

        ans = []
        for i in is_even:
            if (i):
                ans.append(-heapq.heappop(evens))
            else:
                ans.append(heapq.heappop(odds))

        print(f"Case #{n+1}:", *ans)

if __name__ == '__main__':
    main()
