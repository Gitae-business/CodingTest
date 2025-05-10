# 돌 게임 https://www.acmicpc.net/problem/9655
def main():
    n = int(input())
    """
    돌 1 또는 3개씩 가져갈 수 있음.
    즉 상대가 돌을 얼마나 가져감에 상관 없이 4개로 조절할 수 있음.
    마지막 돌을 가져가면 이기니, N % 4번째 돌을 가져간 사람이 이김.
    """
    print('SK' if n % 2 == 1 else 'CY')

if __name__ == '__main__':
    main()