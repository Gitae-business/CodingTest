# 가희와 키워드 https://www.acmicpc.net/problem/22233
import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    keywords_set = set()

    for _ in range(n):
        word = input().strip()
        keywords_set.add(word)

    for _ in range(m):
        writes = input().strip().split(',')
        
        for w in writes:
            if w in keywords_set:
                keywords_set.remove(w)
        
        print(len(keywords_set))

if __name__ == '__main__':
    main()