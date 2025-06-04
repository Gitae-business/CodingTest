# 키 순서 https://www.acmicpc.net/problem/2458

def main():
    n, m = map(int, input().split())
    # taller[a][b]: a가 b보다 크면 1, 작으면 0, 모르면 -1
    taller = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())    # 키 a > b
        taller[a][b] = 1    # a는 b보다 큼
        taller[b][a] = 0    # b는 a보다 작음

    for z in range(1, n+1):
        for x in range(1, n+1):
            if z==x: continue
            for y in range(1, n+1):
                if x==y or z==y: continue

                if taller[x][z] == 1 and taller[z][y] == 1:
                    taller[x][y] = 1    # x는 y보다 큼
                    taller[y][x] = 0    # y는 x보다 작음

    answer = 0

    for i in range(1, n+1):
        isAble = True
        for j in range(1, n+1):
            if i == j: continue
            if taller[i][j] == -1:
                isAble = False
                break
        
        if isAble:
            answer += 1
        
    print(answer)

if __name__ == '__main__':
    main()
