# PIZZA ALVOLOC
def main():
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    # CCW
    def CCW(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def solve():
        a = (x1, y1); b = (x2, y2); c = (x3, y3); d = (x4, y4)
        ab = CCW(a, b, c) * CCW(a, b, d)
        cd = CCW(c, d, a) * CCW(c, d, b)

        if (ab == 0 and cd == 0):
            if (a > b): b, a = a, b
            if (c > d): d, c = c, d
            return b >= c and d >= a

        return ab < 0 and cd < 0

    print(1 if solve() else 0)

if __name__ == '__main__':
    main()
