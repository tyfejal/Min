num = int(input())
arr = [[0]*3 for _ in range(3)]
if num%5 == 1:
    index = 9
    for j in range(3):
        for i in range(3):
            arr[i][j] = index
            index -=1
    for k,l in enumerate(arr):
        print(*l)
if num%5 == 2:
    index = 1
    for i in range(2,-1,-1):
        for j in range(3):
            arr[i][j] = index
            index +=1
    for k,l in enumerate(arr):
        print(*l)
else:
    index=10
    for j in range(3):
        for i in range(3):
            arr[i][j] = index
            index+=1
    for k,l in enumerate(arr):
        print(*l)