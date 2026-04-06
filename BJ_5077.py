# Maps https://www.acmicpc.net/problem/5077
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        solve()

def solve():
    N1, M1 = map(int, input().split())
    image = [input().strip() for _ in range(N1)]

    N2, M2 = map(int, input().split())
    board = [input().strip() for _ in range(N2)]


    ans = 0

    for i in range(N2-N1+1):
        for j in range(M2-M1+1):
            find = True

            for y in range(N1):
                for x in range(M1):
                    if image[y][x] != board[i+y][j+x]:
                        find = False
                        break
                if not find:
                    break

            if find:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()
