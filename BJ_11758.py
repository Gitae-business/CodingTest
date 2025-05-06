# CCW
def main():
    points = [list(map(int, input().split())) for _ in range(3)]

    def CCW(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    
    c = CCW(*points)
    if c == 0:
        print(0)
    elif c > 0:
        print(1)
    else:
        print(-1)

if __name__ == '__main__':
    main()
