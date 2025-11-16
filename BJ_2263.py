# 트리의 순회 https://www.acmicpc.net/problem/2263
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def main():
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    pos = [0] * (n + 1)
    for i, v in enumerate(inorder):
        pos[v] = i

    preorder = []

    def solve(in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return
        
        root = postorder[post_end]
        preorder.append(root)

        root_idx = pos[root]
        left_size = root_idx - in_start

        solve(in_start, root_idx-1, post_start, post_start + left_size - 1)
        solve(root_idx + 1, in_end, post_start + left_size, post_end - 1)    
    
    solve(0, n - 1, 0, n - 1)
    print(*preorder)

if __name__ == '__main__':
    main()
