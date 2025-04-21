
def func1(n):
    if (n==1 or n==2):
        return 1
    else:
        return func1(n-1) + func1(n-2)
    
def func2(n):
    return n-2

def main():
    n = int(input())
    print(func1(n), func2(n))

if __name__ == '__main__':
    main()
