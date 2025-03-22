def checkChar(char):
    if char.isupper():
        print("대",end='')
    elif char.islower():
        print("소",end='')
    

arr = input().split()

for char in arr:
    checkChar(char)

