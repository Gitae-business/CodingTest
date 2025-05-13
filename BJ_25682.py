# 체스판 다시 칠하기 2 https://www.acmicpc.net/problem/25682
def main():
    n, m, k = map(int, input().split())
    board = [[c for c in input()] for _ in range(n)]

    # 누적합 준비
    prefix_b = [[0] * (m + 1) for _ in range(n + 1)]  # 시작이 검은색일 때 바꿔야 하는 칸 수
    prefix_w = [[0] * (m + 1) for _ in range(n + 1)]  # 시작이 흰색일 때 바꿔야 하는 칸 수

    # prefix 배열 채우기
    for i in range(n):
        for j in range(m):
            expected_b = 'B' if (i + j) % 2 == 0 else 'W'  # 시작이 B인 체스판의 패턴
            expected_w = 'W' if (i + j) % 2 == 0 else 'B'  # 시작이 W인 체스판의 패턴

            is_wrong_b = 1 if board[i][j] != expected_b else 0
            is_wrong_w = 1 if board[i][j] != expected_w else 0

            prefix_b[i+1][j+1] = prefix_b[i+1][j] + prefix_b[i][j+1] - prefix_b[i][j] + is_wrong_b
            prefix_w[i+1][j+1] = prefix_w[i+1][j] + prefix_w[i][j+1] - prefix_w[i][j] + is_wrong_w

    # 정답 후보 중 최소값 찾기
    ans = float('inf')  # 칠해야 하는 수
    for i in range(k, n + 1):
        for j in range(k, m + 1):
            total_b = prefix_b[i][j] - prefix_b[i-k][j] - prefix_b[i][j-k] + prefix_b[i-k][j-k]
            total_w = prefix_w[i][j] - prefix_w[i-k][j] - prefix_w[i][j-k] + prefix_w[i-k][j-k]
            ans = min(ans, total_b, total_w)

    print(ans)

if __name__ == '__main__':
    main()
