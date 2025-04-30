
def main():
    n = int(input())
    li = [int(input()) for _ in range(n)]

    sums = int(sum(li) / 2)
    nums = [0] * n

    for i in range(1, n, 2):
        sums -= li[i]
    nums[0] = sums

    for idx, i in enumerate(li[:-1]):
        nums[idx + 1] = i - nums[idx]

    [print(i) for i in nums]

if __name__ == '__main__':
    main()
