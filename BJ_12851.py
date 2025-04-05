from collections import deque

def BFS(n, k):
    MAX = 100001
    time = [float('inf')] * MAX
    count = [0] * MAX

    q = deque()
    q.append((n, 0))
    time[n] = 0
    count[n] = 1

    while q:
        pos, t = q.popleft()

        for next_pos in [pos - 1, pos + 1, pos * 2]:
            if 0 <= next_pos < MAX:
                if time[next_pos] > t + 1:
                    time[next_pos] = t + 1
                    count[next_pos] = count[pos]
                    q.append((next_pos, t + 1))
                elif time[next_pos] == t + 1:
                    count[next_pos] += count[pos]

    print(time[k])
    print(count[k])

def main():
    n, k = map(int, input().split())
    BFS(n, k)

if __name__ == '__main__':
    main()
