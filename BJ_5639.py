import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):  # 새 노드 삽입
        def _insert(node, key): # 내부 삽입 동작
            if not node:    # 기존 node가 없었다면 생성해 반환
                return Node(key)
            
            if key < node.key:  # node의 key보다 작다면 왼쪽에 삽입
                node.left = _insert(node.left, key)
            elif key > node.key: # node의 key보다 크다면 오른쪽에 삽입
                node.right = _insert(node.right, key)
            return node
        
        self.root = _insert(self.root, key)

    def search(self, key):  # 탐색
        def _search(node, key): # 내부 동작
            if not node:
                return False
            
            if key == node.key: # 찾던 값이면 반환
                return True
            elif key < node.key:    # 루트보다 작으면 왼쪽 탐색
                return _search(node.left, key)
            else:   # 루트보다 크면 오른쪽 탐색
                return _search(node.right, key)
        
        return _search(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, key):  # 삭제
        def _delete(node, key): # 내부동작
            if not node:
                return None
            
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # 삭제할 노드 발견
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
                
            return node
        
        self.root = _delete(self.root, key)

    def postOrder(self, node, result):
        if node:
            self.postOrder(node.left, result)
            self.postOrder(node.right, result)
            result.append(node.key)

    # 기존 후위 순회 함수가 RecursionError가 발생해 이터레이션으로 변환
    def postOrder_iterative(self, root):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.key)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]  # 후위순회는 Left → Right → Root 이므로 역순 필요
    
    

def main():
    bst = BST()
    while True:
        try:
            line = input()
            if not line:
                break
            n = int(line)
            bst.insert(n)
        except EOFError:
            break
    
    res = bst.postOrder_iterative(bst.root)
    
    for i in res:
        print(i)

if __name__ == '__main__':
    main()
