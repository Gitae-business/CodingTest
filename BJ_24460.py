# 특별상이라도 받고 싶어 https://www.acmicpc.net/problem/24460

def main():
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    def recursion(x, y, n):
        if n == 1:
            return arr[x][y]
        else:
            temp = []
            temp.append(recursion(x, y, n // 2)) 
            temp.append(recursion(x, y + n // 2, n // 2))
            temp.append(recursion(x + n // 2, y, n // 2))
            temp.append(recursion(x + n // 2, y + n // 2, n // 2))
            
            temp.sort()
            return temp[1]

    print(recursion(0, 0, N))

if __name__ == "__main__":
    main()