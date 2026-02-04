# 줄임말 만들기 https://www.acmicpc.net/problem/3181
import sys
input = sys.stdin.readline

def main():
    USELESS = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
    ans = []
    for i, s in enumerate(input().split()):
        if s not in USELESS or i == 0:
            ans.append(str.upper(s[0]))

    print(''.join(ans))

if __name__ == '__main__':
    main()
