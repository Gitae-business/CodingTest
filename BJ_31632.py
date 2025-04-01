# 병신같은 문제 안풀래

# def sol(n, v, r):
#     WLD = defaultdict(set)
#     for idx, state in enumerate(r):
#         WLD[state].add(v[idx])

#     exist_W = 'W' in WLD
#     exist_L = 'L' in WLD
#     exist_D = 'D' in WLD
#     cnt = exist_W + exist_L + exist_D

#     if cnt == 3:    #### WLD
#         print("NO")
#         return

#     elif cnt == 2:  #### WL, LD, WD
#         if (exist_D and (exist_W or exist_L)):  #### WD, LD
#             print("NO")
#             return
#         else:  #### WL
#             # W 또는 L에 두개 이상의 문자가 배정되었다면 NO 반환
#             if (len(WLD['W']) > 1) or (len(WLD['L']) > 1):
#                 print("NO")
#                 return
            
#             # W과 L에 특정한 문자가 확실하게 매칭 가능
#             WL_match = {}
#             for idx, c in enumerate(r):
#                 if c == '?':
#                     continue
                
#                 if c == 'W':
#                     WL_match['W'] = v[idx]
#                     if (v[idx] == 'G'):
#                         WL_match['L'] = 'O'
#                     elif (v[idx] == 'O'):
#                         WL_match['L'] = 'D'
#                     else :
#                         WL_match['L'] = 'G'

#                 elif c == 'L':
#                     WL_match['L'] = v[idx]
#                     if (v[idx] == 'G'):
#                         WL_match['W'] = 'D'
#                     elif (v[idx] == 'O'):
#                         WL_match['W'] = 'G'
#                     else :
#                         WL_match['W'] = 'O'
#                 break

#             result = list(v)
#             for idx, c in enumerate(result):
#                 if (c != '?'): continue
#                 ch = r[idx]
#                 result[idx] = WL_match[ch]
            
#             print("YES")
#             print("".join(result))
#             return

#     else:   #### D, W, L
#         if exist_D: #### D
#             cs = '' # 추가해야 할 문자

#             if (len(WLD['D']) == 1):    # 문자 하나만 존재
#                 for idx, c in enumerate(r):
#                     if (c == 'D'):
#                         cs = v[idx]
#                         break

#             elif (len(WLD['D']) == 3) :   # 문자 3개 존재
#                 cs ='O'  # 아무 문자나 추가

#             else:   # 문자 2개 존재하니 빈 하나만 추가
#                 temp = set(['G', 'O', 'D'])
#                 for idx, c in enumerate(r):
#                     if c == 'D' and v[idx] != '?':
#                         temp.discard(v[idx])

#                 cs = next(iter(temp)) 

#             result = list(v)
#             for idx, c in enumerate(result):
#                 if (c != '?'): continue
#                 result[idx] = cs
            
#             print("YES")
#             print("".join(result))
#             return
#         else:  #### W, L
#             print("NO")
#             return


# G > O, O > D, D > G
beats = {'G': 'O', 'O': 'D', 'D': 'G'}
loses = {v: k for k, v in beats.items()}

def judge(vegs):
    # 각 키위새가 얻는 승점 여부를 판정
    veg_set = set(vegs)
    results = []
    for v in vegs:
        win = beats[v] in veg_set
        lose = loses[v] in veg_set
        if win and not lose:
            results.append('W')
        elif not win and lose:
            results.append('L')
        elif not win and not lose:
            results.append('D')
        else:  # win and lose 모두 있는 경우 => 후처리 필요
            results.append('X')  # 임시로 X 넣고 아래서 처리
    if 'X' in results:
        # 비긴 경우: 모두 W 혹은 모두 L 없음 → 모두 D
        if 'W' not in results and 'L' not in results:
            results = ['D'] * len(vegs)
        else:
            for i in range(len(results)):
                if results[i] == 'X':
                    # W도 있고 L도 있으니 X는 이기거나 진 것
                    if beats[vegs[i]] in veg_set:
                        results[i] = 'W'
                    else:
                        results[i] = 'L'
    return results

def solve_one_case(V, R):
    N = len(V)
    ques = [i for i, v in enumerate(V) if v == '?']
    known = list(V)

    from itertools import product
    for combo in product('GOD', repeat=len(ques)):
        for i, c in zip(ques, combo):
            known[i] = c
        res = judge(known)
        if all(r1 == r2 for r1, r2 in zip(res, R)):
            return "YES\n" + ''.join(known)
    return "NO"

def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        V = input().strip()
        R = input().strip()
        print(solve_one_case(V, R))

if __name__ == '__main__':
    main()