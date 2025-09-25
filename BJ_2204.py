# 도비의 난독증 테스트 https://www.acmicpc.net/problem/2204
import heapq

def main():
    while True:
        N = int(input())
        if N == 0:
            return
        
        d = {}
        pq = []
        
        for _ in range(N):
            word = input()
            low = word.lower()
            d[low] = word
            heapq.heappush(pq, low)

        print(d[heapq.heappop(pq)])
        

if __name__ == '__main__':
    main()
