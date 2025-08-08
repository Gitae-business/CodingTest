# 이차원 배열과 연산 https://www.acmicpc.net/problem/17140
from collections import Counter

def main():
    r, c, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]

    def sort_arr(arr):
        arr = [x for x in arr if x != 0]
        counter = Counter(arr)
        
        cnt = [[num, counter[num]] for num in counter]
        cnt.sort(key=lambda x: (x[1], x[0]))
        
        flat = [elem for pair in cnt for elem in pair]
        return flat[:100]

    def operate_R():
        nonlocal A
        new_A = []
        max_len = 0
        
        for row in A:
            sorted_row = sort_arr(row)
            max_len = max(max_len, len(sorted_row))
            new_A.append(sorted_row)
            
        for row in new_A:
            row += [0] * (max_len - len(row))
        A = new_A

    def operate_C():
        nonlocal A
        A = list(map(list, zip(*A)))
        operate_R()
        A = list(map(list, zip(*A)))

    def check_k():
        if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]):
            return A[r-1][c-1] == k
        return False

    count = 0
    if check_k():
        print(0)
        return

    while count <= 100:
        rows = len(A)
        cols = len(A[0])
        if rows >= cols:
            operate_R()
        else:
            operate_C()

        count += 1
        if check_k():
            print(count)
            return

    print(-1)

if __name__ == '__main__':
    main()
