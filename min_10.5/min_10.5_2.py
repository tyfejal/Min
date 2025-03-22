arr = [[0]*5 for _ in range(5)]
num = int(input())
index = 1
for j in range(4,-1,-1):
    for i in range(5):
        arr[i][j] = index
        index+=1
        if i == num:
            arr[i][j] = num

for k,l in enumerate(arr):
    print(*l)
