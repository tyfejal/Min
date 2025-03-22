a,b = map(int,input().split())
arr = [0]*5
for i in range(5):
    arr[i] = a+(b*i)

print(*arr)