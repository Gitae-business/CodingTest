# 문서 검색 https://www.acmicpc.net/problem/1543
import sys
input = sys.stdin.readline

def main():
    doc = input().strip()
    word = input().strip()

    ans = 0
    idx = 0
    while doc.find(word, idx) != -1:
        ans += 1
        idx = doc.find(word, idx) + len(word)

    print(ans)

if __name__ == '__main__':
    main()
