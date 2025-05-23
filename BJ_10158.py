# 개미 https://www.acmicpc.net/problem/10158
def main():
    w, h = map(int, input().split())
    x, y = map(int, input().split())
    t = int(input())

    nx = (x + t) % (2 * w)
    ny = (y + t) % (2 * h)

    if nx > w:
        nx = 2 * w - nx
    if ny > h:
        ny = 2 * h - ny

    print(nx, ny)

if __name__ == '__main__':
    main()

