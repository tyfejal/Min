def main():
    a,b = map(int, input().split())
    return a,b
def BBQ(a,b):
    print(f'합:{a+b}\n차:{a-b}\n곱:{a*b}\n몫:{a//b}')

a,b = main()
BBQ(a,b)
