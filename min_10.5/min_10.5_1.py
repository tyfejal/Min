arr = [[0]*4 for _ in  range(4)]
index = 2
for j in range(4):
    for i in range(4):
        arr[i][j] = index
        index+=2
for k,l in enumerate(arr):
    print(*l)