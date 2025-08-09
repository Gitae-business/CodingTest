# 카드 역배치 https://www.acmicpc.net/problem/10804
def main():
    answer = [i for i in range(1, 21)]
    
    for _ in range(10):
        start, end = map(int, input().split())
        start -= 1
        answer[start:end] = answer[start:end][::-1]
    
    print(*answer)
        

if __name__ == '__main__':
    main()
