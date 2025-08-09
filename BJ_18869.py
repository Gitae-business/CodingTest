# 멀티버스 Ⅱ https://www.acmicpc.net/problem/18869
from collections import defaultdict

def get_rank(arr):
    li = sorted(list(set(arr)))
    rank_map = {val: idx for idx, val in enumerate(li)}
    rank_parts = [str(rank_map[a]) for a in arr]
    return "".join(rank_parts)

def main():
    M, N = map(int, input().split())
    space_dict = defaultdict(int)
    
    for _ in range(M):
        space = list(map(int, input().split()))
        str = get_rank(space)
        space_dict[str] += 1
        
    answer = 0
    for count in space_dict.values():
        if count >= 2:
            answer += count * (count - 1) // 2
    
    print(answer)

if __name__ == '__main__':
    main()
