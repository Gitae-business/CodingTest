# 임스와 함께하는 미니게임 https://www.acmicpc.net/problem/25757
def main():
    N, G = input().split()
    game = {'Y': 2, 'F': 3, 'O': 4}
    request = set()

    for _ in range(int(N)):
        user = input()
        request.add(user)
    
    answer = len(request) // (game[G] - 1)
    print(answer)

if __name__ == '__main__':
    main()
