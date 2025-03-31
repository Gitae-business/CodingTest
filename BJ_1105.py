
def main():
    L, R = map(int, input().split())
    cnt = float('inf')

    for i in range(L, R+1):
        n = i
        tmp = 0

        while n > 0:
            if n % 10 == 8:
                tmp += 1
            n //= 10

        if n <= 0:
            cnt = min(cnt, tmp)
            if cnt == 0: break

    print(cnt)

if __name__ == '__main__':
    main()
