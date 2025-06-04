# 문자열 게임 2 https://www.acmicpc.net/problem/20437
from collections import defaultdict

def main():
    t = int(input())
    while t:
        t -= 1

        s = input()
        k = int(input())

        # # 어떤 문자를 정확히 K개 포함하는 가장 짧은 연속 문자열
        d = defaultdict(int)
        shortest = ""
        left = 0
        for right in range(len(s)):
            d[s[right]] += 1
            if d[s[right]] == k:
                while d[s[right]] == k:
                    if shortest == "":
                        shortest = s[left:right+1]
                    elif len(shortest) > (right - left + 1):
                        shortest = s[left:right+1]
                    d[s[left]] -= 1
                    left += 1
        
        # 어떤 문자를 정확히 K개 포함하고, 첫 번째와 마지막 글자가 같은 가장 긴 연속 문자열
        longest = -1
        charIndexes = defaultdict(list)
        for i, c in enumerate(s):
            charIndexes[c].append(i)

        for c in charIndexes:
            idxs = charIndexes[c]
            if len(idxs) >= k:
                for i in range(k-1, len(idxs)):
                    l = idxs[i] - idxs[i-k+1] + 1
                    if longest == -1:
                        longest = l
                    else:
                        longest = max(longest, l)

        if len(shortest) == 0 or longest == -1:
            print(-1)
        else:
            print(len(shortest), longest)

if __name__ == '__main__':
    main()
