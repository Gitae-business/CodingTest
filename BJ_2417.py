# 정수 제곱근 https://www.acmicpc.net/problem/2417
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    start = 1
    end = n
    answer = end

    while start <= end:
        mid = (start + end) // 2
        
        if n <= mid ** 2:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    print(answer)

if __name__ == '__main__':
    main()
