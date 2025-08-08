# 최솟값 https://www.acmicpc.net/problem/10868
# 세그먼트 트리 자료구조 사용
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        
        while self.size < self.n:
            self.size <<= 1
            
        self.tree = [float('inf')] * (2 * self.size)
        
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[i << 1], self.tree[i << 1 | 1])

    def query(self, left, right):
        left += self.size
        right += self.size
        res = float('inf')
        
        while left <= right:
            if left & 1:
                res = min(res, self.tree[left])
                left += 1
                
            if not (right & 1):
                res = min(res, self.tree[right])
                right -= 1
                
            left >>= 1
            right >>= 1
            
        return res

def main():
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    
    segtree = SegmentTree(arr)
    
    for _ in range(M):
        l, r = map(int, input().split())
        print(segtree.query(l - 1, r - 1))

if __name__ == "__main__":
    main()
