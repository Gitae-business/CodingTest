# 두 원
import math

def main():
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    
    def solve():
        d = math.hypot(x1 - x2, y1 - y2)    # 두 원의 중심 사이의 거리

        if d >= r1 + r2:        # 겹치지 않을 때
            return 0.0
        elif d <= abs(r1 - r2): # 완전히 겹칠 때
            return math.pi * (min(r1, r2) ** 2)
        
        # 부분만 겹칠 때 - 렌즈 공식 사용
        a1 = r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
        a2 = r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
        a3 = 0.5 * math.sqrt(
            (-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)
        )
        return a1 + a2 - a3
    
    print("{0:.3f}".format(solve()))

if __name__ == '__main__':
    main()
