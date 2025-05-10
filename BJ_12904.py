# A와 B https://www.acmicpc.net/problem/12904
ans = False

def main():
    S = input()
    T = input()

    while len(T) > len(S):
        if T[-1] == 'A':
            T = T[:-1]
        elif T[-1] == 'B':
            T = T[:-1][::-1]
    
    print(1 if T == S else 0)


if __name__ == '__main__':
    main()
