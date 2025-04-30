import sys
input = sys.stdin.readline

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
subtree_size = [1] * (N + 1)  # 최소 1 (자기 자신)

# 트리 구성
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 반복 DFS로 서브트리 크기 계산
visited = [False] * (N + 1)
stack = [(R, -1)]
order = []

# 후위 순회 순서 기록
while stack:
    node, parent = stack.pop()
    order.append((node, parent))
    visited[node] = True
    for neighbor in tree[node]:
        if not visited[neighbor]:
            stack.append((neighbor, node))

# 후위 순회로 서브트리 크기 계산
for node, parent in reversed(order):
    if parent != -1:
        subtree_size[parent] += subtree_size[node]

# 쿼리 처리
for _ in range(Q):
    u = int(input())
    print(subtree_size[u])
