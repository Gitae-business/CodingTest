# 쿼드트리 https://www.acmicpc.net/problem/1992
def main():
    n = int(input())
    board = [input() for _ in range(n)]
    
    def isUniform(x, y, size):
        past = board[y][x]
        for i in range(y, y+size):
            for j in range(x, x+size):
                if board[i][j] != past:
                    return False
        return True

    def quadtree(x, y, size):
        if isUniform(x, y, size):
            print(board[y][x], end='')
            return

        print('(', end='')
        half = size // 2
        quadtree(x, y, half)
        quadtree(x+half, y, half)
        quadtree(x, y+half, half)
        quadtree(x+half, y+half, half)
        print(')', end='')

    quadtree(0, 0, n)

if __name__ == '__main__':
    main()
