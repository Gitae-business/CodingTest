# 체육은 수학과목 입니다 2 https://www.acmicpc.net/problem/34052
def main():
    laps = [int(input()) for _ in range(4)]
    print("Yes" if sum(laps) <= 1500 else "No")

if __name__ == '__main__':
    main()
