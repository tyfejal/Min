def main():
    a,b = map(int, input().split())
    return a,b

def sum(a,b):
    return a+b

def comp(a,b):
    return a-b

def print1():
    a,b = main()
    plus = sum(a,b)
    minus = comp(a,b)
    print(f'합:{plus}\n차:{minus}')

print1()