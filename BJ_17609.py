# 회문 https://www.acmicpc.net/problem/17609
def main():
    def is_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def solve(s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # 둘 중 하나 제거하고 회문이 되는지 확인
                if is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1):
                    return 1  # 유사회문
                else:
                    return 2  # 회문 아님
        return 0  # 회문
    
    T = int(input())
    while T:
        T -= 1
        s = input()
        print(solve(s))

if __name__ == '__main__':
    main()
