import sys
from collections import deque
input = sys.stdin.readline

# Dinic 알고리즘 구현
class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        
    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])
        
    def bfs(self, s, t):
        self.level = [-1]*self.n
        q = deque()
        self.level[s] = 0
        q.append(s)
        while q:
            u = q.popleft()
            for v, cap, _ in self.adj[u]:
                if cap and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1
    
    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            v, cap, rev = self.adj[u][i]
            if cap and self.level[u] + 1 == self.level[v]:
                ret = self.dfs(v, t, min(f, cap))
                if ret:
                    self.adj[u][i][1] -= ret
                    self.adj[v][rev][1] += ret
                    return ret
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.it = [0]*self.n
            while True:
                pushed = self.dfs(s, t, float('inf'))
                if not pushed:
                    break
                flow += pushed
        return flow

def main():
    sys.setrecursionlimit(10000)
    # 입력 읽기
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    # 각 날 j (0-indexed)에 대해 결석 허용 최대 인원: cap_j = N - (A[j] + B[j])
    cap = [N - (A[j] + B[j]) for j in range(M)]
    # feasibility check: 각 날에 대해 cap[j] must be >= 0, 그리고 sum(cap) >= N
    for j in range(M):
        if cap[j] < 0:
            print("NO")
            return
    if sum(cap) < N:
        print("NO")
        return

    # 노드 번호 할당
    # source = 0
    # 학생 노드: 1 ~ N
    # 날 노드: N+1 ~ N+M
    # sink = N+M+1
    total_nodes = N + M + 2
    s = 0
    t = total_nodes - 1

    flow_net = Dinic(total_nodes)
    # source -> 학생: 용량 1
    for i in range(1, N+1):
        flow_net.add_edge(s, i, 1)
    # 학생 -> 모든 날: 용량 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            flow_net.add_edge(i, N+j, 1)
    # 날 -> sink: 용량 = cap[j-1]
    for j in range(1, M+1):
        flow_net.add_edge(N+j, t, cap[j-1])
    
    maxf = flow_net.max_flow(s, t)
    if maxf < N:
        print("NO")
        return

    # 이제 각 학생 i (1-indexed)가 어떤 날에 결석하는지 결정됨.
    # 학생 i의 결석일은, among edges from i to day nodes (N+1 to N+M),
    # edge with used flow (capacity reduced from 1 to 0) indicates assignment.
    abs_day = [None]*(N+1)  # abs_day[i]는 학생 i가 결석하는 날 (1-indexed, 1..M)
    for i in range(1, N+1):
        for edge in flow_net.adj[i]:
            v, cap_edge, _ = edge
            # 원래 학생->날 edge의 용량은 1.
            # 만약 flow가 사용되었으면, 해당 edge의 남은 용량이 0.
            if N+1 <= v <= N+M and cap_edge == 0:
                abs_day[i] = v - N  # day 번호 (1-indexed)
                break

    # 이제 각 학생 i (1-indexed)의 결석일이 정해졌으므로,
    # 각 학생의 스케줄을 M 길이 문자열로 구성합니다.
    # schedule[i][j] = 'X' if student i의 결석일 == (j+1) else 결정해야 할 나머지.
    schedule = [[''] * M for _ in range(N)]
    # 먼저, 모든 학생의 결석일에 'X' 할당
    for i in range(1, N+1):
        for j in range(1, M+1):
            if abs_day[i] == j:
                schedule[i-1][j-1] = 'X'
            else:
                schedule[i-1][j-1] = None  # 미할당 상태

    # 이제, 각 날 j (1-indexed)마다 결석하지 않은 학생들을 모아서, 
    # 최소 A[j-1]명을 아침(+)과 최소 B[j-1]명을 저녁(-)으로 배정합니다.
    # 참석 학생 집합: i such that abs_day[i] != j.
    for j in range(1, M+1):
        attend = [i for i in range(1, N+1) if abs_day[i] != j]
        # 참석 학생 수 = N - (# absent on day j). 조건에 따라 N - (# absent) >= A[j-1] + B[j-1].
        if len(attend) < A[j-1] + B[j-1]:
            print("NO")
            return
        # 우선 attend에서 앞 A[j-1]명을 아침('+')으로, 다음 B[j-1]명을 저녁('-')으로 배정하고,
        # 나머지는 아무쪽으로 배정해도 됨 (여기서는 '+'로 배정).
        for idx, i in enumerate(attend):
            if idx < A[j-1]:
                schedule[i-1][j-1] = '+'
            elif idx < A[j-1] + B[j-1]:
                schedule[i-1][j-1] = '-'
            else:
                schedule[i-1][j-1] = '+'

    # 모든 스케줄이 결정되었으므로 출력합니다.
    print("YES")
    for row in schedule:
        print(''.join(row))

if __name__ == '__main__':
    main()
