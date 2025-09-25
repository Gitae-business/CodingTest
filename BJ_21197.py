# Stopwatch https://www.acmicpc.net/problem/21197
def main():
    N = int(input())
    times = [int(input()) for _ in range(N)]

    if len(times) % 2 == 1:
        print("still running")
        return
    
    answer = sum([x if idx % 2 == 1 else x * -1 for idx, x in enumerate(times)])
    print(answer)

if __name__ == '__main__':
    main()
