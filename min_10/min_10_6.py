def main():
    a,b = map(int,input().split())
    result = a//b
    if result%2 == 0:
        even(result)
    else:
        odd(result)

    printData(a+b)

def even(result):
    printData(result*2)

def odd(result):
    printData(result-10)

def printData(result):
    print(result)


main()