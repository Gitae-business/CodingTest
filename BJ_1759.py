from itertools import combinations

# 암호 만들기 https://www.acmicpc.net/problem/1759
def is_valid(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = sum(1 for ch in password if ch in vowels)
    consonant_count = len(password) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

def main():
    l, c = map(int, input().split())
    li = list(input().split())
    li.sort()

    for comb in combinations(li, l):
        if is_valid(comb):
            print("".join(comb))

if __name__ == '__main__':
    main()