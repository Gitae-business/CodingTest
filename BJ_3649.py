# 로봇 프로젝트 https://www.acmicpc.net/problem/3649
import sys
input = sys.stdin.readline

def main():
    while True:
        line = input()
        if not line:
            break

        hole = int(line) * 10000000

        N = int(input())
        blocks = [int(input()) for _ in range(N)]
        blocks.sort()

        left, right = 0, N - 1
        found = False

        while left < right:
            current_sum = blocks[left] + blocks[right]
            
            if current_sum == hole:
                print(f"yes {blocks[left]} {blocks[right]}")
                found = True
                break
            elif current_sum < hole:
                left += 1
            else:
                right -= 1

        if not found:
            print("danger")

if __name__ == '__main__':
    main()
