a,b,c = map(int, input().split())
arr = [[0]*4 for _ in range(3)]

for i in range(3):
    for j in range(4):
        if i == 0:
            arr[i][j] = a
            a+=1
        if i == 1:
            arr[i][j] = b
            b+=1
        if i == 2:
            arr[i][j] = c
            c+=1
for k,l in enumerate(arr):
    print(*l)