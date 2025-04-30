
def main():
    n, k = map(int, input().split())
    li = [int(input()) for _ in range(n)] 

    s = set()
    cnt = {}
    for i in li:
        if i in cnt:
            cnt[i] += 1
            if cnt[i] == 2: s.add(i)
            else: continue
        else:
            cnt[i] = 1
    
    ans = -1
    for i in sorted(list(s), reverse=True):
        if (ans != -1): break
        firstIdx = -1

        for idx, j in enumerate(li):
            if (j == i):
                if (firstIdx == -1):
                    firstIdx = idx
                else:
                    if (idx - firstIdx <= k):
                        ans = i
                        break
                    else:
                        firstIdx = idx
    
    print(ans)


if __name__ == '__main__':
    main()
