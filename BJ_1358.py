# 하키 https://www.acmicpc.net/problem/1358
import math

def main():
    w, h, x, y, p = map(int, input().split())

    def getDist(ax, ay, bx, by):
        return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
    
    def isIn(px, py):
        # 가운데 사각형 안에 있는지 확인 (x, y) ~ (x+w, y+h)
        if (x <= px <= x+w) and (y <= py <= y+h):
            return True

        # 왼쪽 반원 안에 있는지
        r = h/2
        if (getDist(x, y+r, px, py) <= r):
            return True
        
        # 오른쪽 반원 안에 있는지
        if (getDist(x+w, y+r, px, py) <= r):
            return True

        return False

    ans = 0
    for _ in range(p):
        px, py = map(int, input().split())
        if (isIn(px, py)): ans += 1
    print(ans)

if __name__ == '__main__':
    main()
