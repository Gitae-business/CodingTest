# 개미굴 https://www.acmicpc.net/problem/14725

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        node = self.root
        for item in path:
            if item not in node.children:
                node.children[item] = TrieNode()
            node = node.children[item]
    
    def DFS(self, node = None, depth = 0):
        if node is None:
            node = self.root
        for key in sorted(node.children):
            print("--" * depth + key)
            self.DFS(node.children[key], depth+ 1)
        
def main():
    T = Trie()
    n = int(input())

    for _ in range(n):
        parts = input().split()
        k = int(parts[0])
        path = parts[1:]
        T.insert(path)

    T.DFS()


if __name__ == '__main__':
    main()
