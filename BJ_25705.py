# 돌림판 문자열 https://www.acmicpc.net/problem/25705
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = input().strip()
    chars = set(arr)

    M = int(input())
    S = input().strip()
    
    for c in S:
        if c not in chars:
            print(-1)
            return
    
    ans = 0
    idx = 0
    point = 0
    l = len(S)
    
    while idx < l:
        if S[idx] == arr[point]:
            idx += 1

        point += 1
        ans += 1
        if point >= len(arr):
            point = 0
        
    print(ans)

if __name__ == '__main__':
    main()
