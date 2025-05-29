# 데이터 체커 https://www.acmicpc.net/problem/22942
def main():
    n = int(input())
    circles = []

    for i in range(n):
        x, r = map(int, input().split())
        circles.append((x-r, x+r, i))   # start, end, index

    events = [] # location, isOpen, idx
    for start, end, idx in circles:
        events.append((start, 1, idx))  # 1: Open
        events.append((end, -1, idx))   # -1: Close
    events.sort()

    stack = []
    for _, typ, idx in events:
        if typ == 1:    # open
            stack.append(idx)
        else:           # close
            if not stack or stack[-1] != idx:   # 이전 원이 본인이 아닐 경우 겹친 상태
                print("NO")
                return
            stack.pop()

    print("YES")

if __name__ == '__main__':
    main()