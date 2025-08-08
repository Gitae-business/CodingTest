# 버블 소트 https://www.acmicpc.net/problem/1517
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    
    def merge_sort(start, end):
        nonlocal arr, cnt
        
        if start < end:
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid + 1, end)
            
            temp = []
            x, y = start, mid + 1
            
            while x <= mid and y <= end:
                if arr[x] <= arr[y]:
                    temp.append(arr[x])
                    x += 1
                else:
                    temp.append(arr[y])
                    y += 1
                    cnt += (mid - x + 1)

            temp += arr[x:mid+1]
            temp += arr[y:end+1]

            for i in range(len(temp)):
                arr[start + i] = temp[i]

    merge_sort(0, N-1)
    print(cnt)

if __name__ == '__main__':
    main()
