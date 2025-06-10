# 로마 숫자 https://www.acmicpc.net/problem/2608
from collections import deque
ARAB = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
INT = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }

def main():
    A = input()
    B = input()

    def arabiaToInt(s):
        temp = 0
        q = deque() # 스택처럼 사용. 현재 값이 이전 값보다 크면 이전 값 꺼내고 현재값에서 뺴기
        for c in s:
            current = ARAB[c]
            if q and q[-1] < current:
                current -= q.pop()
            q.append(current)

        while q:
            temp += q.pop()
        return temp

    def intToArabian(n):
        s = ""
        if n >= 1000:
            thous = n // 1000
            s += 'M' * thous

        if n >= 100:
            hunds = (n % 1000) // 100
            if hunds == 9:
                s += 'CM'
            elif hunds >= 5:
                s += 'D' + 'C' * (hunds - 5)
            elif hunds == 4:
                s += 'CD'
            else:
                s += 'C' * hunds

        if n >= 10:
            tens = (n % 100) // 10
            if tens == 9:
                s += 'XC'
            elif tens >= 5:
                s += 'L' + 'X' * (tens - 5)
            elif tens == 4:
                s += 'XL'
            else:
                s += 'X' * tens

        if n >= 1:
            ones = n % 10
            if ones == 9:
                s += 'IX'
            elif ones >= 5:
                s += 'V' + 'I' * (ones - 5)
            elif ones == 4:
                s += 'IV'
            else:
                s += 'I' * ones

        return s
    
    numA = arabiaToInt(A)
    numB = arabiaToInt(B)

    print(numA + numB)
    print(intToArabian(numA + numB))

if __name__ == '__main__':
    main()
