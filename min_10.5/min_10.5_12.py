def yesOrNo():
    num = int(input())
    if num%3 ==0:
        return 7
    elif num%3 ==1:
        return 35
    elif num%3 == 2:
        return 50


def main():
    value = yesOrNo()
    print(value)

main()