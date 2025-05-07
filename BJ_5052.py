# 전화번호 목록
def main():
    def isConsistent(arr):
        for i in range(len(arr) - 1):
            if arr[i+1].startswith(arr[i]):
                return False
        return True

    t = int(input())
    while (t):
        t -= 1
        n = int(input())
        arr = [input().strip() for _ in range(n)]

        arr.sort()
        ans = isConsistent(arr)
        print("YES" if ans else "NO")

if __name__ == '__main__':
    main()
