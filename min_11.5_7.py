arr = [['a','b','d'],
       ['e','w','z'],
       ['q','v','a']]


def input1():
    char = input()
    return char
def Process(char):
    value = char.lower()
    flag = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == value:
                flag+=1
                break
    if flag >= 1:
        print("존재")   
    else:
        print("없음")

char = input1()
Process(char)