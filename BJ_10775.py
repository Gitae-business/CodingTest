# 공항 https://www.acmicpc.net/problem/10775
import sys
input = sys.stdin.readline

def main():
    G = int(input())
    P = int(input())
    planes = [int(input()) for _ in range(P)]

    parents = [i for i in range(G+1)]

    def find(node):
        if parents[node] == node:
            return node
        parents[node] = find(parents[node])
        return parents[node]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)

        if parent_a != parent_b:
            parents[parent_a] = parent_b

    answer = 0
    for plane in planes:
        gate = find(plane)

        if gate == 0:
            break

        answer += 1
        union(gate, gate - 1)

    print(answer)

if __name__ == '__main__':
    main()
