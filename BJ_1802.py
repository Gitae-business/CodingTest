# 종이접기 https://www.acmicpc.net/problem/1802
def main():
    T = int(input())
    
    def recursive(s):
        if len(s) == 1:
            return True

        mid = len(s) // 2
        left = s[:mid]
        right = s[mid + 1:]

        for i in range(mid):
            if left[i] == right[mid - 1 - i]:
                return False

        return recursive(left) and recursive(right)

    for _ in range(T):
        s = input()
        if recursive(s):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()