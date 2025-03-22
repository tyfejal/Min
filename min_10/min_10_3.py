def chicken():
    n = int(input())
    ans = n+10
    return ans
def coke():
    char = input()
    return char

def KFC():
    chicken_value = chicken()
    coke_value = coke()
    print(chicken_value, coke_value, sep='')

def main():
    KFC()

main()