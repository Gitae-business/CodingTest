def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    ans = []
    ai, bi = 0, 0

    while 1:
        common = set(a[ai:]) & set(b[bi:])
        if not common:
            break

        max_val = max(common)

        ai = a.index(max_val, ai) + 1
        bi = b.index(max_val, bi) + 1
        ans.append(max_val)

    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()
