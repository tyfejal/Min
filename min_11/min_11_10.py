arr = [[3,2,6,2,4],
       [1,4,2,6,5]]

def KFC(target):
    global arr
    cnt = 0
    for i in range(2):
        for j in range(5):
            if arr[i][j] == target:
                cnt+=1
    if cnt >0:
        return 1
    else: return 0

def main():
    target = int(input())
    value = KFC(target)
    if value == 1:
        print("값이 존재합니다")
    else: print("값이 없습니다")

main()
