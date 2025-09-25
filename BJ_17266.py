# 어두운 굴다리 https://www.acmicpc.net/problem/17266
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())
    arr = list(map(int, input().split()))

    start = 1
    end = 100000
    answer = end

    while start <= end:
        mid = (start + end) // 2
        possible = True

        mn = arr[0] - mid
        mx = arr[0] + mid
        
        if mn > 0:
            possible = False
        else:
            for i in arr[1:]:
                left = i - mid
                right = i + mid

                if left <= mx:
                    mx = right
                else:
                    possible = False
                    break

        if mx < N:
            possible = False

        if possible:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)

if __name__ == '__main__':
    main()
