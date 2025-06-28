# 물수제비 (SUJEBI) https://www.acmicpc.net/problem/14931
def main():
    l = int(input())
    scores = [0] + list(map(int, input().split()))

    d, ans = float('inf'), 0
    for length in range(1, l+1):
        t = 0
        for step in range(length, l+1, length):
            t += scores[step]
        
        if t < 0:
            continue
        if t > ans:
            d, ans = length, t
        elif t == ans and length < d:
            d = length

    if ans == 0:
        print(0, 0)
    else:
        print(d, ans)

if __name__ == '__main__':
    main()
