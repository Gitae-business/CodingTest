from collections import deque

def BFS(start):
    q = deque()
    q.append((0, start))

    visited = set()
    visited.add(start)

    while q:
        cost, current = q.popleft()
        visited.add(current)

        if (current == 1):
            return cost
        
        nextNodes = [current-1]
        if (current%3==0): nextNodes.append(current//3)
        if (current%2==0): nextNodes.append(current//2)

        for next in nextNodes:
            if (next not in visited):
                visited.add(next)
                q.append((cost+1, next))

    return -1

def main():
    x = int(input())
    ans = BFS(x)
    print(ans)

if __name__ == '__main__':
    main()
