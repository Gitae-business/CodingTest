# 줄 세우기 https://www.acmicpc.net/problem/2605
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    answer = []
    
    for idx, a in enumerate(arr):
        answer.insert(len(answer) - a, idx + 1)
        
    print(" ".join(str(a) for a in answer))
    
if __name__ == '__main__':
    main()
