
def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    intervals = list(map(int, input().split()))

    i = j = 0
    cnt = 0

    tasks.sort()
    intervals.sort()

    while (i < n) and (j < m):
        if tasks[i] <= intervals[j]:
            cnt += 1
            i += 1
            j +=1
        else:
            j += 1

    print(cnt)

if __name__ == '__main__':
    main()
