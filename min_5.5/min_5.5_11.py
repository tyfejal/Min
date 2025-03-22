arr=[0]*6

a,b,c = map(int,input().split())

arr[0] = a
arr[1] = b
arr[2] = c

d = int(input())
for i in range(3):
    arr[i+3] = d+i

for i in arr:
    print(i,end=' ')