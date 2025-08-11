# 치킨 TOP N https://www.acmicpc.net/problem/11582
def main():
    n = int(input())
    chickens = list(map(int, input().split()))
    k = int(input())
    
    step = n // k
    
    def recursive(start, end):
        nonlocal chickens
        
        if (end - start) <= step:
            chickens[start:end] = sorted(chickens[start:end])
            return
        
        mid = (start + end) // 2
        recursive(start, mid)
        recursive(mid, end)

    recursive(0, n)
    print(*chickens)

if __name__ == '__main__':
    main()
