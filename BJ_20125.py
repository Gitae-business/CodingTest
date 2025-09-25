# 쿠키의 신체 측정 https://www.acmicpc.net/problem/20125
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def main():
    n = int(input())
    board = [input() for _ in range(n)]

    heartX, heartY = 0, 0
    for i in range(1, n-1):
        for j in range(1, n-1):
            isHeart = True

            for x in range(4):
                nx = j + dx[x]
                ny = i + dy[x]
                if board[ny][nx] != '*':
                    isHeart = False
                    break
            
            if isHeart:
                heartY, heartX = i, j
                break
    
    larm = rarm = 0
    lleg = rleg = 0
    waist = 0

    for x in range(heartX - 1, -1, -1):
        if board[heartY][x] == '*':
            larm += 1
        else:
            break
    
    for x in range(heartX + 1, n):
        if board[heartY][x] == '*':
            rarm += 1
        else:
            break

    waistX, waistY = 0, 0
    for y in range(heartY+1, n):
        if board[y][heartX] == '*':
            waist += 1
        else:
            waistX = heartX
            waistY = y - 1
            break
    
    for y in range(waistY+1, n):
        if board[y][waistX-1] == '*':
            lleg += 1
        else:
            break
    
    for y in range(waistY+1, n):
        if board[y][waistX+1] == '*':
            rleg += 1
        else:
            break

    print(heartY+1, heartX+1)
    print(larm, rarm, waist, lleg, rleg)

if __name__ == '__main__':
    main()
