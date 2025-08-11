# 투에-모스 문자열 https://www.acmicpc.net/problem/18222
def main():
    k = int(input())
    
    def solve(n, reverse):
        if n == 0:
            return 0 if not reverse else 1
        
        else:
            if n % 2 == 1:
                return solve(n // 2, not reverse)
            else:
                return solve(n // 2, reverse)
    
    print(solve(k - 1, False))

if __name__ == '__main__':
    main()

