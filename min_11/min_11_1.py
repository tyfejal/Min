def input1():
    a,b,c = map(int, input().split())
    return a,b,c

def calc():
    a,b,c = input1()
    value = a+b+c
    print(value)

calc()