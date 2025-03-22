arr = list(map(int, input().split()))

for i in range(5,-1,-1):
    print(arr[i], end=' ')
    if arr[i]==7: break
    