arr = [0]*6

a,b = map(int,input().split())

for i in range(3):
    arr[i] = a+i
# for i in range(3):
#     arr[i+3] = b-(2-i)

# print(*arr)

for i in range(3,6):
    arr[i] = b-(5-i)

print(*arr)