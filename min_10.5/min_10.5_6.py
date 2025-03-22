a,b = map(int, input().split())
arr = [[0]*3 for _ in range(6)]

index = 10
for j in range(3):
    for i in range(6):
        arr[i][j] = index
        index+=1
    for i in range(a,b+1):
        arr[i][j] = 7

for k,l in enumerate(arr):
    print(*l)