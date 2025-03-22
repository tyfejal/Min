def main():
    num = int(input())
    return num
def run():
    rnt = main()
    arr = [[0]*3 for _ in range(3)]
    cnt = 1
    if rnt < 10:
        for i in range(3):
            for j in range(3):
                arr[i][j] = cnt
                cnt+=1
    else:
        for i in range(3):
            for j in range(2,-1,-1):
                arr[i][j] = cnt
                cnt+=1

    for k,l in enumerate(arr):
        print(*l,sep='')

run()