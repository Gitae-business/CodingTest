
def backtrack(path, start, s):
    if (len(path) == M):
        print(*path)
        return
    
    for i in range(start, len(s)):
        path.append(s[i])
        backtrack(path, i, s)

        path.pop()

def main():
    global N, M
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 중복제거, 오름차순 정렬된 set
    s = sorted(set(arr))

    backtrack([], 0, s)

if __name__ == '__main__':
    main()
