
def main():
    n = int(input())
    times = {}

    for _ in range(n):
        for time in [4, 6, 4, 10]:
            li = list(map(str, input().split()))
            for name in li:
                if name == '-': continue
                if name in times:
                    times[name] += time
                else:
                    times[name] = time

    t = times.values()
    try:
        if (max(t) - min(t) <= 12):
            print("Yes")
        else:
            print("No")
    except:
        print("Yes")

if __name__ == '__main__':
    main()
