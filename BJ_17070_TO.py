# 방향은 아래를 향하는 방향부터 반시계 방향으로 0, 1, 2로 설정
def DFS(x, y, arr, dir):
    global ans

    if (y == N-1 and x == N-1): # 끝점에 도달하면 카운트 증가 후 DFS 종료
        ans += 1
        return
    
    for i in range(-1, 2):
        new_dir = dir + i
        if (new_dir < 0 or new_dir > 2): continue

        if (new_dir == 0):      # 하단
            if (y+1 < N) and (arr[y+1][x] == 0):
                DFS(x, y+1, arr, new_dir)

        elif (new_dir == 1):    # 우하단
            if (x+1 < N and y+1 < N) and (arr[y+1][x] == 0 and arr[y+1][x+1] == 0 and arr[y][x+1] == 0):
                DFS(x+1, y+1, arr, new_dir)

        else :                  # 우측
            if (x+1 < N) and (arr[y][x+1] == 0):
                DFS(x+1, y, arr, new_dir)

def main():
    global N, ans
    N = int(input())
    ans = 0
    
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    DFS(1, 0, arr, 2)
    print(ans)

if __name__ == '__main__':
    main()
