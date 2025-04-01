
def main():
    ans = 0
    votes = list(map(int, input().split()))
    for i in range(1, 5):
        if (votes[0] - votes[i] <= 1000):
            ans += 1
        else: break
    print(ans)

if __name__ == '__main__':
    main()
