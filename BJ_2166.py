# 신발끈 공식 사용

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]    # 마지막 점은 첫 점과 연결
        ans += (x1 * y2) - (x2 * y1)

    print(f"{abs(ans)/2:.1f}")

if __name__ == '__main__':
    main()
