
def main():
    n = int(input())
    li = list(map(int, input().split()))

    left = 0
    right = n-1
    ansLeftIdx = 0
    ansRightIdx = n-1

    while(left<right):
        new = li[left] + li[right]
        past = li[ansLeftIdx] + li[ansRightIdx]
        if (abs(new) < abs(past)):
            ansLeftIdx, ansRightIdx = left, right
        else: # 방향 정하기
            nl = left + 1
            nr = right - 1
            leftMoved = li[nl] + li[right]
            rightMoved = li[left] + li[nr]

            if (abs(leftMoved) < abs(rightMoved)):
                left += 1
            else:
                right -= 1

    
    print(li[ansLeftIdx], li[ansRightIdx])


if __name__ == '__main__':
    main()
