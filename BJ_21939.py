import bisect

# 문제 추천 시스템 Version 1
def main():
    n = int(input())
    quest = {}  # 문제번호
    diff = []   # 난이도

    for _ in range(n):
        P, L = map(int, input().split())
        quest[P] = L
        bisect.insort(diff, (L, P))

    m = int(input())
    for _ in range(m):
        parts = list(map(str, input().split()))     # 명령어 입력
        if parts[0] == 'add':           # add P L
            P, L = int(parts[1]), int(parts[2])
            if P in quest:
                old = quest[P]
                diff.remove((old, P))
            quest[P] = L
            bisect.insort(diff, (L, P))
        elif parts[0] == 'solved':      # solved P
            P = int(parts[1])
            L = quest[P]
            diff.remove((L, P))
            del quest[P]
        elif parts[0] == 'recommend':   # recommend x
            x = int(parts[1])
            if x == 1:
                print(diff[-1][1])
            else:
                print(diff[0][1])

if __name__ == '__main__':
    main()