# 숫자 https://www.acmicpc.net/problem/10093
def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
        
    if b - a <= 1:
        print(0)
        return
    
    print(b - a - 1)
    [print(i, end=" ") for i in range(a+1, b)]

if __name__ == '__main__':
    main()
