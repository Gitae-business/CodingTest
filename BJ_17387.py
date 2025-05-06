# 선분 교차 2
def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    def CCW(x1, y1, x2, y2, x3, y3):
        return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    # CCW(1,2,3)*CCW(1,2,4) <= 0 and CCW(3,4,1)*CCW(3,4,2) <= 0
    # 단 겹치거나 닿았는지도 확인

    def isIntersect():
        ab = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4)
        cd = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)
        
        if ab == 0 and cd == 0: # 일직선이라면 범위가 겹치는지
            a = min(x1, x2) <= max(x3, x4)
            b = max(x1, x2) >= min(x3, x4)
            c = min(y1, y2) <= max(y3, y4)
            d = max(y1, y2) >= min(y3, y4)
            return a and b and c and d
        return ab <= 0 and cd <= 0
    
    print(1 if isIntersect() else 0)

if __name__ == '__main__':
    main()
