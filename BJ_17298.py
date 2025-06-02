# 오큰수 https://www.acmicpc.net/problem/17298
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    nge = [-1 for _ in range(n)]

    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:    # stack[-1]은 오큰수를 찾지 못한 인덱스
            idx = stack.pop()
            nge[idx] = arr[i]
        stack.append(i)
    
    print(*nge)

if __name__ == '__main__':
    main()
