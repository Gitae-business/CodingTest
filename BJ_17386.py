# 선분 교차 1
def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    def CCW(x1, y1, x2, y2, x3, y3):
        return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    # CCW(1,2,3)*CCW(1,2,4) <= 0 and CCW(3,4,1)*CCW(3,4,2) <= 0

    def isIntersect():
        ab = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4)
        cd = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)

        return ab <= 0 and cd <= 0
    
    print(1 if isIntersect() else 0)

if __name__ == '__main__':
    main()
