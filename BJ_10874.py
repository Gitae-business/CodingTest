def isPerfect(response):
    for j in range(1, 11):
        ans = ((j - 1) % 5) + 1
        if (response[j-1] != ans):
            return False
    return True

def main():
    N = int(input())
    for i in range(N):
        res = list(map(int, input().split()))
        if (isPerfect(res)): print(i+1)


if __name__ == '__main__':
    main()
