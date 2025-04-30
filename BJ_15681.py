class Node:
    def __init__(self, node):
        self.node = node
        self.parent = -1
        self.child = []
    
    def addChild(self, node):
        self.child.append(node)
    
    def getChild(self):
        return self.child
    
    def setParent(self, node):
        self.parent = node

    def getParent(self):
        return self.parent

def DFS(current, parent, graph, nodes, subtree_size):
    nodes[current] = Node(current)
    nodes[current].setParent(parent)
    size = 1

    for neighbor in graph[current]:
        if neighbor == parent: continue

        nodes[current].addChild(neighbor)
        child_size = DFS(neighbor, current, graph, nodes, subtree_size)
        size += child_size
    subtree_size[current] = size

    return size

def main():
    N, R, Q = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}

    for _ in range(N - 1):
        U, V = map(int, input().split())
        graph[U].append(V)
        graph[V].append(U)

    nodes = [None] * (N + 1)
    subtree_size = [0] * (N + 1)

    DFS(R, -1, graph, nodes, subtree_size)

    for _ in range(Q):
        u = int(input())
        print(subtree_size[u])

if __name__ == '__main__':
    main()
