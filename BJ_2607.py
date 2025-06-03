# 비슷한 단어 https://www.acmicpc.net/problem/2607
from collections import Counter

def isSimilar(word1, word2):
    c1 = Counter(word1)
    c2 = Counter(word2)

    # 문자 빈도 차이 계산
    diff = 0
    for ch in set(c1.keys()).union(c2.keys()):
        diff += abs(c1[ch] - c2[ch])
    
    # 길이 차이가 2 이상이면 무조건 불가능
    if abs(len(word1) - len(word2)) >= 2:
        return False

    # 완전히 같은 경우
    if diff == 0:
        return True

    # 한 글자만 추가/삭제된 경우
    if diff == 1:
        return True

    # 한 글자 바꾼 경우: 길이 같고 문자 하나씩 다를 때
    if diff == 2 and len(word1) == len(word2):
        return True

    return False

def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    base = words[0]
    answer = 0

    for word in words[1:]:
        if isSimilar(base, word):
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()
