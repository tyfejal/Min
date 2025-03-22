def getChar():
    char1, char2 = input().split()
    if ord(char1)>ord(char2):
        return char1
    else:
        return char2
def main():
    getChar_value = getChar()
    print(getChar_value)

main()