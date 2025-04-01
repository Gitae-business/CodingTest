from collections import deque

def BFS(start, depth):
    global ans
    q = deque([(start, depth)])

    while (q):
        cur, dep = q.popleft()
        
        if (cur == B):
            ans = dep + 1
            return
        
        for i in range(2):
            tmp = cur * 2 if i == 0 else cur * 10 + 1
            if (tmp <= B):
                q.append((tmp, dep + 1))

def main():
    global A, B, ans
    A, B = map(int, input().split())

    ans = -1
    BFS(A, 0)
    print(ans)

if __name__ == '__main__':
    main()
