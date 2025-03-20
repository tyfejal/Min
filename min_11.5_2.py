arr = [[1,1,1],
       [1,2,1],
       [3,6,3]]

def main():
    num = int(input())
    value = Count(num)
    print(value)

def Count(num):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == num:
                cnt+=1
    return cnt

main()