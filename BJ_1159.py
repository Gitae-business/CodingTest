# 농구 경기 https://www.acmicpc.net/problem/1159
import sys
from collections import Counter
input = sys.stdin.readline

def main():
    N = int(input())
    first_chars = [input()[0] for _ in range(N)]
    count = Counter(first_chars)

    ans = []
    for key in count:
        if count[key] >= 5:
            ans.append(key)

    if len(ans) == 0:
        print("PREDAJA")
        return
    
    ans.sort()
    print(''.join(ans))

if __name__ == '__main__':
    main()
