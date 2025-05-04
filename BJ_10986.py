
def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    count = {i:0 for i in range(m+1)} # 나머지값의 개수를 저장할 딕셔너리
    count[0] = 1                    # 0 % m == 0

    prefix = 0
    ans = 0

    for i in arr:
        prefix = (prefix + i) % m   # 누적합에 모듈러 적용
        ans += count[prefix]        # 동일한 나머지를 가진 값 2개 선택
        count[prefix] += 1
    
    print(ans)

if __name__ == '__main__':
    main()
