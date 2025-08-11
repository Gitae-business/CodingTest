# 숫자판 점프 https://www.acmicpc.net/problem/2210
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
SIZE = 5

def main():
    answer_set = set()
    board = [list(map(str, input().split())) for _ in range(SIZE)]

    def dfs(x, y, s):
        if len(s) == 6:
            answer_set.add(s)
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                dfs(nx, ny, s + board[ny][nx])
    
    for i in range(SIZE):
        for j in range(SIZE):
            dfs(j, i, "")
    
    print(len(answer_set))

if __name__ == '__main__':
    main()
