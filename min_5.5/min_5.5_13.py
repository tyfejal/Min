arr = [3,4,1,5,8,1,7,7,3,6,9]

num = int(input())

def PrintAll():
    for i in range(0,11,num):
        print(arr[i], end=' ')

PrintAll()