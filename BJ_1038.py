# 감소하는 수 https://www.acmicpc.net/problem/1038
def main():
    """
    가장 큰 감소하는 수는 9,876,543,210
    DFS를 사용해서 재귀적으로 모든 리스트 생성
    n이 범위 초과시 -1 출력.
    """
    n = int(input())

    arr = []

    # 가능한 경우만 고려해 배열에 추가
    def DFS(num, last):
        arr.append(num)

        for i in range(last):
            DFS(num * 10 + i, i)
    
    for i in range(10):
        DFS(i, i)
    arr.sort()

    print(arr[n] if n < len(arr) else -1)

if __name__ == '__main__':
    main()
