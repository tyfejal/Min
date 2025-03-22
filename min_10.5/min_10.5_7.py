def aToZ():
    char = input()
    if abs(ord(char)-ord('A')) < abs(ord(char)-ord('Z')):
        return 'A'
    else: return 'Z'

def main():
    ret = aToZ()
    print(ret)
main()