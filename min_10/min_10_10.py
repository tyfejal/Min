num = int(input())
arr = [[0]*4 for _ in range(3)]
index = 1
for i in range(2,-1,-1):
    for j in range(3,-1,-1):
        arr[i][j] = index
        index+=1
        if j == num:
            arr[i][j] = 0

for k,l in enumerate(arr):
    print(*l)