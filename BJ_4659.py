# 비밀번호 발음하기 https://www.acmicpc.net/problem/4659
VOWELS = ['a', 'e', 'i', 'o', 'u']

def main():
    def isAcceptable(s):
        has_vowel = False
        vowel_cnt = 0
        consonant_cnt = 0
        prev_char = ''
        
        for i, c in enumerate(s):
            if c in VOWELS: # 모음일 경우
                has_vowel = True
                vowel_cnt += 1
                consonant_cnt = 0
            else:           # 자음일 경우
                consonant_cnt += 1
                vowel_cnt = 0

            # 자음/모음 3개 연속
            if vowel_cnt >= 3 or consonant_cnt >= 3:
                return False
            
            # 같은 글자 연속 체크 (ee, oo는 예외)
            if i > 0 and c == prev_char and c not in ['e', 'o']:
                return False

            prev_char = c

        return has_vowel

    while True:
        s = input()
        if s == "end":
            break

        result = "acceptable" if isAcceptable(s) else "not acceptable"
        print(f"<{s}> is {result}.")

if __name__ == '__main__':
    main()
