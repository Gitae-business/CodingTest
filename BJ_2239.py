
def isValid(board, x, y, num):
        # 가로
        for i in range(9):
            if board[y][i] == num:
                return False

        # 세로
        for i in range(9):
            if board[i][x] == num:
                return False
        
        # 3X3
        stepX = x // 3
        stepY = y // 3
        for i in range(stepY*3, (stepY+1)*3):
            for j in range(stepX*3, (stepX+1)*3):
                if board[i][j] == num:
                    return False
        
        return True

def DFS(board, blanks, idx):
    if idx == len(blanks):
        for row in board:
            print("".join(map(str, row)))
        exit()
    
    x, y = blanks[idx]
    for num in range(1, 10):
        if isValid(board, x, y, num):
            board[y][x] = num
            DFS(board, blanks, idx+1)
            board[y][x] = 0 # 백트래킹

def main():
    board = [list(map(int, list(input().strip()))) for _ in range(9)]
    blanks = []

    # 사전 순으로 채울 위치 선택
    for y in range(9): 
        for x in range(9):
            if board[y][x] == 0:
                blanks.append((x, y))

    DFS(board, blanks, 0)

if __name__ == '__main__':
    main()
