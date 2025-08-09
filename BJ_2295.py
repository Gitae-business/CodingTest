# 세 수의 합 https://www.acmicpc.net/problem/2295

def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    
    sum_x_y = set()
    for i in range(n):
        for j in range(i, n):
            sum_x_y.add(arr[i] + arr[j])
    
    for i in range(n - 1, -1, -1):
        for j in range(n):
            k = arr[i]
            z = arr[j]
            
            target = k - z
            
            if target in sum_x_y:
                print(k)
                return


if __name__ == '__main__':
    main()