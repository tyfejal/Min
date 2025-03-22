arr = [[0]*4 for _ in range(4)]

index = 1
for j in range(3,-1,-1):
    for i in range(4):
        arr[i][j] = index
        index += 1

for k,l in enumerate(arr):
    print(*l)