# 크게 만들기 https://www.acmicpc.net/problem/2812
from collections import deque

def main():
    n, k = map(int, input().split())
    nums = input()
    stack = deque()
    remove_count = k
    
    for c in nums:
        num = int(c)
        
        while stack and remove_count > 0 and stack[-1] < num:
            stack.pop()
            remove_count -= 1
        stack.append(num)
    
    while remove_count > 0:
        stack.pop()
        remove_count -= 1
    
    print(''.join(map(str, stack)))

if __name__ == '__main__':
    main()
