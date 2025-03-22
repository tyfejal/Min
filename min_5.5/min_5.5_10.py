a = int(input())
arr = [0]*6

for i in range(6):
    arr[i] = a+(a*i)

# print(*arr)

for i in arr:
    print(i)