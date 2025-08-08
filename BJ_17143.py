# 낚시왕 https://www.acmicpc.net/problem/17143
dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]

def main():
    R, C, M = map(int, input().split())
    sharks = [[(0, 0, 0)] * C for _ in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        sharks[r-1][c-1] = (z, s, d)    # size, velocity, direction
        
    answer = 0

    def catch(x):
        nonlocal answer
        for y in range(R):
            size, _, _ = sharks[y][x]
            if size > 0:
                answer += size
                sharks[y][x] = (0, 0, 0)
                break
        
    def move():
        nonlocal sharks
        new_sharks = [[(0, 0, 0)] * C for _ in range(R)]
        
        for y in range(R):
            for x in range(C):
                size, velocity, direction = sharks[y][x]
                if size == 0:
                    continue

                if direction in (3, 4):  # 가로 이동
                    pattern_x = (C - 1) * 2
                    move_dist = velocity % pattern_x
                    if direction == 3:  # 오른쪽
                        pos = (x + move_dist) % pattern_x
                    else:  # 왼쪽
                        pos = (x - move_dist) % pattern_x
                    if pos >= C:
                        pos = pattern_x - pos
                        direction = 4 if direction == 3 else 3
                    nx, ny = pos, y

                else:  # 세로 이동
                    pattern_y = (R - 1) * 2
                    move_dist = velocity % pattern_y
                    if direction == 2:  # 아래
                        pos = (y + move_dist) % pattern_y
                    else:  # 위
                        pos = (y - move_dist) % pattern_y
                    if pos >= R:
                        pos = pattern_y - pos
                        direction = 1 if direction == 2 else 2
                    nx, ny = x, pos

                loc_size, _, _ = new_sharks[ny][nx]
                if loc_size < size:
                    new_sharks[ny][nx] = (size, velocity, direction)

        sharks = new_sharks

    for player_c in range(C):
        catch(player_c)
        if player_c == C - 1:
            break
        
        move()
        
    print(answer)

if __name__ == '__main__':
    main()
