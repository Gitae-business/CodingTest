# 레벨 햄버거 https://www.acmicpc.net/problem/16974
def main():
    N, X = map(int, input().split())

    burger_size = [0] * (N + 1)
    patty_count = [0] * (N + 1)
    
    burger_size[0] = 1
    patty_count[0] = 1

    for i in range(1, N + 1):
        burger_size[i] = 2 * burger_size[i - 1] + 3
        patty_count[i] = 2 * patty_count[i - 1] + 1

    def eat(l, x):
        if l == 0:
            return 1 if x == 1 else 0

        if x == 1:
            return 0
        elif 1 < x <= 1 + burger_size[l - 1]:
            return eat(l - 1, x - 1)
        elif x == 1 + burger_size[l - 1] + 1:
            return patty_count[l - 1] + 1
        elif 1 + burger_size[l - 1] + 1 < x <= burger_size[l - 1] * 2 + 2:
            return patty_count[l - 1] + 1 + eat(l - 1, x - burger_size[l - 1] - 2)
        else:
            return patty_count[l]

    print(eat(N, X))

if __name__ == '__main__':
    main()