import re

def main():
    t = int(input())
    p = re.compile(r'(100+1+|01)+')

    while (t):
        t -= 1
        s = input()
        print("YES" if p.fullmatch(s) else "NO")

if __name__ == '__main__':
    main()
