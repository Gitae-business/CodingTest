# 알고리즘 수업 - 병합 정렬 1 https://www.acmicpc.net/problem/24060
saved_arr = []

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global saved_arr
    i = p
    j = q + 1
    tmp = []
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while i <= q:
        tmp.append(A[i])
        i += 1
    
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    t = 0
    for k in range(p, r + 1):
        A[k] = tmp[t]
        saved_arr.append(A[k])
        t += 1

def main():
    global saved_arr
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    merge_sort(A, 0, n - 1)
    
    if len(saved_arr) < k:
        print(-1)
    else:
        print(saved_arr[k - 1])

if __name__ == '__main__':
    main()
