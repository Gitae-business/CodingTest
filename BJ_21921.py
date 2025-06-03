# 블로그 https://www.acmicpc.net/problem/21921
def main():
    n, x = map(int, input().split())
    visitors = list(map(int, input().split()))

    cnt = 0
    mx = 0

    sm = sum(visitors[:x])
    if sm > 0:
        if sm > mx:
            cnt = 1
            mx = sm
        elif sm == mx:
            cnt += 1

    for i in range(x, len(visitors)):
        sm = sm + visitors[i] - visitors[i - x]
        if sm > mx:
            cnt = 1
            mx = sm
        elif sm == mx:
            cnt += 1
    
    if mx == 0:
        print("SAD")
        return
    else:
        print(mx)
        print(cnt)


if __name__ == '__main__':
    main()
