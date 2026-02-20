# 중앙값 구하기 https://www.acmicpc.net/problem/2696
import sys
import math
import heapq
input = sys.stdin.readline

def solve():
    M = int(input())
    N = (M + 1) // 2
    print(N)

    ans = []
    cnt = 0

    # left의 모든 원소들을 right보다 작게 유지
    left = []   # 최대힙. 부호반전
    right = []  # 최소힙

    for _ in range(math.ceil(M/10)):
        li = list(map(int, input().split()))
        for i in li:
            cnt += 1
            
            if not left or i <= -left[0]:
                heapq.heappush(left, -i)
            else:
                heapq.heappush(right, i)
            
            # left가 하나 더 많거나 같게 유지
            if len(left) > len(right) + 1:
                heapq.heappush(right, -heapq.heappop(left))
            elif len(left) < len(right):
                heapq.heappush(left, -heapq.heappop(right))

            if cnt % 2 == 1:
                ans.append(-left[0])
    
    printAnswer(ans)

def printAnswer(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
        if (i % 10 == 9):
            print()

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
