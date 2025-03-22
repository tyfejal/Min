num = int(input())
arr = [[0]*4 for _ in range(4)]
index = 1
if num%2 == 0:
    for cross in range(4):
        i=cross
        j=cross
        arr[i][j] = index
        index+=1
else:
    for cross2 in range(4):
        i = cross2
        j = 3-cross2
        arr[i][j] = index
        index+=1

for i,j in enumerate(arr):
    print(*j)