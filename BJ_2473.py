# 세 용액
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    temp = float('inf')
    ans = []

    # 투포인터
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while(left < right):
            s = arr[i] + arr[left] + arr[right]
            if abs(s) < abs(temp):
                temp = s
                ans = [arr[i], arr[left], arr[right]]

            if s == 0:
                break
            elif s < 0:
                left += 1
            else:
                right -= 1

    ans.sort()
    print(*ans)

if __name__ == '__main__':
    main()
