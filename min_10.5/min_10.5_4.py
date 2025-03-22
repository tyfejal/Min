arr = [['D','A','C','C','D'],
       ['S','D','F','A','E'],
       ['E','E','T','J','H']]

def check(value):
    global arr
    cnt = 0
    for i in range(3):
        for j in range(5):
            if arr[i][j] == value:
                cnt+=1
    if cnt >=1: return 1
    else: return 0


def input1():
    char = input()
    ret = check(char)

    if ret == 1:
        print("있음")
    else:
        print("없음")

def main():
    input1()

main()