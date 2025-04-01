def getDivs(n):
    return [i for i in range(2, n+1) if n % i == 0]

def isValid(problems, k):
    n = len(problems)
    size = n//k

    for i in range(k - 1):
        sec_i = problems[i*size : (i+1)*size]
        sec_j = problems[(i+1)*size : (i+2)*size]
        if (max(sec_i) >= min(sec_j)):
            return False
    return True

def main():
    n = int(input())
    problems = [int(input()) for _ in range(n)]

    divs = getDivs(n)
    ans = []

    for k in divs:
        if (isValid(problems, k)):
            ans.append(k)
        
    if len(ans) > 0:
        for k in sorted(ans):
            print(k)
    else:
        print(-1)

if __name__ == '__main__':
    main()
