# 차집합 https://www.acmicpc.net/problem/1822

def main():
    na, nb = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    
    inter = A & B
    diff = A - inter
    
    print(len(diff))
    [print(a, end=" ") for a in sorted(list(diff))]

if __name__ == '__main__':
    main()
