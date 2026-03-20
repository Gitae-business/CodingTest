# 창용이의 시계 https://www.acmicpc.net/problem/12840
import sys
input = sys.stdin.readline

sec = 0

def main():
    global sec
    h, m, s = map(int, input().split())
    sec = h * 3600 + m * 60 + s

    q = int(input())
    for _ in range(q):
        li = list(map(int, input().split()))
        
        if (li[0] == 1): add_time(li[1])
        elif (li[0] == 2): add_time(-li[1])
        else: print_time()

def add_time(s):
    global sec
    sec += 24 * 3600
    sec = (sec + s) % (24 * 3600)
    return sec

def print_time():
    h = sec // 3600
    m = (sec % 3600) // 60
    s = (sec % 60)
    print(f"{h} {m} {s}")


if __name__ == '__main__':
    main()
