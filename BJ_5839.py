# Cow Race https://www.acmicpc.net/problem/5839
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    bessie = [list(map(int, input().split())) for _ in range(N)]
    elsie = [list(map(int, input().split())) for _ in range(M)]

    a = get_segments(bessie)
    b = get_segments(elsie)

    ans = 0
    is_a_lead = False

    for i in range(len(a)):
        if a[i] > b[i]:
            is_a_lead = True
            break
        elif a[i] < b[i]:
            is_a_lead = False
            break

    for i in range(1, len(a)):
        ax = a[i]
        bx = b[i]

        if ax > bx and not is_a_lead:
            ans += 1
            is_a_lead = True
        elif bx > ax and is_a_lead:
            ans += 1
            is_a_lead = False
    
    print(ans)


def get_segments(arr):
    res = []
    l = 0
    for v, t in arr:
        for _ in range(t):
            l += v
            res.append(l)

    return res

if __name__ == '__main__':
    main()
