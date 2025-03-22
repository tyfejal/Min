arr = [['F','E','W'],
       ['D','C','A']]

def main():
    char = input()
    return(char)

def findCH(char):
    global arr
    cnt = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j] == char:
                cnt+=1
    if cnt >= 1:
        print("발견")
    else:
        print("미발견")

char = main()
findCH(char)