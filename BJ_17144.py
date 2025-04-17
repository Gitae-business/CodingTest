dx = [1,-1,0,0]
dy = [0,0,1,-1]

def checkIsInRange(nx, ny, r, c):
    return (nx>=0 and nx<c and ny>=0 and ny<r)

def diffusion(origin, r, c):
    temp = [[0 for col in range(c)] for row in range(r)]
    for row in range(r):
        for col in range(c):
            if (origin[row][col] == -1):
                temp[row][col] = -1
                continue

            diff = origin[row][col] // 5

            for d in range(4):
                nx = col + dx[d]
                ny = row + dy[d]

                if not checkIsInRange(nx, ny, r, c): continue # 새 칸이 범위 안에 있는지 확인
                if origin[ny][nx] == -1: continue # 새 칸에 공기청정기 있는지 확인

                temp[ny][nx] += diff
                origin[row][col] -= diff

            temp[row][col] += origin[row][col]

    return temp

def convection(origin, loc1, loc2, r, c):
    temp = [row[:] for row in origin]  # 깊은 복사

    # 위쪽 공기청정기 (반시계 방향)
    top = loc1[0]

    for y in range(top - 1, 0, -1):
        temp[y][0] = origin[y - 1][0]
        
    for x in range(c - 1):
        temp[0][x] = origin[0][x + 1]
        
    for y in range(top):
        temp[y][c - 1] = origin[y + 1][c - 1]
        
    for x in range(c - 1, 1, -1):
        temp[top][x] = origin[top][x - 1]
    temp[top][1] = 0

    # 아래쪽 공기청정기 (시계 방향)
    bottom = loc2[0]

    for y in range(bottom + 1, r - 1):
        temp[y][0] = origin[y + 1][0]
        
    for x in range(c - 1):
        temp[r - 1][x] = origin[r - 1][x + 1]
        
    for y in range(r - 1, bottom, -1):
        temp[y][c - 1] = origin[y - 1][c - 1]
        
    for x in range(c - 1, 1, -1):
        temp[bottom][x] = origin[bottom][x - 1]
    temp[bottom][1] = 0

    # 공기청정기 위치
    temp[loc1[0]][loc1[1]] = -1
    temp[loc2[0]][loc2[1]] = -1

    return temp


def getTotalDust(arr):
    ans = 2
    for rows in arr:
        for c in rows:
           ans += c
    return ans 

def printTable(arr):
    for row in arr:
        print(*row)

def main():
    r, c, t = map(int, input().split())
    arr = []

    for i in range(r):
        arr.append(list(map(int, input().split())))


    aircleans = []
    for i in range(r):
        for j in range(c):
            if (arr[i][j] == -1):
                aircleans.append((i, j))

        if (len(aircleans) == 2):
            break


    while (t):
        t -= 1
        arr = diffusion(arr, r, c)
        arr = convection(arr, aircleans[0], aircleans[1], r, c)

    ans = getTotalDust(arr)
    print(ans)

if __name__ == '__main__':
    main()
