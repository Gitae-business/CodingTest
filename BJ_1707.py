from collections import deque

def main():
    k = int(input())
    while (k):
        k -= 1
        v, e = map(int, input().split())
        graph = {i:[] for i in range(1, v+1)}
        
        for _ in range(e):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        ans = True
        color = [False] * (v + 1)       # 색깔
        visited = [False] * (v + 1)     # 방문
        for start in range(1, v+1):
            if not visited[start]:  # 방문하지 않았을 경우
                q = deque()
                q.append(start)

                visited[start] = True
                color[start] = True

                while q:
                    node = q.popleft()
                    for next in graph[node]:
                        if not visited[next]:
                            color[next] = not color[node]   # 0, 1 반전
                            visited[next] = True
                            q.append(next)
                        elif color[node] == color[next]:
                            ans = False
                            break
                    if not ans: break
            if not ans: break
            
        print("YES" if ans else "NO")

if __name__ == '__main__':
    main()
