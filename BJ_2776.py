
def main():
    t = int(input())
    while (t):
        t-=1

        n = int(input())
        note1 = list(map(int, input().split()))
        m = int(input())
        note2 = list(map(int, input().split()))

        note1.sort()

        for i in note2:
            isFind = 0
            left = 0
            right = n - 1

            while (left<=right):
                mid = int((left+right)/2)

                if (note1[mid] == i):
                    isFind = 1
                    break
                elif (i < note1[mid]):
                    right = mid-1
                else:
                    left = mid+1
        
            print(isFind)


if __name__ == '__main__':
    main()
