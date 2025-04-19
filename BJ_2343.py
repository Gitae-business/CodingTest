import math

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    left, right = max(arr), sum(arr)
    ans = right

    while (left <= right):
        mid = math.floor((left+right)/2)
        ls = []
        temp = 0

        for i in arr:
            if (temp+i <= mid):
                temp+=i
            else:
                ls.append(temp)
                temp=i
        
        if (temp>0):
            ls.append(temp)
        
        if (len(ls) <= m):
            ans = mid
            right = mid-1
        else:
            left = mid+1
            
    print(ans)


if __name__ == '__main__':
    main()
