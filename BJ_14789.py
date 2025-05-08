# Oversized Pancake Flipper (Large)
def main():
    T = int(input())
    for t in range(1, T+1):
        s, k = map(str, input().split())
        k = int(k)

        arr = [True if i == '+' else False for i in s]  # 모든 arr을 True로

        cnt = 0
        for i in range(len(s) - k + 1):
            if not arr[i]:  # 뒤집기
                cnt += 1
                for j in range(i, i + k):
                    arr[j] = not arr[j]
        
        isHappy = True
        for i in arr:
            if not i:
                isHappy = False
                break

        print(f"Case #{t}:", cnt if isHappy else "IMPOSSIBLE")

if __name__ == '__main__':
    main()

