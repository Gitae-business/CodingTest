# A와 B 2 https://www.acmicpc.net/problem/12919
isAble = False

def main():
    s = input()
    t = input()

    def solve(temp):
        global isAble
        if temp == s:
            isAble = True
            return
        elif len(temp) <= len(s):
            return
        
        if temp[-1] == 'A':
            solve(temp[:-1])

        if temp[0] == 'B':
            solve(''.join(reversed(temp))[:-1])

    solve(t)
    print(1 if isAble else 0)

if __name__ == '__main__':
    main()
