def main():
    N = int(input())
    arr = list(map(int, input().split()))

    evens = sum(1 for x in arr if x % 2 == 0)
    odds = N - evens

    ans = 0
    is_even = True
    while 1:
        if (is_even):
            if (evens < 1):
                if (odds < 2):
                    break
                else:
                    evens += 1
                    odds -= 2
            ans += 1
            evens -= 1
            is_even = False

        else:
            if (odds < 1):
                break
            else:
                odds -= 1
                ans += 1
                is_even = True

    if (odds % 2 == 1):
        ans -= 1

    print(ans)

if __name__ == '__main__':
    main()